import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Define the URL to scrape
base_url = "https://www.bis.doc.gov/index.php/annual-country-licensing-and-trade-analysis"
root_url = "https://www.bis.doc.gov"

# Set up the directory for saving PDFs
output_folder = "trade_analysis_pdfs"
os.makedirs(output_folder, exist_ok=True)

# Create requester session to be able to download using index links
session = requests.Session()

def get_bis_document(base_bis_url, document_link, s):
    s.get(base_bis_url)
    pdf_response = s.get(document_link)
    pdf_response.raise_for_status()
    return pdf_response

def download_pdfs(base_url):
    # Send a request to fetch the content of the base URL
    response = requests.get(base_url)
    response.raise_for_status()  # Check for request errors
    
    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")
    
    soup = soup.find_all("div", {"itemprop": "articleBody"})
    soup = soup[0]
    # Find all links on the page
    links = soup.find_all("a")
    
    # Filter and download all PDF links
    for link in links:
        pdf_url = link.get("href")
        if pdf_url and "task=doc_download" in pdf_url:
            # Construct the full URL (in case of relative URLs)
            full_redirect_url = urljoin(root_url, pdf_url)
            
            # Download the PDF
            pdf_response = get_bis_document(base_url, full_redirect_url, session)
            pdf_name = pdf_response.url.split('/')[-2] + '.pdf'
            print(f"Downloading {pdf_name}...")
            

            # Save the PDF to the output folder
            pdf_path = os.path.join(output_folder, pdf_name)
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)
                
            print(f"Saved {pdf_name} to {output_folder}")


# Run the function
download_pdfs(base_url)
