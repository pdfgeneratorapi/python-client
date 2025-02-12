# OpenEditorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OpenEditorRequestData**](OpenEditorRequestData.md) |  | [optional] 
**language** | **str** | Specify the editor UI language. Defaults to organization editor language. | [optional] 

## Example

```python
from pdf_generator_api_client.models.open_editor_request import OpenEditorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenEditorRequest from a JSON string
open_editor_request_instance = OpenEditorRequest.from_json(json)
# print the JSON string representation of the object
print(OpenEditorRequest.to_json())

# convert the object into a dict
open_editor_request_dict = open_editor_request_instance.to_dict()
# create an instance of OpenEditorRequest from a dict
open_editor_request_from_dict = OpenEditorRequest.from_dict(open_editor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


