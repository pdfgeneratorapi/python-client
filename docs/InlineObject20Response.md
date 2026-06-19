# InlineObject20Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique job id which is also added to the callback request as header PDF-API-Job-Id | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object20_response import InlineObject20Response

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject20Response from a JSON string
inline_object20_response_instance = InlineObject20Response.from_json(json)
# print the JSON string representation of the object
print(InlineObject20Response.to_json())

# convert the object into a dict
inline_object20_response_dict = inline_object20_response_instance.to_dict()
# create an instance of InlineObject20Response from a dict
inline_object20_response_from_dict = InlineObject20Response.from_dict(inline_object20_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


