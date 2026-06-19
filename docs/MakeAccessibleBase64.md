# MakeAccessibleBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF document in base64 encoded string format | 
**options** | [**List[AccessibilityOption]**](AccessibilityOption.md) | Accessibility processing options | [optional] 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**metadata** | [**MetadataParam**](MetadataParam.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.make_accessible_base64 import MakeAccessibleBase64

# TODO update the JSON string below
json = "{}"
# create an instance of MakeAccessibleBase64 from a JSON string
make_accessible_base64_instance = MakeAccessibleBase64.from_json(json)
# print the JSON string representation of the object
print(MakeAccessibleBase64.to_json())

# convert the object into a dict
make_accessible_base64_dict = make_accessible_base64_instance.to_dict()
# create an instance of MakeAccessibleBase64 from a dict
make_accessible_base64_from_dict = MakeAccessibleBase64.from_dict(make_accessible_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


