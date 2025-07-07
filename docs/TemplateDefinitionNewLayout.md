# TemplateDefinitionNewLayout

Defines template layout (e.g page format, margins).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Defines template page size | [optional] 
**width** | **float** | Page width in units | [optional] 
**height** | **float** | Page height in units | [optional] 
**unit** | **str** | Measure unit | [optional] 
**orientation** | **str** | Page orientation | [optional] 
**rotation** | **int** | Page rotation in degrees | [optional] 
**margins** | [**TemplateDefinitionNewLayoutMargins**](TemplateDefinitionNewLayoutMargins.md) |  | [optional] 
**repeat_layout** | [**TemplateDefinitionNewLayoutRepeatLayout**](TemplateDefinitionNewLayoutRepeatLayout.md) |  | [optional] 
**empty_labels** | **int** | Defines how many pages or labels should be empty | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition_new_layout import TemplateDefinitionNewLayout

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewLayout from a JSON string
template_definition_new_layout_instance = TemplateDefinitionNewLayout.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewLayout.to_json())

# convert the object into a dict
template_definition_new_layout_dict = template_definition_new_layout_instance.to_dict()
# create an instance of TemplateDefinitionNewLayout from a dict
template_definition_new_layout_from_dict = TemplateDefinitionNewLayout.from_dict(template_definition_new_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


