# GenerateViewerUrl200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Public URL to the PDF viewer. | [optional] 
**meta** | [**GenerateViewerUrl200ResponseMeta**](GenerateViewerUrl200ResponseMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_viewer_url200_response import GenerateViewerUrl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateViewerUrl200Response from a JSON string
generate_viewer_url200_response_instance = GenerateViewerUrl200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateViewerUrl200Response.to_json())

# convert the object into a dict
generate_viewer_url200_response_dict = generate_viewer_url200_response_instance.to_dict()
# create an instance of GenerateViewerUrl200Response from a dict
generate_viewer_url200_response_from_dict = GenerateViewerUrl200Response.from_dict(generate_viewer_url200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


