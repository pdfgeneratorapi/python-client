# OptimizeDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | Public URL to a PDF document | 
**name** | **str** | Name for the PDF file | [optional] 
**output** | **str** | Returned document output format | [optional] [default to 'base64']
**file_base64** | **str** | PDF document in base64 encoded string format | 

## Example

```python
from pdf_generator_api_client.models.optimize_document_request import OptimizeDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeDocumentRequest from a JSON string
optimize_document_request_instance = OptimizeDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(OptimizeDocumentRequest.to_json())

# convert the object into a dict
optimize_document_request_dict = optimize_document_request_instance.to_dict()
# create an instance of OptimizeDocumentRequest from a dict
optimize_document_request_from_dict = OptimizeDocumentRequest.from_dict(optimize_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


