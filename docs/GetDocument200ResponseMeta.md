# GetDocument200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name. This value is automatically generated if name attribute is not defined in request. | [optional] 
**display_name** | **str** | Document name without the file extension. | [optional] 
**encoding** | **str** | Document encoding | [optional] 
**content_type** | **str** | Document content type. | [optional] 
**public_id** | **str** | Document public id | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_document200_response_meta import GetDocument200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocument200ResponseMeta from a JSON string
get_document200_response_meta_instance = GetDocument200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(GetDocument200ResponseMeta.to_json())

# convert the object into a dict
get_document200_response_meta_dict = get_document200_response_meta_instance.to_dict()
# create an instance of GetDocument200ResponseMeta from a dict
get_document200_response_meta_from_dict = GetDocument200ResponseMeta.from_dict(get_document200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


