# AddWatermark422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error description | [optional] 
**errors** | **object** | Details about validation errors | [optional] 

## Example

```python
from pdf_generator_api_client.models.add_watermark422_response import AddWatermark422Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddWatermark422Response from a JSON string
add_watermark422_response_instance = AddWatermark422Response.from_json(json)
# print the JSON string representation of the object
print(AddWatermark422Response.to_json())

# convert the object into a dict
add_watermark422_response_dict = add_watermark422_response_instance.to_dict()
# create an instance of AddWatermark422Response from a dict
add_watermark422_response_from_dict = AddWatermark422Response.from_dict(add_watermark422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


