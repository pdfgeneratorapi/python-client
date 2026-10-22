# FormActionSend

Posts the submitted answers as JSON to the specified HTTPS URL. When the form also stores the document (store_document) and has a template, the request includes the generated document as well; otherwise only the answers are sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_document** | [**FormActionSendSendDocument**](FormActionSendSendDocument.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_action_send import FormActionSend

# TODO update the JSON string below
json = "{}"
# create an instance of FormActionSend from a JSON string
form_action_send_instance = FormActionSend.from_json(json)
# print the JSON string representation of the object
print(FormActionSend.to_json())

# convert the object into a dict
form_action_send_dict = form_action_send_instance.to_dict()
# create an instance of FormActionSend from a dict
form_action_send_from_dict = FormActionSend.from_dict(form_action_send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


