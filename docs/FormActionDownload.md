# FormActionDownload

Key-value pair of action configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_document** | **bool** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_action_download import FormActionDownload

# TODO update the JSON string below
json = "{}"
# create an instance of FormActionDownload from a JSON string
form_action_download_instance = FormActionDownload.from_json(json)
# print the JSON string representation of the object
print(FormActionDownload.to_json())

# convert the object into a dict
form_action_download_dict = form_action_download_instance.to_dict()
# create an instance of FormActionDownload from a dict
form_action_download_from_dict = FormActionDownload.from_dict(form_action_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


