# InlineObject12


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Base64 encoded document if the output&#x3D;base64 is used or URL to the document when the output&#x3D;url is used. | [optional] 
**meta** | [**InlineObject12Meta**](InlineObject12Meta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object12 import InlineObject12

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject12 from a JSON string
inline_object12_instance = InlineObject12.from_json(json)
# print the JSON string representation of the object
print(InlineObject12.to_json())

# convert the object into a dict
inline_object12_dict = inline_object12_instance.to_dict()
# create an instance of InlineObject12 from a dict
inline_object12_from_dict = InlineObject12.from_dict(inline_object12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


