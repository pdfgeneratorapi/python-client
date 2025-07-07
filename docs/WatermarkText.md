# WatermarkText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Watermark text | 
**color** | **str** | Watermark text color in hexadecimal format | [optional] [default to '#000000']
**size** | **int** | Watermark text font size in px | [optional] [default to 48]
**opacity** | **float** | Watermark text opaxity | [optional] [default to 0.5]
**position** | [**WatermarkPosition**](WatermarkPosition.md) |  | [optional] [default to WatermarkPosition.CENTER]
**rotation** | **int** | Watermark rotation | [optional] [default to 0]

## Example

```python
from pdf_generator_api_client.models.watermark_text import WatermarkText

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkText from a JSON string
watermark_text_instance = WatermarkText.from_json(json)
# print the JSON string representation of the object
print(WatermarkText.to_json())

# convert the object into a dict
watermark_text_dict = watermark_text_instance.to_dict()
# create an instance of WatermarkText from a dict
watermark_text_from_dict = WatermarkText.from_dict(watermark_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


