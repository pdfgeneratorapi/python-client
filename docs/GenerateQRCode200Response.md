# GenerateQRCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Base64 encoded PNG image | [optional] 
**meta** | [**GenerateQRCode200ResponseMeta**](GenerateQRCode200ResponseMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_qr_code200_response import GenerateQRCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateQRCode200Response from a JSON string
generate_qr_code200_response_instance = GenerateQRCode200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateQRCode200Response.to_json())

# convert the object into a dict
generate_qr_code200_response_dict = generate_qr_code200_response_instance.to_dict()
# create an instance of GenerateQRCode200Response from a dict
generate_qr_code200_response_from_dict = GenerateQRCode200Response.from_dict(generate_qr_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


