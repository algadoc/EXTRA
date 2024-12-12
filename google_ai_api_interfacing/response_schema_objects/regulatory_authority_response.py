import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

regulatory_authority_query = "Extract the value of exports in millions of dollars for each regulatory authority category for all available years on page {page} from the {country} report."

regulatory_authority_schema = content.Schema(
    type=content.Type.OBJECT,
    required=[
        "country",
        "report_year",
        "regulatory_authority_years",
        "regulatory_authority_department_of_state_values",
        "regulatory_authority_other_usg_agencies_values",
        "regulatory_authority_department_of_commerce_values",
        "regulatory_authority_bis_license",
        "regulatory_authority_bis_license_exception",
        "regulatory_authority_nlr_reporting_eccn",
        "regulatory_authority_nlr_reporting_ear99",
        "regulatory_authority_nlr_not_reporting_eccn",
        "regulatory_authority_600_series"
    ],
    properties={
        "country": content.Schema(
            type=content.Type.STRING
        ),
        "report_year": content.Schema(
            type=content.Type.NUMBER
        ),
        "regulatory_authority_years": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_department_of_state_values": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_other_usg_agencies_values": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_department_of_commerce_values": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_bis_license": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_bis_license_exception": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_nlr_reporting_eccn": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_nlr_reporting_ear99": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_nlr_not_reporting_eccn": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "regulatory_authority_600_series": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        )
    }
)
