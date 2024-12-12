from pypdf import PdfReader
import os
import re
import sys

def process_files_in_trade_directory():
    # Specify the directory containing the PDFs
    directory_path = 'trade_analysis_pdfs'
    
    # Iterate through the files in the directory
    file_info_array = []
    skipped_files = 0
    skipped_paths = []
    errored_files = 0
    errored_paths = []
    for file_name in os.listdir(directory_path):
        # Construct the full path to the file
        file_path = os.path.join(directory_path, file_name)
        
        # Check if it's a file and ends with '.pdf'
        if os.path.isfile(file_path) and file_name.lower().endswith('.pdf'):
            # Process the file
            try:
                absolute_path = os.path.abspath(file_path)
                corrected_file_name = apply_file_name_exceptions(file_name)
                file_info = extract_file_info(corrected_file_name)
                file_info['absolute_file_path'] = absolute_path
                file_info['country'] = apply_country_name_fix(file_info['country'])
                reader = PdfReader(absolute_path)
                file_info['pdf_reader'] = reader
                file_info_array.append(file_info)
                   
            except ValueError:
                errored_files += 1
                errored_paths.append(corrected_file_name)
        else:
            skipped_files += 1
            skipped_paths.append(file_path)

    return (file_info_array,
    skipped_files,
    skipped_paths,
    errored_files,
    errored_paths)

def extract_file_info(filename):
    # Extract file number, year, and the rest of the filename
    match = re.match(r"(\d+)-(\d+)-.*-(?!pdf)(\w+)(?:-pdf\.pdf|\.pdf)", filename)
    if not match:
        raise ValueError("Filename does not match the expected pattern.")
    
    file_number, year, country_section = match.groups()
    year = int(year)
    
    # Logic for determining country name based on year
    country_name = extract_country_name(country_section, year)
    
    return {
        "file_number": file_number,
        "year": year,
        "country": country_name
    }

def extract_country_name(country_section, year):
    country_name = country_section.capitalize()    
    return country_name


def apply_file_name_exceptions(file_name):
    """ Implement hard-coded cases of file name mismatch"""

    # Reasons documented in code
    match file_name:
        case '2519-ukraine-2018-dataportal.pdf':
            # Broken file name, changed to match other files
            return '2519-2018-statistical-analysis-of-u-s-trade-with-ukraine.pdf'
        case '3403-2022-statistical-analysis-of-us-global-trade.pdf':
            # Change to match other world trade files
            return '3403-2022-statistical-analysis-of-u-trade-with-the-world.pdf'
        case '3015-2021-statistical-analysis-of-u-s-trade-with-european-union-countries.pdf':
            # Change to match other EU trade files
            return '3015-2021-statistical-analysis-of-u-s-trade-with-eu.pdf'
        case '2440-2017-statistical-analysis-of-us-trade-with-japan-pdf.pdf':
            # Year errata, should be 2018
            return '2440-2018-statistical-analysis-of-us-trade-with-japan.pdf'

    return file_name

def apply_country_name_fix(country_name):
    """ Implement hard-coded fixes for broken country names caused by the weird dash formatting used on the files"""
    
    match country_name:
        case 'Kong':
            return 'Hong Kong'
        case 'K'|'Kingdom':
            return 'United Kingdom'
        case 'Eu':
            return 'EU'
        case 'Uae':
            return 'UAE'
        case 'Arabia':
            return 'Saudi Arabia'
        case 'Ote':
            return 'Japan'
    return country_name

if __name__ == "__main__":
   (file_info_array, skipped_files, skipped_paths, errored_files, errored_paths) = process_files_in_trade_directory()

   print("Program end")