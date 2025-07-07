# ValidateTemplate200ResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | True if template configuration was valid | [optional] [default to True]

## Example

```python
from pdf_generator_api_client.models.validate_template200_response_response import ValidateTemplate200ResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTemplate200ResponseResponse from a JSON string
validate_template200_response_response_instance = ValidateTemplate200ResponseResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateTemplate200ResponseResponse.to_json())

# convert the object into a dict
validate_template200_response_response_dict = validate_template200_response_response_instance.to_dict()
# create an instance of ValidateTemplate200ResponseResponse from a dict
validate_template200_response_response_from_dict = ValidateTemplate200ResponseResponse.from_dict(validate_template200_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


