# DocumentUser

The user who created the version or performed the action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id_code** | **str** | National identification code, when provided. | [optional] 
**ip** | **str** | IP address captured when the action was performed. | [optional] 

## Example

```python
from pdf_generator_api_client.models.document_user import DocumentUser

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUser from a JSON string
document_user_instance = DocumentUser.from_json(json)
# print the JSON string representation of the object
print(DocumentUser.to_json())

# convert the object into a dict
document_user_dict = document_user_instance.to_dict()
# create an instance of DocumentUser from a dict
document_user_from_dict = DocumentUser.from_dict(document_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


