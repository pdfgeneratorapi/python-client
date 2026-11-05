# GenerateDocumentAsynchronousRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**TemplateParam**](TemplateParam.md) |  | [optional] 
**callback** | [**CallbackParam**](CallbackParam.md) |  | 
**format** | [**FormatParam**](FormatParam.md) |  | [optional] [default to FormatParam.PDF]
**output** | [**AsyncOutputParam**](AsyncOutputParam.md) |  | [optional] [default to AsyncOutputParam.BASE64]
**name** | **str** | Generated document name (optional) | [optional] [default to '']
**testing** | **bool** | When set to true the generation is not counted as merge (monthly usage), but a large PREVIEW stamp is added. | [optional] [default to False]
**make_accessible** | **bool** | Enables semantic document tagging. When enabled, a separate Make Accessible action is executed, which consumes additional credits. | [optional] [default to False]
**var_print** | **bool** | When set to true, the PDF opens the print dialog when it is opened in a viewer. | [optional] [default to False]
**empty_labels** | **int** | Number of label positions to leave empty at the start of the first sheet. Only applies to label templates. | [optional] [default to 0]
**attachments** | [**List[AttachmentsParamInner]**](AttachmentsParamInner.md) | Files embedded into the generated PDF as attachments. Only PDF and XML files are accepted. | [optional] 
**metadata** | [**MetadataParam**](MetadataParam.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_document_asynchronous_request import GenerateDocumentAsynchronousRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocumentAsynchronousRequest from a JSON string
generate_document_asynchronous_request_instance = GenerateDocumentAsynchronousRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateDocumentAsynchronousRequest.to_json())

# convert the object into a dict
generate_document_asynchronous_request_dict = generate_document_asynchronous_request_instance.to_dict()
# create an instance of GenerateDocumentAsynchronousRequest from a dict
generate_document_asynchronous_request_from_dict = GenerateDocumentAsynchronousRequest.from_dict(generate_document_asynchronous_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


