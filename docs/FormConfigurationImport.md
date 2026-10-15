# FormConfigurationImport

Optional form settings applied to the imported form. Form fields are created from the editable fields of the PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template ID which is connected to the form | [optional] 
**name** | **str** | Form name | [optional] 
**actions** | [**List[FormConfigurationNewActionsInner]**](FormConfigurationNewActionsInner.md) | Array of action configurations. Each action is a separate object with a single key; leave an action out to disable it. | [optional] 
**configuration** | [**FormConfiguration**](FormConfiguration.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_configuration_import import FormConfigurationImport

# TODO update the JSON string below
json = "{}"
# create an instance of FormConfigurationImport from a JSON string
form_configuration_import_instance = FormConfigurationImport.from_json(json)
# print the JSON string representation of the object
print(FormConfigurationImport.to_json())

# convert the object into a dict
form_configuration_import_dict = form_configuration_import_instance.to_dict()
# create an instance of FormConfigurationImport from a dict
form_configuration_import_from_dict = FormConfigurationImport.from_dict(form_configuration_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


