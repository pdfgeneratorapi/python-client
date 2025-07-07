# WatermarkImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_url** | **str** | URL to an image | 
**position** | [**WatermarkPosition**](WatermarkPosition.md) |  | [optional] [default to WatermarkPosition.CENTER]
**rotation** | **int** | Watermark rotation | [optional] [default to 0]
**scale** | **float** | Watermark image scale | [optional] [default to 1]
**content_base64** | **str** | Base64 image string | 

## Example

```python
from pdf_generator_api_client.models.watermark_image import WatermarkImage

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkImage from a JSON string
watermark_image_instance = WatermarkImage.from_json(json)
# print the JSON string representation of the object
print(WatermarkImage.to_json())

# convert the object into a dict
watermark_image_dict = watermark_image_instance.to_dict()
# create an instance of WatermarkImage from a dict
watermark_image_from_dict = WatermarkImage.from_dict(watermark_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


