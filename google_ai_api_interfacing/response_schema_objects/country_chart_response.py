import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

country_chart_query = "Look at the table labeled Reasons For Control on the {country} report, on page {page}. Return the cells marked with an X on the table in the reason_for_control field. Use their abbreviated name and number."

country_chart_schema = content.Schema(
    type=content.Type.OBJECT,
    required=[
        "country",
        "report_year",
        "reasons_for_control"
    ],
    properties={
        "country": content.Schema(
            type=content.Type.STRING
        ),
        "report_year": content.Schema(
            type=content.Type.NUMBER
        ),
        "reasons_for_control": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        )
    }
)
