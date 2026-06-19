# MakeAccessibleUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**options** | [**List[AccessibilityOption]**](AccessibilityOption.md) | Accessibility processing options | [optional] 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**metadata** | [**MetadataParam**](MetadataParam.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.make_accessible_url import MakeAccessibleUrl

# TODO update the JSON string below
json = "{}"
# create an instance of MakeAccessibleUrl from a JSON string
make_accessible_url_instance = MakeAccessibleUrl.from_json(json)
# print the JSON string representation of the object
print(MakeAccessibleUrl.to_json())

# convert the object into a dict
make_accessible_url_dict = make_accessible_url_instance.to_dict()
# create an instance of MakeAccessibleUrl from a dict
make_accessible_url_from_dict = MakeAccessibleUrl.from_dict(make_accessible_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


