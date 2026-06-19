# InlineObject13


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | UUID of the async job. | [optional] 
**status** | **str** | Status of the async job. | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object13 import InlineObject13

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject13 from a JSON string
inline_object13_instance = InlineObject13.from_json(json)
# print the JSON string representation of the object
print(InlineObject13.to_json())

# convert the object into a dict
inline_object13_dict = inline_object13_instance.to_dict()
# create an instance of InlineObject13 from a dict
inline_object13_from_dict = InlineObject13.from_dict(inline_object13_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


