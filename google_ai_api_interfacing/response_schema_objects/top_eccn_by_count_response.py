import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

top_eccn_by_count_query = "Extract the top ten ECCNs by count and their descriptions exported under a license, with a license exception, or under NLR with ECCN reported from page {page} from the {country} report. Report the ECCNs in descending order."

top_eccn_by_count_schema = content.Schema(
    type=content.Type.OBJECT,
    required=[
        "country",
        "report_year",
        "top_eccn_count_licensed_eccn_codes",
        "top_eccn_count_exceptions_eccn_codes",
        "top_eccn_count_nlr_with_eccn_eccn_codes",
        "top_eccn_count_licensed_descriptions",
        "top_eccn_count_exceptions_descriptions",
        "top_eccn_count_nlr_with_eccn_descriptions"
    ],
    properties={
        "country": content.Schema(
            type=content.Type.STRING
        ),
        "report_year": content.Schema(
            type=content.Type.NUMBER
        ),
        "top_eccn_count_licensed_eccn_codes": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        ),
        "top_eccn_count_exceptions_eccn_codes": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        ),
        "top_eccn_count_nlr_with_eccn_eccn_codes": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        ),
        "top_eccn_count_licensed_descriptions": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        ),
        "top_eccn_count_exceptions_descriptions": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        ),
        "top_eccn_count_nlr_with_eccn_descriptions": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.STRING
            )
        )
    }
)
