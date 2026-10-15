# FormTableColumn

Table column definition. Column names must be unique within the table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Column label displayed in the form | 
**name** | **str** | Data field name of the column | 
**type** | **str** | Column type. &#x60;select&#x60; columns require &#x60;subRows&#x60; with options and a &#x60;default&#x60; value. | 
**required** | **bool** | Specifies if the column is required or not | 
**default** | **str** | Value pre-filled in the column. Required for &#x60;select&#x60; columns and must be one of the options. | [optional] 
**sub_rows** | [**List[FormFieldOptions]**](FormFieldOptions.md) | Options for &#x60;select&#x60; columns (a single object). Not used by other column types. | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_table_column import FormTableColumn

# TODO update the JSON string below
json = "{}"
# create an instance of FormTableColumn from a JSON string
form_table_column_instance = FormTableColumn.from_json(json)
# print the JSON string representation of the object
print(FormTableColumn.to_json())

# convert the object into a dict
form_table_column_dict = form_table_column_instance.to_dict()
# create an instance of FormTableColumn from a dict
form_table_column_from_dict = FormTableColumn.from_dict(form_table_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


