# OpenEditorRequestData

Data used to generate the document. This can be an object or array of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pdf_generator_api_client.models.open_editor_request_data import OpenEditorRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of OpenEditorRequestData from a JSON string
open_editor_request_data_instance = OpenEditorRequestData.from_json(json)
# print the JSON string representation of the object
print(OpenEditorRequestData.to_json())

# convert the object into a dict
open_editor_request_data_dict = open_editor_request_data_instance.to_dict()
# create an instance of OpenEditorRequestData from a dict
open_editor_request_data_from_dict = OpenEditorRequestData.from_dict(open_editor_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


