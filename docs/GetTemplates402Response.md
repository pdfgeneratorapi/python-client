# GetTemplates402Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error description | [optional] 
**status** | **int** | HTTP Error code | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_templates402_response import GetTemplates402Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplates402Response from a JSON string
get_templates402_response_instance = GetTemplates402Response.from_json(json)
# print the JSON string representation of the object
print(GetTemplates402Response.to_json())

# convert the object into a dict
get_templates402_response_dict = get_templates402_response_instance.to_dict()
# create an instance of GetTemplates402Response from a dict
get_templates402_response_from_dict = GetTemplates402Response.from_dict(get_templates402_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


