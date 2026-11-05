# WatermarkFileUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | PDF file from remote URL to add the watermark to | 
**watermark** | [**WatermarkFileUrlWatermark**](WatermarkFileUrlWatermark.md) |  | 
**output** | **str** | Returned document output | [optional] [default to 'base64']
**name** | **str** | File name of the returned document | [optional] 

## Example

```python
from pdf_generator_api_client.models.watermark_file_url import WatermarkFileUrl

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkFileUrl from a JSON string
watermark_file_url_instance = WatermarkFileUrl.from_json(json)
# print the JSON string representation of the object
print(WatermarkFileUrl.to_json())

# convert the object into a dict
watermark_file_url_dict = watermark_file_url_instance.to_dict()
# create an instance of WatermarkFileUrl from a dict
watermark_file_url_from_dict = WatermarkFileUrl.from_dict(watermark_file_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


