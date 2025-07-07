# AddWatermarkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | PDF file from remote URL to add the watermark to | 
**watermark** | [**WatermarkFileUrlWatermark**](WatermarkFileUrlWatermark.md) |  | 
**output** | **str** | Returned document output | [optional] [default to 'base64']
**name** | **str** | File name of the returned document | [optional] 
**file_base64** | **str** | PDF file from base64 string to add the watermark to | 

## Example

```python
from pdf_generator_api_client.models.add_watermark_request import AddWatermarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWatermarkRequest from a JSON string
add_watermark_request_instance = AddWatermarkRequest.from_json(json)
# print the JSON string representation of the object
print(AddWatermarkRequest.to_json())

# convert the object into a dict
add_watermark_request_dict = add_watermark_request_instance.to_dict()
# create an instance of AddWatermarkRequest from a dict
add_watermark_request_from_dict = AddWatermarkRequest.from_dict(add_watermark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


