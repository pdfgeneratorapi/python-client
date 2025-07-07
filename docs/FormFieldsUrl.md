# FormFieldsUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 

## Example

```python
from pdf_generator_api_client.models.form_fields_url import FormFieldsUrl

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldsUrl from a JSON string
form_fields_url_instance = FormFieldsUrl.from_json(json)
# print the JSON string representation of the object
print(FormFieldsUrl.to_json())

# convert the object into a dict
form_fields_url_dict = form_fields_url_instance.to_dict()
# create an instance of FormFieldsUrl from a dict
form_fields_url_from_dict = FormFieldsUrl.from_dict(form_fields_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


