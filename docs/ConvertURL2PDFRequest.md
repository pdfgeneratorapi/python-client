# ConvertURL2PDFRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Public URL | [optional] 
**paper_size** | **str** | PDF page size | [optional] [default to 'a4']
**orientation** | **str** |  | [optional] [default to 'portrait']
**output** | **str** | Output | [optional] [default to 'base64']
**filename** | **str** | Document name | [optional] 

## Example

```python
from pdf_generator_api_client.models.convert_url2_pdf_request import ConvertURL2PDFRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertURL2PDFRequest from a JSON string
convert_url2_pdf_request_instance = ConvertURL2PDFRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertURL2PDFRequest.to_json())

# convert the object into a dict
convert_url2_pdf_request_dict = convert_url2_pdf_request_instance.to_dict()
# create an instance of ConvertURL2PDFRequest from a dict
convert_url2_pdf_request_from_dict = ConvertURL2PDFRequest.from_dict(convert_url2_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


