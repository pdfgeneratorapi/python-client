# DocumentAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action performed on the document. | [optional] 
**person** | [**DocumentUser**](DocumentUser.md) |  | [optional] 
**created_at** | **str** | Action timestamp (Y-m-d H:i:s). | [optional] 

## Example

```python
from pdf_generator_api_client.models.document_action import DocumentAction

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAction from a JSON string
document_action_instance = DocumentAction.from_json(json)
# print the JSON string representation of the object
print(DocumentAction.to_json())

# convert the object into a dict
document_action_dict = document_action_instance.to_dict()
# create an instance of DocumentAction from a dict
document_action_from_dict = DocumentAction.from_dict(document_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


