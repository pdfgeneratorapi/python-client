# GetTemplateLibrary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[PublicTemplateLibraryItem]**](PublicTemplateLibraryItem.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_template_library200_response import GetTemplateLibrary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplateLibrary200Response from a JSON string
get_template_library200_response_instance = GetTemplateLibrary200Response.from_json(json)
# print the JSON string representation of the object
print(GetTemplateLibrary200Response.to_json())

# convert the object into a dict
get_template_library200_response_dict = get_template_library200_response_instance.to_dict()
# create an instance of GetTemplateLibrary200Response from a dict
get_template_library200_response_from_dict = GetTemplateLibrary200Response.from_dict(get_template_library200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


