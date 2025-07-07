# WatermarkBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF file from base64 string to add the watermark to | 
**watermark** | [**WatermarkFileUrlWatermark**](WatermarkFileUrlWatermark.md) |  | 
**output** | **str** | Returned document output | [optional] [default to 'base64']
**name** | **str** | File name of the returned document | [optional] 

## Example

```python
from pdf_generator_api_client.models.watermark_base64 import WatermarkBase64

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkBase64 from a JSON string
watermark_base64_instance = WatermarkBase64.from_json(json)
# print the JSON string representation of the object
print(WatermarkBase64.to_json())

# convert the object into a dict
watermark_base64_dict = watermark_base64_instance.to_dict()
# create an instance of WatermarkBase64 from a dict
watermark_base64_from_dict = WatermarkBase64.from_dict(watermark_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


