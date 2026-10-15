# FormField

Form field definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Field label displayed in the form | 
**name** | **str** | Data field name. For example \&quot;name\&quot; can be used as \&quot;{name}\&quot; in the document as placeholder. | 
**type** | **str** | Field type * &#x60;text&#x60; - Free text input * &#x60;integer&#x60; - Whole number input * &#x60;number&#x60; - Decimal number input * &#x60;date&#x60; - Date picker * &#x60;signature&#x60; - Hand-drawn signature, stored as an image * &#x60;select&#x60; - Dropdown with a single choice. Requires &#x60;subRows&#x60; with options and a &#x60;default&#x60; value * &#x60;multi-select&#x60; - Dropdown with multiple choices. Requires &#x60;subRows&#x60; with options * &#x60;table&#x60; - Repeating rows of values. Its columns are defined in &#x60;subRows&#x60; * &#x60;image&#x60; - Image upload * &#x60;pdf&#x60; - PDF file upload  | 
**required** | **bool** | Specifies if the field is required or not | 
**default** | **str** | Value pre-filled in the field. Required for &#x60;select&#x60; fields and must be one of the options. Not used by &#x60;table&#x60; fields. | [optional] 
**description** | **str** | Help text shown with the field | [optional] 
**sub_rows** | [**List[FormFieldSubRowsInner]**](FormFieldSubRowsInner.md) | Options for &#x60;select&#x60; and &#x60;multi-select&#x60; fields (a single object), columns for &#x60;table&#x60; fields. Not used by other field types. | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_field import FormField

# TODO update the JSON string below
json = "{}"
# create an instance of FormField from a JSON string
form_field_instance = FormField.from_json(json)
# print the JSON string representation of the object
print(FormField.to_json())

# convert the object into a dict
form_field_dict = form_field_instance.to_dict()
# create an instance of FormField from a dict
form_field_from_dict = FormField.from_dict(form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


