# FormFieldSubRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **str** | Comma-separated list of choices. Whitespace around each choice is trimmed and choices must be unique. | 
**label** | **str** | Column label displayed in the form | 
**name** | **str** | Data field name of the column | 
**type** | **str** | Column type. &#x60;select&#x60; columns require &#x60;subRows&#x60; with options and a &#x60;default&#x60; value. | 
**required** | **bool** | Specifies if the column is required or not | 
**default** | **str** | Value pre-filled in the column. Required for &#x60;select&#x60; columns and must be one of the options. | [optional] 
**sub_rows** | [**List[FormFieldOptions]**](FormFieldOptions.md) | Options for &#x60;select&#x60; columns (a single object). Not used by other column types. | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_field_sub_rows_inner import FormFieldSubRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldSubRowsInner from a JSON string
form_field_sub_rows_inner_instance = FormFieldSubRowsInner.from_json(json)
# print the JSON string representation of the object
print(FormFieldSubRowsInner.to_json())

# convert the object into a dict
form_field_sub_rows_inner_dict = form_field_sub_rows_inner_instance.to_dict()
# create an instance of FormFieldSubRowsInner from a dict
form_field_sub_rows_inner_from_dict = FormFieldSubRowsInner.from_dict(form_field_sub_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


