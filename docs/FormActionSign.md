# FormActionSign

Asks the person who submitted the form to sign the generated document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_document** | **bool** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_action_sign import FormActionSign

# TODO update the JSON string below
json = "{}"
# create an instance of FormActionSign from a JSON string
form_action_sign_instance = FormActionSign.from_json(json)
# print the JSON string representation of the object
print(FormActionSign.to_json())

# convert the object into a dict
form_action_sign_dict = form_action_sign_instance.to_dict()
# create an instance of FormActionSign from a dict
form_action_sign_from_dict = FormActionSign.from_dict(form_action_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


