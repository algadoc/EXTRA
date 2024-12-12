# EXTRA: EXport Regulation and TRade Analytics

This is the repository holding EXTRA, the EXport Regulation and TRade Analytics tool.
**This tool aims to provide a source of information to guide the constructive debate of export control reform**.

This tool is being implemented by Alfonso Lagares and began as his final project for Dr. Roberts INTA 3043 Space Policy class at the Georgia Institute of Technology during the Fall 2024 semester.

## Data sources

The tool aims to agreggate export control data from multiple sources. The marked data sources are the ones currently implemeted. This list can grow as new data sources are included:
[X] - [BIS Trade Analysis Reports](https://www.bis.doc.gov/index.php/annual-country-licensing-and-trade-analysis)
[ ] - [The Commerce Country Chart](https://www.bis.doc.gov/index.php/documents/regulations-docs/federal-register-notices/federal-register-2014/1033-738-supp-1/file).
[ ] - [2018-2022 Report on Deemed Export Licensing](https://www.bis.doc.gov/index.php/documents/technology-evaluation/ote-data-portal/licensing-analysis/3261-statistics-of-deemed-export-licensing-2018-2022/file)

## Parameters

The data available within the tool currently consists of the following parameters:
**Parameter Definition**

A set of target parameters was defined that could be found in all reports across all available years, countries, and formats. These selected parameters are:

1. **Total import and export volume.**
2. **Import and export volume for defined commodity categories.**
3. **Trade volume falling under individual jurisdictions:**
   * Department of State
   * Other USG Agencies
   * Department of Commerce, further subdivided into licensing processes:
     * BIS license
     * BIS license exception
     * NLR reporting an ECCN
     * NLR reporting EAR99
     * NLR not reporting ECCN
     * 600-Series license
4. **Top ten ECCNs by value exported under license, license exception, and NLR with ECCN regimes.**
5. **Top ten ECCNs and description by count exported under license, license exception, and NLR with ECCN regimes.**
6. **Export applications count and resulting outcomes (Approved, Return Without Action, and Denied).**
7. **Deemed Export applications count and resulting outcomes (Approved, Return Without Action, and Denied).**

Reason for Control for each country and year are provided, but the values reported by the model are not accurate and have not been used for analysis.

## Repo structure

The tool is still under development and this structure might change as development continues. The repository currently contrains

### `web_scrapper` and `trade_analysis_pdfs`

`web_scrapper` contains the web scrapping scripts that download the PDF reports from the BIS website. Running `download_pdf.py` will download all available reports into the `trade_analysis_pdfs` directory. The PDFs are not tracked by git to avoid bloating the repository.

### `google_ai_api_interfacing`

Contrains the code needed to interface with the Google Gemini model used to process the BIS reports. The directory `response_schema_objects` contains the schema and queries used to query the model for the tracked parameters. The file `gemini_report_api.py` contains the high-level functions needed to query the model for a given report.

### `run_model_on_files.ipynb`

This notebook loads all available reports in `trade_analysis_pdfs` and provides the functions to gather responses from the model for all the reports. The responses are stored in the `google_ai_responses` directory. Running the notebook from scratch will take around two hours.

### `google_ai_response`

Stores all the JSON objects with the information extracted from the model responses.

### `google_ai_response_analysis`

Contains the analysis performed on the data gathered by the model. The notebook `data_parsing.ipynb` contains the functions used to generate the graphs and csv files in the directory.

## Usage

In order to use the repository, you must create a `.env` key at the root repository and input your own [Google API key](https://aistudio.google.com/u/2/apikey). The `.env` file should follow the following format:

```text
GEMINI_API_KEY = your_api_key
```

The python environment needed to run the repository uses Python 3.10.15 and requires the dependencies listed under the `environment.yaml` file. Conda was used for packet management.
