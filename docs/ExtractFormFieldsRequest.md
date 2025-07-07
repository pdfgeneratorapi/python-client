# ExtractFormFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**file_base64** | **str** | PDF document in base64 encoded string format | 

## Example

```python
from pdf_generator_api_client.models.extract_form_fields_request import ExtractFormFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractFormFieldsRequest from a JSON string
extract_form_fields_request_instance = ExtractFormFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(ExtractFormFieldsRequest.to_json())

# convert the object into a dict
extract_form_fields_request_dict = extract_form_fields_request_instance.to_dict()
# create an instance of ExtractFormFieldsRequest from a dict
extract_form_fields_request_from_dict = ExtractFormFieldsRequest.from_dict(extract_form_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


