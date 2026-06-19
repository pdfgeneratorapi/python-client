# GetStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**StatusParam**](StatusParam.md) |  | [optional] [default to StatusParam.OK]
**chart_api** | [**StatusParam**](StatusParam.md) |  | [optional] [default to StatusParam.OK]
**conversion_api** | [**StatusParam**](StatusParam.md) |  | [optional] [default to StatusParam.OK]
**generator_api_sync** | [**StatusParam**](StatusParam.md) |  | [optional] [default to StatusParam.OK]
**generator_api_async** | [**StatusParam**](StatusParam.md) |  | [optional] [default to StatusParam.OK]
**e_invoice** | [**StatusParam**](StatusParam.md) |  | [optional] [default to StatusParam.OK]

## Example

```python
from pdf_generator_api_client.models.get_status200_response import GetStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200Response from a JSON string
get_status200_response_instance = GetStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatus200Response.to_json())

# convert the object into a dict
get_status200_response_dict = get_status200_response_instance.to_dict()
# create an instance of GetStatus200Response from a dict
get_status200_response_from_dict = GetStatus200Response.from_dict(get_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


