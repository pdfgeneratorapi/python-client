# GetForms200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FormConfiguration]**](FormConfiguration.md) |  | [optional] 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.get_forms200_response import GetForms200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetForms200Response from a JSON string
get_forms200_response_instance = GetForms200Response.from_json(json)
# print the JSON string representation of the object
print(GetForms200Response.to_json())

# convert the object into a dict
get_forms200_response_dict = get_forms200_response_instance.to_dict()
# create an instance of GetForms200Response from a dict
get_forms200_response_from_dict = GetForms200Response.from_dict(get_forms200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


