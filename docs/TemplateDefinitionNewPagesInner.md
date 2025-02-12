# TemplateDefinitionNewPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Page width in units | [optional] 
**height** | **float** | Page height in units | [optional] 
**margins** | [**TemplateDefinitionNewPagesInnerMargins**](TemplateDefinitionNewPagesInnerMargins.md) |  | [optional] 
**border** | **bool** |  | [optional] [default to False]
**components** | **List[object]** |  | [optional] 
**layout** | **object** | Defines page specific layout which can differ from the main template layout (e.g page format, margins). | [optional] 
**conditional_formats** | **List[object]** |  | [optional] 
**background_image** | **str** | Defines background image for the page. | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition_new_pages_inner import TemplateDefinitionNewPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewPagesInner from a JSON string
template_definition_new_pages_inner_instance = TemplateDefinitionNewPagesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewPagesInner.to_json())

# convert the object into a dict
template_definition_new_pages_inner_dict = template_definition_new_pages_inner_instance.to_dict()
# create an instance of TemplateDefinitionNewPagesInner from a dict
template_definition_new_pages_inner_from_dict = TemplateDefinitionNewPagesInner.from_dict(template_definition_new_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


