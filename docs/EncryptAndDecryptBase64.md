# EncryptAndDecryptBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF document in base64 encoded string format | 
**owner_password** | **str** | An owner password to open the encrypted document | 
**user_password** | **str** | An user password to open the encrypted document | [optional] 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']

## Example

```python
from pdf_generator_api_client.models.encrypt_and_decrypt_base64 import EncryptAndDecryptBase64

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptAndDecryptBase64 from a JSON string
encrypt_and_decrypt_base64_instance = EncryptAndDecryptBase64.from_json(json)
# print the JSON string representation of the object
print(EncryptAndDecryptBase64.to_json())

# convert the object into a dict
encrypt_and_decrypt_base64_dict = encrypt_and_decrypt_base64_instance.to_dict()
# create an instance of EncryptAndDecryptBase64 from a dict
encrypt_and_decrypt_base64_from_dict = EncryptAndDecryptBase64.from_dict(encrypt_and_decrypt_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


