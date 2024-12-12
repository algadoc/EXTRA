import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

export_balance_query = "Get the total trade, imports and exports, from page {page} of the {country} report for the available years. Report the year and values of exports and imports in billions of dollars."

export_balance_schema = content.Schema(
    type=content.Type.OBJECT,
    required=[
        "year",
        "export_value",
        "import_value",
        "country",
        "report_year"
    ],
    properties={
        "year": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_value": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "import_value": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "country": content.Schema(
            type=content.Type.STRING
        ),
        "report_year": content.Schema(
            type=content.Type.NUMBER
        )
    }
)
