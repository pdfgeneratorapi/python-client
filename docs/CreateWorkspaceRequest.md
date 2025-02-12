# CreateWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | A unique identifier of the workspace. Make sure that you can generate the same identifier for your user. | [optional] 

## Example

```python
from pdf_generator_api_client.models.create_workspace_request import CreateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceRequest from a JSON string
create_workspace_request_instance = CreateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceRequest.to_json())

# convert the object into a dict
create_workspace_request_dict = create_workspace_request_instance.to_dict()
# create an instance of CreateWorkspaceRequest from a dict
create_workspace_request_from_dict = CreateWorkspaceRequest.from_dict(create_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


