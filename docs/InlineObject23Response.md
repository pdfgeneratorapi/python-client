# InlineObject23Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique job id which is also added to the callback request as header PDF-API-Job-Id | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object23_response import InlineObject23Response

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject23Response from a JSON string
inline_object23_response_instance = InlineObject23Response.from_json(json)
# print the JSON string representation of the object
print(InlineObject23Response.to_json())

# convert the object into a dict
inline_object23_response_dict = inline_object23_response_instance.to_dict()
# create an instance of InlineObject23Response from a dict
inline_object23_response_from_dict = InlineObject23Response.from_dict(inline_object23_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


