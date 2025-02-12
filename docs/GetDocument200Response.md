# GetDocument200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Public URL to the document. | [optional] 
**meta** | [**GetDocument200ResponseMeta**](GetDocument200ResponseMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_document200_response import GetDocument200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocument200Response from a JSON string
get_document200_response_instance = GetDocument200Response.from_json(json)
# print the JSON string representation of the object
print(GetDocument200Response.to_json())

# convert the object into a dict
get_document200_response_dict = get_document200_response_instance.to_dict()
# create an instance of GetDocument200Response from a dict
get_document200_response_from_dict = GetDocument200Response.from_dict(get_document200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


