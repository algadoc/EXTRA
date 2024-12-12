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
4. **Country Chart at the time of making the report and associated Reasons for Control.**
5. **Top ten ECCNs by value exported under license, license exception, and NLR with ECCN regimes.**
6. **Top ten ECCNs and description by count exported under license, license exception, and NLR with ECCN regimes.**
7. **Export applications count and resulting outcomes (Approved, Return Without Action, and Denied).**
8. **Deemed Export applications count and resulting outcomes (Approved, Return Without Action, and Denied).**
