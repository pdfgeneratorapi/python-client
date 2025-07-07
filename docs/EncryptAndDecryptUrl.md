# EncryptAndDecryptUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**owner_password** | **str** | An owner password to open the encrypted document | 
**user_password** | **str** | An user password to open the encrypted document | [optional] 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']

## Example

```python
from pdf_generator_api_client.models.encrypt_and_decrypt_url import EncryptAndDecryptUrl

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptAndDecryptUrl from a JSON string
encrypt_and_decrypt_url_instance = EncryptAndDecryptUrl.from_json(json)
# print the JSON string representation of the object
print(EncryptAndDecryptUrl.to_json())

# convert the object into a dict
encrypt_and_decrypt_url_dict = encrypt_and_decrypt_url_instance.to_dict()
# create an instance of EncryptAndDecryptUrl from a dict
encrypt_and_decrypt_url_from_dict = EncryptAndDecryptUrl.from_dict(encrypt_and_decrypt_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


