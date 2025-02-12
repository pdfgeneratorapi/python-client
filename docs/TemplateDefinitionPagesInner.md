# TemplateDefinitionPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Page width in units | [optional] 
**height** | **float** | Page height in units | [optional] 
**margins** | [**TemplateDefinitionNewPagesInnerMargins**](TemplateDefinitionNewPagesInnerMargins.md) |  | [optional] 
**components** | **List[object]** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition_pages_inner import TemplateDefinitionPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionPagesInner from a JSON string
template_definition_pages_inner_instance = TemplateDefinitionPagesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionPagesInner.to_json())

# convert the object into a dict
template_definition_pages_inner_dict = template_definition_pages_inner_instance.to_dict()
# create an instance of TemplateDefinitionPagesInner from a dict
template_definition_pages_inner_from_dict = TemplateDefinitionPagesInner.from_dict(template_definition_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


