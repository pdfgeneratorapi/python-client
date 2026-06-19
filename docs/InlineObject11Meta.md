# InlineObject11Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name. This value is automatically generated if name attribute is not defined in request. | [optional] 
**display_name** | **str** | Document name without the file extension. | [optional] 
**encoding** | **str** | Document encoding | [optional] 
**content_type** | **str** | Document content type. | [optional] 
**public_id** | **str** | Document public id | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object11_meta import InlineObject11Meta

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject11Meta from a JSON string
inline_object11_meta_instance = InlineObject11Meta.from_json(json)
# print the JSON string representation of the object
print(InlineObject11Meta.to_json())

# convert the object into a dict
inline_object11_meta_dict = inline_object11_meta_instance.to_dict()
# create an instance of InlineObject11Meta from a dict
inline_object11_meta_from_dict = InlineObject11Meta.from_dict(inline_object11_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


