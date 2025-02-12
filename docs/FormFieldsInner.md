# FormFieldsInner

Form field definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Field label displayed in the form | [optional] 
**name** | **str** | Data field name. For example \&quot;name\&quot; can be used as \&quot;{name}\&quot; in the document as placeholder. | [optional] 
**type** | **str** | Field type | [optional] 
**required** | **bool** | Specifies if the field is required or not | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_fields_inner import FormFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldsInner from a JSON string
form_fields_inner_instance = FormFieldsInner.from_json(json)
# print the JSON string representation of the object
print(FormFieldsInner.to_json())

# convert the object into a dict
form_fields_inner_dict = form_fields_inner_instance.to_dict()
# create an instance of FormFieldsInner from a dict
form_fields_inner_from_dict = FormFieldsInner.from_dict(form_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


