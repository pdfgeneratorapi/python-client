# GenerateQRCode201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Base64 encoded image if the output&#x3D;base64. Raw image string if output&#x3D;file is used | [optional] 
**meta** | [**GenerateQRCode201ResponseMeta**](GenerateQRCode201ResponseMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_qr_code201_response import GenerateQRCode201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateQRCode201Response from a JSON string
generate_qr_code201_response_instance = GenerateQRCode201Response.from_json(json)
# print the JSON string representation of the object
print(GenerateQRCode201Response.to_json())

# convert the object into a dict
generate_qr_code201_response_dict = generate_qr_code201_response_instance.to_dict()
# create an instance of GenerateQRCode201Response from a dict
generate_qr_code201_response_from_dict = GenerateQRCode201Response.from_dict(generate_qr_code201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


