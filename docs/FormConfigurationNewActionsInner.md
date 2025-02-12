# FormConfigurationNewActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_document** | **bool** |  | [optional] 
**download_document** | **bool** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_configuration_new_actions_inner import FormConfigurationNewActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormConfigurationNewActionsInner from a JSON string
form_configuration_new_actions_inner_instance = FormConfigurationNewActionsInner.from_json(json)
# print the JSON string representation of the object
print(FormConfigurationNewActionsInner.to_json())

# convert the object into a dict
form_configuration_new_actions_inner_dict = form_configuration_new_actions_inner_instance.to_dict()
# create an instance of FormConfigurationNewActionsInner from a dict
form_configuration_new_actions_inner_from_dict = FormConfigurationNewActionsInner.from_dict(form_configuration_new_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


