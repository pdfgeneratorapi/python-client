# InlineObject12Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | UUID of the async job. | 
**status** | **str** | Status of the async job. | 

## Example

```python
from pdf_generator_api_client.models.inline_object12_response import InlineObject12Response

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject12Response from a JSON string
inline_object12_response_instance = InlineObject12Response.from_json(json)
# print the JSON string representation of the object
print(InlineObject12Response.to_json())

# convert the object into a dict
inline_object12_response_dict = inline_object12_response_instance.to_dict()
# create an instance of InlineObject12Response from a dict
inline_object12_response_from_dict = InlineObject12Response.from_dict(inline_object12_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


