# ShareForm201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Public URL for form data collection | [optional] 
**meta** | [**ShareForm201ResponseMeta**](ShareForm201ResponseMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.share_form201_response import ShareForm201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShareForm201Response from a JSON string
share_form201_response_instance = ShareForm201Response.from_json(json)
# print the JSON string representation of the object
print(ShareForm201Response.to_json())

# convert the object into a dict
share_form201_response_dict = share_form201_response_instance.to_dict()
# create an instance of ShareForm201Response from a dict
share_form201_response_from_dict = ShareForm201Response.from_dict(share_form201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


