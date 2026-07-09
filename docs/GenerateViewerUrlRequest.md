# GenerateViewerUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** | Response format. &#x60;url&#x60; returns a public URL to the stored document; &#x60;viewer&#x60; returns a public URL to the PDF viewer (with encrypted prefill when provided). | [optional] [default to 'url']
**prefill** | [**PrefillParam**](PrefillParam.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_viewer_url_request import GenerateViewerUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateViewerUrlRequest from a JSON string
generate_viewer_url_request_instance = GenerateViewerUrlRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateViewerUrlRequest.to_json())

# convert the object into a dict
generate_viewer_url_request_dict = generate_viewer_url_request_instance.to_dict()
# create an instance of GenerateViewerUrlRequest from a dict
generate_viewer_url_request_from_dict = GenerateViewerUrlRequest.from_dict(generate_viewer_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


