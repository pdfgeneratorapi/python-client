# AddWatermark201ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name. This value is automatically generated if name attribute is not defined in request. | [optional] 
**display_name** | **str** | Document name without the file extension. | [optional] 
**encoding** | **str** | Document encoding | [optional] 
**content_type** | **str** | Document content type. | [optional] 
**public_id** | **str** | Document public id, if output&#x3D;url was used for document storage | [optional] 

## Example

```python
from pdf_generator_api_client.models.add_watermark201_response_meta import AddWatermark201ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AddWatermark201ResponseMeta from a JSON string
add_watermark201_response_meta_instance = AddWatermark201ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(AddWatermark201ResponseMeta.to_json())

# convert the object into a dict
add_watermark201_response_meta_dict = add_watermark201_response_meta_instance.to_dict()
# create an instance of AddWatermark201ResponseMeta from a dict
add_watermark201_response_meta_from_dict = AddWatermark201ResponseMeta.from_dict(add_watermark201_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


