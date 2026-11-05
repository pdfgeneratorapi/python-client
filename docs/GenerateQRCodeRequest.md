# GenerateQRCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The content which is used to generate QR code | 
**color** | **str** | QR code color as a hex color code | [optional] [default to '#000000']
**logo_base64** | **str** | A logo as a base64 image string to add on the QR code. Cannot be combined with &#x60;logo_url&#x60;. | [optional] 
**logo_url** | **str** | Public HTTPS URL of a logo image to add on the QR code. Cannot be combined with &#x60;logo_base64&#x60;. | [optional] 
**output** | **str** | Response format | [optional] [default to 'base64']

## Example

```python
from pdf_generator_api_client.models.generate_qr_code_request import GenerateQRCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateQRCodeRequest from a JSON string
generate_qr_code_request_instance = GenerateQRCodeRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateQRCodeRequest.to_json())

# convert the object into a dict
generate_qr_code_request_dict = generate_qr_code_request_instance.to_dict()
# create an instance of GenerateQRCodeRequest from a dict
generate_qr_code_request_from_dict = GenerateQRCodeRequest.from_dict(generate_qr_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


