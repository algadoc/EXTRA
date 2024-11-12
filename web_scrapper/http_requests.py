import requests
import logging

#logging.basicConfig(level=logging.DEBUG)

first_url = 'https://www.bis.doc.gov/index.php/annual-country-licensing-and-trade-analysis'
second_url = 'https://www.bis.doc.gov/index.php/component/docman/?task=doc_download&gid=3417'

s = requests.Session()
s.get(first_url)
pdf_response = s.get(second_url)
pdf_response.raise_for_status()
print(pdf_response.url)

with open("text_pdf_request.pdf", "wb") as pdf_file:
    pdf_file.write(pdf_response.content)
