import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

commodities_query = "Get the types of commodities and export and import percentages, from page {page} of the {country} report for the report year."

commodities_schema = content.Schema(
  type = content.Type.OBJECT,
  required =  [
    "country",
    "report_year",
    "commodities_traded_type",
    "commodities_traded_import_percentage",
    "commodities_traded_export_percentage"],
  properties =  {
    "country": content.Schema(
       type = content.Type.STRING
    ),
    "report_year": content.Schema(
       type = content.Type.NUMBER
    ),
    "commodities_traded_type": content.Schema(
      type = content.Type.ARRAY,
      items= content.Schema(
         type = content.Type.STRING
      )
    ),
    "commodities_traded_import_percentage": content.Schema(
      type = content.Type.ARRAY,
      items= content.Schema(
         type = content.Type.NUMBER
      )
    ),
    "commodities_traded_export_percentage": content.Schema(
      type = content.Type.ARRAY,
      items= content.Schema(
         type = content.Type.NUMBER
      )
    )
  },
)
