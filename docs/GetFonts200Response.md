# GetFonts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[Font]**](Font.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_fonts200_response import GetFonts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFonts200Response from a JSON string
get_fonts200_response_instance = GetFonts200Response.from_json(json)
# print the JSON string representation of the object
print(GetFonts200Response.to_json())

# convert the object into a dict
get_fonts200_response_dict = get_fonts200_response_instance.to_dict()
# create an instance of GetFonts200Response from a dict
get_fonts200_response_from_dict = GetFonts200Response.from_dict(get_fonts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


