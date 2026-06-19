# InlineObjectMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **str** | Document encoding | [optional] 
**content_type** | **str** | Document content type. | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object_meta import InlineObjectMeta

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObjectMeta from a JSON string
inline_object_meta_instance = InlineObjectMeta.from_json(json)
# print the JSON string representation of the object
print(InlineObjectMeta.to_json())

# convert the object into a dict
inline_object_meta_dict = inline_object_meta_instance.to_dict()
# create an instance of InlineObjectMeta from a dict
inline_object_meta_from_dict = InlineObjectMeta.from_dict(inline_object_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


