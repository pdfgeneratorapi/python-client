# FormFillBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF document in base64 encoded string format | 
**data** | **object** | Form field data to fill in the PDF | 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**name** | **str** | Name for the PDF file | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_fill_base64 import FormFillBase64

# TODO update the JSON string below
json = "{}"
# create an instance of FormFillBase64 from a JSON string
form_fill_base64_instance = FormFillBase64.from_json(json)
# print the JSON string representation of the object
print(FormFillBase64.to_json())

# convert the object into a dict
form_fill_base64_dict = form_fill_base64_instance.to_dict()
# create an instance of FormFillBase64 from a dict
form_fill_base64_from_dict = FormFillBase64.from_dict(form_fill_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


