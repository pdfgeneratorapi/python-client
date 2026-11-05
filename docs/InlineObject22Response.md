# InlineObject22Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique job id which is also added to the callback request as header PDF-API-Job-Id | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object22_response import InlineObject22Response

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject22Response from a JSON string
inline_object22_response_instance = InlineObject22Response.from_json(json)
# print the JSON string representation of the object
print(InlineObject22Response.to_json())

# convert the object into a dict
inline_object22_response_dict = inline_object22_response_instance.to_dict()
# create an instance of InlineObject22Response from a dict
inline_object22_response_from_dict = InlineObject22Response.from_dict(inline_object22_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


