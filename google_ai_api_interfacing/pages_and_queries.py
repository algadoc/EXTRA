from . import response_schema_objects
from .response_schema_objects import commodities_response
from .response_schema_objects import country_chart_response
from .response_schema_objects import export_balance_response
from .response_schema_objects import export_license_response
from .response_schema_objects import regulatory_authority_response
from .response_schema_objects import top_eccn_by_count_response
from .response_schema_objects import top_eccn_by_value_response

available_queries = [
    "export_balance",
    "commodities",
    "regulatory_authority",
    "country_chart",
    "top_eccn_by_value",
    "top_eccn_by_count",
    "export_license"
]

query_dictionary = {
    "export_balance" : export_balance_response.export_balance_query,
    "commodities" : commodities_response.commodities_query,
    "regulatory_authority" : regulatory_authority_response.regulatory_authority_query,
    "country_chart" : country_chart_response.country_chart_query,
    "top_eccn_by_value" : top_eccn_by_value_response.top_eccn_by_value_query,
    "top_eccn_by_count" : top_eccn_by_count_response.top_eccn_by_count_query,
    "export_license" : export_license_response.export_license_query
}

schema_dictionary = {
    "export_balance" : export_balance_response.export_balance_schema,
    "commodities" : commodities_response.commodities_schema,
    "regulatory_authority" : regulatory_authority_response.regulatory_authority_schema,
    "country_chart" : country_chart_response.country_chart_schema,
    "top_eccn_by_value" : top_eccn_by_value_response.top_eccn_by_value_schema,
    "top_eccn_by_count" : top_eccn_by_count_response.top_eccn_by_count_schema,
    "export_license" : export_license_response.export_license_schema
}

pages_dictionary = {
    "2018" : {
        "export_balance" : "1",
        "commodities" : "2",
        "regulatory_authority" : "3",
        "country_chart" : "3",
        "top_eccn_by_value" : "6", 
        "top_eccn_by_count" : "7",
        "export_license" : "8"
    },
    "2018_world" : {
        "export_balance" : "1",
        "commodities" : "2",
        "regulatory_authority" : "6",
        "country_chart" : None,
        "top_eccn_by_value" : "10", 
        "top_eccn_by_count" : "11",
        "export_license" : "12 and 14"
    },
    "2019" : {
        "export_balance" : "1 and 2",
        "commodities" : "2 or 3",
        "regulatory_authority" : "3 or 4",
        "country_chart" : "3 or 4",
        "top_eccn_by_value" : "6 or 7", 
        "top_eccn_by_count" : "7 or 8",
        "export_license" : "8 and 9"
    },
    "2019_world" : {
        "export_balance" : "1",
        "commodities" : "2",
        "regulatory_authority" : "5",
        "country_chart" : None,
        "top_eccn_by_value" : "8", 
        "top_eccn_by_count" : "9",
        "export_license" : "10, 11 and 12"
    },
    "2020" : {
        "export_balance" : "1 and 2",
        "commodities" : "2 or 3",
        "regulatory_authority" : "3 or 4",
        "country_chart" : "3 or 4",
        "top_eccn_by_value" : "6 or 7", 
        "top_eccn_by_count" : "7 or 8",
        "export_license" : "8 and 9"
    },
    "2020_world" : {
        "export_balance" : "1",
        "commodities" : "2",
        "regulatory_authority" : "7",
        "country_chart" : None,
        "top_eccn_by_value" : "10", 
        "top_eccn_by_count" : "11",
        "export_license" : "12, 13 and 14"
    },
    "2021" : {
        "export_balance" : "1 and 2",
        "commodities" : "2 or 3",
        "regulatory_authority" : "3 or 4",
        "country_chart" : "3 or 4",
        "top_eccn_by_value" : "6 or 7", 
        "top_eccn_by_count" : "7 or 8",
        "export_license" : "8 and 9"
    },
    "2021_world" : {
        "export_balance" : "3",
        "commodities" : "4",
        "regulatory_authority" : "7",
        "country_chart" : None,
        "top_eccn_by_value" : "10", 
        "top_eccn_by_count" : "11",
        "export_license" : "12, 13 and 14"
    },
    "2022" : {
        "export_balance" : "3",
        "commodities" : "4",
        "regulatory_authority" : "5",
        "country_chart" : "5",
        "top_eccn_by_value" : "8", 
        "top_eccn_by_count" : "9",
        "export_license" : "10, 11 and 12"
    },
    "2022_world" : {
        "export_balance" : "3",
        "commodities" : "4",
        "regulatory_authority" : "5",
        "country_chart" : None,
        "top_eccn_by_value" : "8", 
        "top_eccn_by_count" : "9",
        "export_license" : "10, 11 and 12"
    }

}