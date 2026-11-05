# TemplateDefinitionUpdate

The template configuration to change. Each top-level field sent replaces the stored one, and a field left out, the name included, keeps its stored value. Use the Get schema endpoint to see the detailed payload structure.

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

## Example

```python
from pdf_generator_api_client.models.template_definition_update import TemplateDefinitionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionUpdate from a JSON string
template_definition_update_instance = TemplateDefinitionUpdate.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionUpdate.to_json())

# convert the object into a dict
template_definition_update_dict = template_definition_update_instance.to_dict()
# create an instance of TemplateDefinitionUpdate from a dict
template_definition_update_from_dict = TemplateDefinitionUpdate.from_dict(template_definition_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


