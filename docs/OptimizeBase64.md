# OptimizeBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF document in base64 encoded string format | 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']

## Example

```python
from pdf_generator_api_client.models.optimize_base64 import OptimizeBase64

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeBase64 from a JSON string
optimize_base64_instance = OptimizeBase64.from_json(json)
# print the JSON string representation of the object
print(OptimizeBase64.to_json())

# convert the object into a dict
optimize_base64_dict = optimize_base64_instance.to_dict()
# create an instance of OptimizeBase64 from a dict
optimize_base64_from_dict = OptimizeBase64.from_dict(optimize_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


