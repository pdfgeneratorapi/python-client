# TemplateDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**name** | **str** | Template name | [optional] 
**tags** | **List[str]** | A list of tags assigned to a template | [optional] 
**is_draft** | **bool** | Indicates if the template is a draft or published. | [optional] 
**layout** | [**TemplateDefinitionNewLayout**](TemplateDefinitionNewLayout.md) |  | [optional] 
**pages** | [**List[TemplateDefinitionNewPagesInner]**](TemplateDefinitionNewPagesInner.md) | Defines page or label size, margins and components on page or label | [optional] 
**data_settings** | [**TemplateDefinitionDataSettings**](TemplateDefinitionDataSettings.md) |  | [optional] 
**editor** | [**TemplateDefinitionEditor**](TemplateDefinitionEditor.md) |  | [optional] 

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


