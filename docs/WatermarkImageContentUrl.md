# WatermarkImageContentUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_url** | **str** | URL to an image | 
**position** | [**WatermarkPosition**](WatermarkPosition.md) |  | [optional] [default to WatermarkPosition.CENTER]
**rotation** | **int** | Watermark rotation | [optional] [default to 0]
**scale** | **float** | Watermark image scale | [optional] [default to 1]

## Example

```python
from pdf_generator_api_client.models.watermark_image_content_url import WatermarkImageContentUrl

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkImageContentUrl from a JSON string
watermark_image_content_url_instance = WatermarkImageContentUrl.from_json(json)
# print the JSON string representation of the object
print(WatermarkImageContentUrl.to_json())

# convert the object into a dict
watermark_image_content_url_dict = watermark_image_content_url_instance.to_dict()
# create an instance of WatermarkImageContentUrl from a dict
watermark_image_content_url_from_dict = WatermarkImageContentUrl.from_dict(watermark_image_content_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


