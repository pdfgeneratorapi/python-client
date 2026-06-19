# FormActionSendSendDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | HTTPS URL where the generated document will be delivered. | 
**headers** | [**List[FormActionSendSendDocumentHeadersInner]**](FormActionSendSendDocumentHeadersInner.md) | Optional HTTP headers to include with the delivery request. | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_action_send_send_document import FormActionSendSendDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FormActionSendSendDocument from a JSON string
form_action_send_send_document_instance = FormActionSendSendDocument.from_json(json)
# print the JSON string representation of the object
print(FormActionSendSendDocument.to_json())

# convert the object into a dict
form_action_send_send_document_dict = form_action_send_send_document_instance.to_dict()
# create an instance of FormActionSendSendDocument from a dict
form_action_send_send_document_from_dict = FormActionSendSendDocument.from_dict(form_action_send_send_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


