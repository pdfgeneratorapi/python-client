# ConvertPDF2ImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | Base64 encoded PDF file. Required if file_url is not provided. | [optional] 
**file_url** | **str** | Public HTTPS URL to a PDF file. Required if file_base64 is not provided. | [optional] 
**format** | **str** | Output image format | [optional] [default to 'png']
**quality** | **int** | Image quality (1-100) | [optional] [default to 85]
**resolution** | **int** | Image resolution in DPI (72-600) | [optional] [default to 150]
**pages** | **str** | Page number or range to convert. Use a single number (e.g. \&quot;1\&quot;) or a range (e.g. \&quot;1-4\&quot;). Defaults to all pages. | [optional] [default to 'all']
**output** | **str** | Output format | [optional] [default to 'base64']
**name** | **str** | Document name (max 120 characters). Auto-generated if not provided. | [optional] 

## Example

```python
from pdf_generator_api_client.models.convert_pdf2_image_request import ConvertPDF2ImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertPDF2ImageRequest from a JSON string
convert_pdf2_image_request_instance = ConvertPDF2ImageRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertPDF2ImageRequest.to_json())

# convert the object into a dict
convert_pdf2_image_request_dict = convert_pdf2_image_request_instance.to_dict()
# create an instance of ConvertPDF2ImageRequest from a dict
convert_pdf2_image_request_from_dict = ConvertPDF2ImageRequest.from_dict(convert_pdf2_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


