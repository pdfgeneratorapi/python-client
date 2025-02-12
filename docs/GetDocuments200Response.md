# GetDocuments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[Document]**](Document.md) |  | [optional] 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_documents200_response import GetDocuments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocuments200Response from a JSON string
get_documents200_response_instance = GetDocuments200Response.from_json(json)
# print the JSON string representation of the object
print(GetDocuments200Response.to_json())

# convert the object into a dict
get_documents200_response_dict = get_documents200_response_instance.to_dict()
# create an instance of GetDocuments200Response from a dict
get_documents200_response_from_dict = GetDocuments200Response.from_dict(get_documents200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


