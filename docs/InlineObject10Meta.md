# InlineObject10Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name with extension. Auto-generated if not provided in request. | [optional] 
**display_name** | **str** | File name without extension. | [optional] 
**encoding** | **str** | Encoding of the response data. | [optional] 
**content_type** | **str** | Image content type. | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object10_meta import InlineObject10Meta

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10Meta from a JSON string
inline_object10_meta_instance = InlineObject10Meta.from_json(json)
# print the JSON string representation of the object
print(InlineObject10Meta.to_json())

# convert the object into a dict
inline_object10_meta_dict = inline_object10_meta_instance.to_dict()
# create an instance of InlineObject10Meta from a dict
inline_object10_meta_from_dict = InlineObject10Meta.from_dict(inline_object10_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


