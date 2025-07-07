# GetTemplates429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error description | [optional] 
**status** | **int** | HTTP Error code | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_templates429_response import GetTemplates429Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplates429Response from a JSON string
get_templates429_response_instance = GetTemplates429Response.from_json(json)
# print the JSON string representation of the object
print(GetTemplates429Response.to_json())

# convert the object into a dict
get_templates429_response_dict = get_templates429_response_instance.to_dict()
# create an instance of GetTemplates429Response from a dict
get_templates429_response_from_dict = GetTemplates429Response.from_dict(get_templates429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


