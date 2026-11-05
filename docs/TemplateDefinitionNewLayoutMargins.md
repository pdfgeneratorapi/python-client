# TemplateDefinitionNewLayoutMargins

Page margins in units, all four sides

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** | Top margin in units | 
**right** | **float** | Right margin in units | 
**bottom** | **float** | Bottom margin in units | 
**left** | **float** | Left margin in units | 

## Example

```python
from pdf_generator_api_client.models.template_definition_new_layout_margins import TemplateDefinitionNewLayoutMargins

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewLayoutMargins from a JSON string
template_definition_new_layout_margins_instance = TemplateDefinitionNewLayoutMargins.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewLayoutMargins.to_json())

# convert the object into a dict
template_definition_new_layout_margins_dict = template_definition_new_layout_margins_instance.to_dict()
# create an instance of TemplateDefinitionNewLayoutMargins from a dict
template_definition_new_layout_margins_from_dict = TemplateDefinitionNewLayoutMargins.from_dict(template_definition_new_layout_margins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


