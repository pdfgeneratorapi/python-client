# TemplateDefinitionNewLayoutRepeatLayout

Defines page size if layout is repeated on the page e.g sheet labels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Defines template page size | [optional] 
**width** | **float** | Page width in units | [optional] 
**height** | **float** | Page height in units | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition_new_layout_repeat_layout import TemplateDefinitionNewLayoutRepeatLayout

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewLayoutRepeatLayout from a JSON string
template_definition_new_layout_repeat_layout_instance = TemplateDefinitionNewLayoutRepeatLayout.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewLayoutRepeatLayout.to_json())

# convert the object into a dict
template_definition_new_layout_repeat_layout_dict = template_definition_new_layout_repeat_layout_instance.to_dict()
# create an instance of TemplateDefinitionNewLayoutRepeatLayout from a dict
template_definition_new_layout_repeat_layout_from_dict = TemplateDefinitionNewLayoutRepeatLayout.from_dict(template_definition_new_layout_repeat_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


