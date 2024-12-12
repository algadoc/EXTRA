import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

export_license_query = "Extract information regarding the number and value of requested export licenses from page {page} from the {country} report. Report the values for all available years and the dollar amounts in millions of dollars. The deemed export application is only available for the report year."

export_license_schema = content.Schema(
    type=content.Type.OBJECT,
    required=[
        "country",
        "report_year",
        "export_applications_available_years",
        "export_applications_approved",
        "export_applications_approved_value",
        "export_applications_rwa",
        "export_applications_rwa_value",
        "export_applications_denied",
        "export_applications_denied_value",
        "export_applications_average_processing_time",
        "export_applications_deeemed_export_license_approved",
        "export_applications_deeemed_export_license_rwa",
        "export_applications_deeemed_export_license_denied"
    ],
    properties={
        "country": content.Schema(
            type=content.Type.STRING
        ),
        "report_year": content.Schema(
            type=content.Type.NUMBER
        ),
        "export_applications_available_years": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_approved": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_approved_value": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_rwa": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_rwa_value": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_denied": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_denied_value": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_average_processing_time": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_deeemed_export_license_approved": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_deeemed_export_license_rwa": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        ),
        "export_applications_deeemed_export_license_denied": content.Schema(
            type=content.Type.ARRAY,
            items=content.Schema(
                type=content.Type.NUMBER
            )
        )
    }
)
