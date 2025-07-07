# FormFillUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**data** | **object** | Form field data to fill in the PDF | 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**name** | **str** | Name for the PDF file | [optional] 

## Example

```python
from pdf_generator_api_client.models.form_fill_url import FormFillUrl

# TODO update the JSON string below
json = "{}"
# create an instance of FormFillUrl from a JSON string
form_fill_url_instance = FormFillUrl.from_json(json)
# print the JSON string representation of the object
print(FormFillUrl.to_json())

# convert the object into a dict
form_fill_url_dict = form_fill_url_instance.to_dict()
# create an instance of FormFillUrl from a dict
form_fill_url_from_dict = FormFillUrl.from_dict(form_fill_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


