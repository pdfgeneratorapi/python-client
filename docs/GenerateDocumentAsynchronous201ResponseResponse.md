# GenerateDocumentAsynchronous201ResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique job id which is also added to the callback request as header PDF-API-Job-Id | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_document_asynchronous201_response_response import GenerateDocumentAsynchronous201ResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocumentAsynchronous201ResponseResponse from a JSON string
generate_document_asynchronous201_response_response_instance = GenerateDocumentAsynchronous201ResponseResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateDocumentAsynchronous201ResponseResponse.to_json())

# convert the object into a dict
generate_document_asynchronous201_response_response_dict = generate_document_asynchronous201_response_response_instance.to_dict()
# create an instance of GenerateDocumentAsynchronous201ResponseResponse from a dict
generate_document_asynchronous201_response_response_from_dict = GenerateDocumentAsynchronous201ResponseResponse.from_dict(generate_document_asynchronous201_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


