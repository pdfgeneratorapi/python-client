# StoreDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | Base64 encoded PDF file. Required if file_url is not provided. | [optional] 
**file_url** | **str** | Public HTTPS URL to a PDF file. Required if file_base64 is not provided. | [optional] 
**name** | **str** | Generated document name (optional) | [optional] [default to '']
**output** | **str** | Response format. &#x60;url&#x60; returns a public URL to the stored document; &#x60;viewer&#x60; returns a public URL to the PDF viewer. | [optional] [default to 'url']

## Example

```python
from pdf_generator_api_client.models.store_document_request import StoreDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreDocumentRequest from a JSON string
store_document_request_instance = StoreDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(StoreDocumentRequest.to_json())

# convert the object into a dict
store_document_request_dict = store_document_request_instance.to_dict()
# create an instance of StoreDocumentRequest from a dict
store_document_request_from_dict = StoreDocumentRequest.from_dict(store_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


