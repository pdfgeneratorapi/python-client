# MakeAccessibleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**options** | [**List[AccessibilityOption]**](AccessibilityOption.md) | Accessibility processing options | [optional] 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**metadata** | [**MetadataParam**](MetadataParam.md) |  | [optional] 
**file_base64** | **str** | PDF document in base64 encoded string format | 

## Example

```python
from pdf_generator_api_client.models.make_accessible_request import MakeAccessibleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MakeAccessibleRequest from a JSON string
make_accessible_request_instance = MakeAccessibleRequest.from_json(json)
# print the JSON string representation of the object
print(MakeAccessibleRequest.to_json())

# convert the object into a dict
make_accessible_request_dict = make_accessible_request_instance.to_dict()
# create an instance of MakeAccessibleRequest from a dict
make_accessible_request_from_dict = MakeAccessibleRequest.from_dict(make_accessible_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


