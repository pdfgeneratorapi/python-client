# GenerateQRCode201ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **str** | Response encoding | [optional] 
**content_type** | **str** | Response content type. | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_qr_code201_response_meta import GenerateQRCode201ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateQRCode201ResponseMeta from a JSON string
generate_qr_code201_response_meta_instance = GenerateQRCode201ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(GenerateQRCode201ResponseMeta.to_json())

# convert the object into a dict
generate_qr_code201_response_meta_dict = generate_qr_code201_response_meta_instance.to_dict()
# create an instance of GenerateQRCode201ResponseMeta from a dict
generate_qr_code201_response_meta_from_dict = GenerateQRCode201ResponseMeta.from_dict(generate_qr_code201_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


