# InlineObject14


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Dict[str, InlineObject14ResponseValue]**](InlineObject14ResponseValue.md) | Form fields extracted from the PDF document | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object14 import InlineObject14

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject14 from a JSON string
inline_object14_instance = InlineObject14.from_json(json)
# print the JSON string representation of the object
print(InlineObject14.to_json())

# convert the object into a dict
inline_object14_dict = inline_object14_instance.to_dict()
# create an instance of InlineObject14 from a dict
inline_object14_from_dict = InlineObject14.from_dict(inline_object14_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


