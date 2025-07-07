# FormFieldsBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF document in base64 encoded string format | 

## Example

```python
from pdf_generator_api_client.models.form_fields_base64 import FormFieldsBase64

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldsBase64 from a JSON string
form_fields_base64_instance = FormFieldsBase64.from_json(json)
# print the JSON string representation of the object
print(FormFieldsBase64.to_json())

# convert the object into a dict
form_fields_base64_dict = form_fields_base64_instance.to_dict()
# create an instance of FormFieldsBase64 from a dict
form_fields_base64_from_dict = FormFieldsBase64.from_dict(form_fields_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


