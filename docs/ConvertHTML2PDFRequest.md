# ConvertHTML2PDFRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | HTML content | [optional] 
**paper_size** | **str** | PDF page size | [optional] [default to 'a4']
**orientation** | **str** |  | [optional] [default to 'portrait']
**output** | **str** | Output | [optional] [default to 'base64']
**filename** | **str** | Document name | [optional] 

## Example

```python
from pdf_generator_api_client.models.convert_html2_pdf_request import ConvertHTML2PDFRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertHTML2PDFRequest from a JSON string
convert_html2_pdf_request_instance = ConvertHTML2PDFRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertHTML2PDFRequest.to_json())

# convert the object into a dict
convert_html2_pdf_request_dict = convert_html2_pdf_request_instance.to_dict()
# create an instance of ConvertHTML2PDFRequest from a dict
convert_html2_pdf_request_from_dict = ConvertHTML2PDFRequest.from_dict(convert_html2_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


