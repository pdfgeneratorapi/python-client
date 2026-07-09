# GenerateViewerUrl200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**public_id** | **str** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_viewer_url200_response_meta import GenerateViewerUrl200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateViewerUrl200ResponseMeta from a JSON string
generate_viewer_url200_response_meta_instance = GenerateViewerUrl200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(GenerateViewerUrl200ResponseMeta.to_json())

# convert the object into a dict
generate_viewer_url200_response_meta_dict = generate_viewer_url200_response_meta_instance.to_dict()
# create an instance of GenerateViewerUrl200ResponseMeta from a dict
generate_viewer_url200_response_meta_from_dict = GenerateViewerUrl200ResponseMeta.from_dict(generate_viewer_url200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


