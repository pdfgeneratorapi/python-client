# ValidateTemplate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ValidateTemplate200ResponseResponse**](ValidateTemplate200ResponseResponse.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.validate_template200_response import ValidateTemplate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTemplate200Response from a JSON string
validate_template200_response_instance = ValidateTemplate200Response.from_json(json)
# print the JSON string representation of the object
print(ValidateTemplate200Response.to_json())

# convert the object into a dict
validate_template200_response_dict = validate_template200_response_instance.to_dict()
# create an instance of ValidateTemplate200Response from a dict
validate_template200_response_from_dict = ValidateTemplate200Response.from_dict(validate_template200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


