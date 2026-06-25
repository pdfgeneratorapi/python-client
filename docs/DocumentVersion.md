# DocumentVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** | Version identifier (hash). | [optional] 
**name** | **str** | Version name. | [optional] 
**person** | [**DocumentUser**](DocumentUser.md) |  | [optional] 
**created_at** | **str** | Creation timestamp (Y-m-d H:i:s). | [optional] 

## Example

```python
from pdf_generator_api_client.models.document_version import DocumentVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVersion from a JSON string
document_version_instance = DocumentVersion.from_json(json)
# print the JSON string representation of the object
print(DocumentVersion.to_json())

# convert the object into a dict
document_version_dict = document_version_instance.to_dict()
# create an instance of DocumentVersion from a dict
document_version_from_dict = DocumentVersion.from_dict(document_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


