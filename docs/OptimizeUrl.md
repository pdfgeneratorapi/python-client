# OptimizeUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']

## Example

```python
from pdf_generator_api_client.models.optimize_url import OptimizeUrl

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeUrl from a JSON string
optimize_url_instance = OptimizeUrl.from_json(json)
# print the JSON string representation of the object
print(OptimizeUrl.to_json())

# convert the object into a dict
optimize_url_dict = optimize_url_instance.to_dict()
# create an instance of OptimizeUrl from a dict
optimize_url_from_dict = OptimizeUrl.from_dict(optimize_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


