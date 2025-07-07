# WatermarkImageContentBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_base64** | **str** | Base64 image string | 
**position** | [**WatermarkPosition**](WatermarkPosition.md) |  | [optional] [default to WatermarkPosition.CENTER]
**rotation** | **int** | Watermark rotation | [optional] [default to 0]
**scale** | **float** | Watermark image scale | [optional] [default to 1]

## Example

```python
from pdf_generator_api_client.models.watermark_image_content_base64 import WatermarkImageContentBase64

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkImageContentBase64 from a JSON string
watermark_image_content_base64_instance = WatermarkImageContentBase64.from_json(json)
# print the JSON string representation of the object
print(WatermarkImageContentBase64.to_json())

# convert the object into a dict
watermark_image_content_base64_dict = watermark_image_content_base64_instance.to_dict()
# create an instance of WatermarkImageContentBase64 from a dict
watermark_image_content_base64_from_dict = WatermarkImageContentBase64.from_dict(watermark_image_content_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


