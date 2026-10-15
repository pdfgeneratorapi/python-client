# FormFieldOptions

Choices of a `select` or `multi-select` field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **str** | Comma-separated list of choices. Whitespace around each choice is trimmed and choices must be unique. | 

## Example

```python
from pdf_generator_api_client.models.form_field_options import FormFieldOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldOptions from a JSON string
form_field_options_instance = FormFieldOptions.from_json(json)
# print the JSON string representation of the object
print(FormFieldOptions.to_json())

# convert the object into a dict
form_field_options_dict = form_field_options_instance.to_dict()
# create an instance of FormFieldOptions from a dict
form_field_options_from_dict = FormFieldOptions.from_dict(form_field_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


