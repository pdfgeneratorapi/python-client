# CallbackParam

Callback URL and optional headers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Public callback URL that is used to make a POST request when the document is generated. | [optional] 
**headers** | **object** | A key-value pairs of header values sent with the POST request. | [optional] 

## Example

```python
from pdf_generator_api_client.models.callback_param import CallbackParam

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackParam from a JSON string
callback_param_instance = CallbackParam.from_json(json)
# print the JSON string representation of the object
print(CallbackParam.to_json())

# convert the object into a dict
callback_param_dict = callback_param_instance.to_dict()
# create an instance of CallbackParam from a dict
callback_param_from_dict = CallbackParam.from_dict(callback_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


