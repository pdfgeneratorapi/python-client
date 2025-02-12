# GetTemplates422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error description | [optional] 
**errors** | **object** | Details about validation errors | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_templates422_response import GetTemplates422Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplates422Response from a JSON string
get_templates422_response_instance = GetTemplates422Response.from_json(json)
# print the JSON string representation of the object
print(GetTemplates422Response.to_json())

# convert the object into a dict
get_templates422_response_dict = get_templates422_response_instance.to_dict()
# create an instance of GetTemplates422Response from a dict
get_templates422_response_from_dict = GetTemplates422Response.from_dict(get_templates422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


