# EncryptDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**owner_password** | **str** | An owner password to open the encrypted document | 
**user_password** | **str** | An user password to open the encrypted document | [optional] 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**file_base64** | **str** | PDF document in base64 encoded string format | 

## Example

```python
from pdf_generator_api_client.models.encrypt_document_request import EncryptDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptDocumentRequest from a JSON string
encrypt_document_request_instance = EncryptDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(EncryptDocumentRequest.to_json())

# convert the object into a dict
encrypt_document_request_dict = encrypt_document_request_instance.to_dict()
# create an instance of EncryptDocumentRequest from a dict
encrypt_document_request_from_dict = EncryptDocumentRequest.from_dict(encrypt_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


