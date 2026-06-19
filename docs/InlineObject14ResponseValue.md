# InlineObject14ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique field identifier | [optional] 
**type** | **str** | Field type | [optional] 
**name** | **str** | Field name | [optional] 
**value** | [**InlineObject14ResponseValueValue**](InlineObject14ResponseValueValue.md) |  | [optional] 
**locked** | **bool** | Whether the field is locked | [optional] 
**pages** | **List[int]** | Pages where the field appears | [optional] 
**default** | [**InlineObject14ResponseValueDefault**](InlineObject14ResponseValueDefault.md) |  | [optional] 
**defaults** | **List[str]** | Default values for multi-select fields | [optional] 
**values** | **List[str]** | Selected values for multi-select fields | [optional] 
**options** | **List[str]** | Available options for select fields | [optional] 
**format** | **str** | Field format (for date fields) | [optional] 
**maxlen** | **int** | Maximum field length | [optional] 
**multiline** | **bool** | Whether text field is multiline | [optional] 
**editable** | **bool** | Whether combo box is editable | [optional] 
**multi** | **bool** | Whether list box allows multiple selections | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object14_response_value import InlineObject14ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject14ResponseValue from a JSON string
inline_object14_response_value_instance = InlineObject14ResponseValue.from_json(json)
# print the JSON string representation of the object
print(InlineObject14ResponseValue.to_json())

# convert the object into a dict
inline_object14_response_value_dict = inline_object14_response_value_instance.to_dict()
# create an instance of InlineObject14ResponseValue from a dict
inline_object14_response_value_from_dict = InlineObject14ResponseValue.from_dict(inline_object14_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


