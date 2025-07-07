# FillFormFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**data** | **object** | Form field data to fill in the PDF | 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**name** | **str** | Name for the PDF file | [optional] 
**file_base64** | **str** | PDF document in base64 encoded string format | 

## Example

```python
from pdf_generator_api_client.models.fill_form_fields_request import FillFormFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FillFormFieldsRequest from a JSON string
fill_form_fields_request_instance = FillFormFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(FillFormFieldsRequest.to_json())

# convert the object into a dict
fill_form_fields_request_dict = fill_form_fields_request_instance.to_dict()
# create an instance of FillFormFieldsRequest from a dict
fill_form_fields_request_from_dict = FillFormFieldsRequest.from_dict(fill_form_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


