# ExtractFormFields200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Dict[str, ExtractFormFields200ResponseResponseValue]**](ExtractFormFields200ResponseResponseValue.md) | Form fields extracted from the PDF document | [optional] 

## Example

```python
from pdf_generator_api_client.models.extract_form_fields200_response import ExtractFormFields200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractFormFields200Response from a JSON string
extract_form_fields200_response_instance = ExtractFormFields200Response.from_json(json)
# print the JSON string representation of the object
print(ExtractFormFields200Response.to_json())

# convert the object into a dict
extract_form_fields200_response_dict = extract_form_fields200_response_instance.to_dict()
# create an instance of ExtractFormFields200Response from a dict
extract_form_fields200_response_from_dict = ExtractFormFields200Response.from_dict(extract_form_fields200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


