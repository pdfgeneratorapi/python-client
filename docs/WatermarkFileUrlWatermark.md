# WatermarkFileUrlWatermark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**WatermarkImage**](WatermarkImage.md) |  | [optional] 
**text** | [**WatermarkText**](WatermarkText.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.watermark_file_url_watermark import WatermarkFileUrlWatermark

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkFileUrlWatermark from a JSON string
watermark_file_url_watermark_instance = WatermarkFileUrlWatermark.from_json(json)
# print the JSON string representation of the object
print(WatermarkFileUrlWatermark.to_json())

# convert the object into a dict
watermark_file_url_watermark_dict = watermark_file_url_watermark_instance.to_dict()
# create an instance of WatermarkFileUrlWatermark from a dict
watermark_file_url_watermark_from_dict = WatermarkFileUrlWatermark.from_dict(watermark_file_url_watermark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


