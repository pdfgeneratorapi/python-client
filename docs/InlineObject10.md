# InlineObject10


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **List[str]** | Array of base64 encoded images, one per converted page. | [optional] 
**meta** | [**InlineObject10Meta**](InlineObject10Meta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object10 import InlineObject10

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10 from a JSON string
inline_object10_instance = InlineObject10.from_json(json)
# print the JSON string representation of the object
print(InlineObject10.to_json())

# convert the object into a dict
inline_object10_dict = inline_object10_instance.to_dict()
# create an instance of InlineObject10 from a dict
inline_object10_from_dict = InlineObject10.from_dict(inline_object10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


