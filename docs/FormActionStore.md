# FormActionStore

Key-value pair of action configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_document** | **bool** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_action_store import FormActionStore

# TODO update the JSON string below
json = "{}"
# create an instance of FormActionStore from a JSON string
form_action_store_instance = FormActionStore.from_json(json)
# print the JSON string representation of the object
print(FormActionStore.to_json())

# convert the object into a dict
form_action_store_dict = form_action_store_instance.to_dict()
# create an instance of FormActionStore from a dict
form_action_store_from_dict = FormActionStore.from_dict(form_action_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


