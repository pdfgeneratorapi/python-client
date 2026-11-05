# GenerateDocumentBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**List[TemplateParam]**](TemplateParam.md) |  | 
**format** | [**FormatParam**](FormatParam.md) |  | [optional] [default to FormatParam.PDF]
**output** | [**OutputParam**](OutputParam.md) |  | [optional] [default to OutputParam.BASE64]
**name** | **str** | Generated document name (optional) | [optional] [default to '']
**testing** | **bool** | When set to true the generation is not counted as merge (monthly usage), but a large PREVIEW stamp is added. | [optional] [default to False]
**var_print** | **bool** | When set to true, the PDF opens the print dialog when it is opened in a viewer. | [optional] [default to False]
**empty_labels** | **int** | Number of label positions to leave empty at the start of the first sheet. Only applies to label templates. | [optional] [default to 0]
**attachments** | [**List[AttachmentsParamInner]**](AttachmentsParamInner.md) | Files embedded into the generated PDF as attachments. Only PDF and XML files are accepted. | [optional] 
**metadata** | [**MetadataParam**](MetadataParam.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_document_batch_request import GenerateDocumentBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocumentBatchRequest from a JSON string
generate_document_batch_request_instance = GenerateDocumentBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateDocumentBatchRequest.to_json())

# convert the object into a dict
generate_document_batch_request_dict = generate_document_batch_request_instance.to_dict()
# create an instance of GenerateDocumentBatchRequest from a dict
generate_document_batch_request_from_dict = GenerateDocumentBatchRequest.from_dict(generate_document_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


