import os
from dotenv import load_dotenv
import time
import json
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

# Load response object with schema and query
from . import pages_and_queries

# Load pages and queries dictionary, which tell the model what pages to look for in each query and what queries are available


# Load API key
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
  """Waits for the given files to be active.

  Some files uploaded to the Gemini API need to be processed before they can be
  used as prompt inputs. The status can be seen by querying the file's "state"
  field.

  This implementation uses a simple blocking polling loop. Production code
  should probably employ a more sophisticated approach.
  """
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end="", flush=True)
      time.sleep(10)
      file = genai.get_file(name)
    if file.state.name != "ACTIVE":
      raise Exception(f"File {file.name} failed to process")

def find_queries_and_schemas(country: str, year):
  # If country is world, switch to the version of the pages for the world version of the pdf
  pages_index = str(year)
  if country.lower() == "World":
    pages_index = str(year) + "_world"
  return (pages_and_queries.available_queries, pages_and_queries.query_dictionary, pages_and_queries.schema_dictionary, pages_and_queries.pages_dictionary[pages_index])

# Function to process a single report
def extract_information_from_report(country, year, file_path):

  # Get pages and schema dictionaries for this case
  (responses, queries, schemas, pages) = find_queries_and_schemas(country, year)

  # Data extracted by model will be stored here
  response_dictionary = {
    "country" : country,
    "report_year" : year,
    "file_path" :   file_path,
    "export_balance": None,
    "commodities": None,
    "regulatory_authority": None,
    "country_chart": None,
    "top_eccn_by_value": None,
    "top_eccn_by_count": None,
    "export_license": None
  }

  # Create the model
  generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_schema": schemas[responses[0]],
    "response_mime_type": "application/json",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
  )

  files = [
    upload_to_gemini(file_path, mime_type="application/pdf")
  ]

  # Some files have a processing delay. Wait for them to be ready.
  wait_for_files_active(files)

  chat_session = model.start_chat()
  for i_response in responses:
    # Change model schema
    model._generation_config["response_schema"] = schemas[i_response]

    # Get query
    i_query = queries[i_response]
    if pages[i_response] == None:
      continue # For cases when no pages are defined for the query

    i_query = i_query.format(page = pages[i_response], country =country)
    
    if i_response == responses[0]:
      # If this is the first response, upload the file
      model_response = chat_session.send_message([i_query, files[0]])
    
    else:
      model_response = chat_session.send_message([i_query])
    
    # Store response
    response_dictionary[i_response] = json.loads(model_response.text)
      
  return response_dictionary