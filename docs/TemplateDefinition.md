# TemplateDefinition

A template as stored. Its configuration fields are those a new template is sent with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Template name | [optional] 
**tags** | **List[str]** | A list of tags assigned to a template | [optional] 
**is_draft** | **bool** | Indicates if the template is a draft or published. | [optional] 
**layout** | [**TemplateDefinitionNewLayout**](TemplateDefinitionNewLayout.md) |  | [optional] 
**pages** | [**List[TemplateDefinitionNewPagesInner]**](TemplateDefinitionNewPagesInner.md) | Defines page or label size, margins and components on page or label | [optional] 
**data_settings** | [**TemplateDefinitionNewDataSettings**](TemplateDefinitionNewDataSettings.md) |  | [optional] 
**editor** | [**TemplateDefinitionNewEditor**](TemplateDefinitionNewEditor.md) |  | [optional] 
**font_subsetting** | **bool** | If font-subsetting is applied to document when generated | [optional] [default to False]
**barcode_as_image** | **bool** | Defines if barcodes are rendered as raster images instead of vector graphics. | [optional] [default to False]
**id** | **int** | Unique identifier. &#x60;null&#x60; for a template library preview, which is not a template of the workspace. | [optional] 
**improved_html_spacing** | **bool** | Measures HTML text the way it is drawn. New templates have it on; one saved before it existed keeps it off, and the layout it was designed with. | [optional] 
**background_pdf** | **str** | A base64 PDF the pages are drawn on. Set when the template is imported from a PDF. | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition import TemplateDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinition from a JSON string
template_definition_instance = TemplateDefinition.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinition.to_json())

# convert the object into a dict
template_definition_dict = template_definition_instance.to_dict()
# create an instance of TemplateDefinition from a dict
template_definition_from_dict = TemplateDefinition.from_dict(template_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


