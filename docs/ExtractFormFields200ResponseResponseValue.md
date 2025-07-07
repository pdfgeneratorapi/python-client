# ExtractFormFields200ResponseResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique field identifier | [optional] 
**type** | **str** | Field type | [optional] 
**name** | **str** | Field name | [optional] 
**value** | [**ExtractFormFields200ResponseResponseValueValue**](ExtractFormFields200ResponseResponseValueValue.md) |  | [optional] 
**locked** | **bool** | Whether the field is locked | [optional] 
**pages** | **List[int]** | Pages where the field appears | [optional] 
**default** | [**ExtractFormFields200ResponseResponseValueDefault**](ExtractFormFields200ResponseResponseValueDefault.md) |  | [optional] 
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
from pdf_generator_api_client.models.extract_form_fields200_response_response_value import ExtractFormFields200ResponseResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractFormFields200ResponseResponseValue from a JSON string
extract_form_fields200_response_response_value_instance = ExtractFormFields200ResponseResponseValue.from_json(json)
# print the JSON string representation of the object
print(ExtractFormFields200ResponseResponseValue.to_json())

# convert the object into a dict
extract_form_fields200_response_response_value_dict = extract_form_fields200_response_response_value_instance.to_dict()
# create an instance of ExtractFormFields200ResponseResponseValue from a dict
extract_form_fields200_response_response_value_from_dict = ExtractFormFields200ResponseResponseValue.from_dict(extract_form_fields200_response_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


