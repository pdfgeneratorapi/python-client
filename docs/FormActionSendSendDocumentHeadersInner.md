# FormActionSendSendDocumentHeadersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Header name | 
**value** | **str** | Header value | 

## Example

```python
from pdf_generator_api_client.models.form_action_send_send_document_headers_inner import FormActionSendSendDocumentHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormActionSendSendDocumentHeadersInner from a JSON string
form_action_send_send_document_headers_inner_instance = FormActionSendSendDocumentHeadersInner.from_json(json)
# print the JSON string representation of the object
print(FormActionSendSendDocumentHeadersInner.to_json())

# convert the object into a dict
form_action_send_send_document_headers_inner_dict = form_action_send_send_document_headers_inner_instance.to_dict()
# create an instance of FormActionSendSendDocumentHeadersInner from a dict
form_action_send_send_document_headers_inner_from_dict = FormActionSendSendDocumentHeadersInner.from_dict(form_action_send_send_document_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


