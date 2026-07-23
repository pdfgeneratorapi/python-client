# PrefillParam

Viewer prefill data, encrypted into the viewer URL. Only applied when `output` is `viewer`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_code** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**signature_id** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] [default to True]

## Example

```python
from pdf_generator_api_client.models.prefill_param import PrefillParam

# TODO update the JSON string below
json = "{}"
# create an instance of PrefillParam from a JSON string
prefill_param_instance = PrefillParam.from_json(json)
# print the JSON string representation of the object
print(PrefillParam.to_json())

# convert the object into a dict
prefill_param_dict = prefill_param_instance.to_dict()
# create an instance of PrefillParam from a dict
prefill_param_from_dict = PrefillParam.from_dict(prefill_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


