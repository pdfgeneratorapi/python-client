# TemplateDefinitionNewDataSettings

Defines filter and sort option for root data set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_by** | **List[object]** |  | [optional] 
**filter_by** | **List[object]** |  | [optional] 
**transform** | **List[object]** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_definition_new_data_settings import TemplateDefinitionNewDataSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefinitionNewDataSettings from a JSON string
template_definition_new_data_settings_instance = TemplateDefinitionNewDataSettings.from_json(json)
# print the JSON string representation of the object
print(TemplateDefinitionNewDataSettings.to_json())

# convert the object into a dict
template_definition_new_data_settings_dict = template_definition_new_data_settings_instance.to_dict()
# create an instance of TemplateDefinitionNewDataSettings from a dict
template_definition_new_data_settings_from_dict = TemplateDefinitionNewDataSettings.from_dict(template_definition_new_data_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


