# TemplateDefinitionNewPagesInnerLayout

Defines page specific layout which can differ from the main template layout (e.g page format, margins). A page without one may have an empty array, as older templates store it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pdf_generator_api_client.models.template_definition_new_pages_inner_layout import TemplateDefinitionNewPagesInnerLayout

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewPagesInnerLayout from a JSON string
template_definition_new_pages_inner_layout_instance = TemplateDefinitionNewPagesInnerLayout.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewPagesInnerLayout.to_json())

# convert the object into a dict
template_definition_new_pages_inner_layout_dict = template_definition_new_pages_inner_layout_instance.to_dict()
# create an instance of TemplateDefinitionNewPagesInnerLayout from a dict
template_definition_new_pages_inner_layout_from_dict = TemplateDefinitionNewPagesInnerLayout.from_dict(template_definition_new_pages_inner_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


