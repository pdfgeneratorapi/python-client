# FormConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**template_id** | **int** | Template ID which is connected to the form | [optional] 
**name** | **str** | Form name | [optional] 
**actions** | [**List[FormConfigurationNewActionsInner]**](FormConfigurationNewActionsInner.md) | Array of action configurations | [optional] 
**fields** | [**List[FormFieldsInner]**](FormFieldsInner.md) | A list of form field objects | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_configuration import FormConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of FormConfiguration from a JSON string
form_configuration_instance = FormConfiguration.from_json(json)
# print the JSON string representation of the object
print(FormConfiguration.to_json())

# convert the object into a dict
form_configuration_dict = form_configuration_instance.to_dict()
# create an instance of FormConfiguration from a dict
form_configuration_from_dict = FormConfiguration.from_dict(form_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


