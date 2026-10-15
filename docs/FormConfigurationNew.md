# FormConfigurationNew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template ID which is connected to the form | [optional] 
**name** | **str** | Form name | 
**actions** | [**List[FormConfigurationNewActionsInner]**](FormConfigurationNewActionsInner.md) | Array of action configurations. Each action is a separate object with a single key; leave an action out to disable it. | 
**fields** | [**List[FormField]**](FormField.md) | Input fields shown on the form, in display order. Field names must be unique within the form. | 
**configuration** | [**FormConfiguration**](FormConfiguration.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_configuration_new import FormConfigurationNew

# TODO update the JSON string below
json = "{}"
# create an instance of FormConfigurationNew from a JSON string
form_configuration_new_instance = FormConfigurationNew.from_json(json)
# print the JSON string representation of the object
print(FormConfigurationNew.to_json())

# convert the object into a dict
form_configuration_new_dict = form_configuration_new_instance.to_dict()
# create an instance of FormConfigurationNew from a dict
form_configuration_new_from_dict = FormConfigurationNew.from_dict(form_configuration_new_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


