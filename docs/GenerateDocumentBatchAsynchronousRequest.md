# GenerateDocumentBatchAsynchronousRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**List[TemplateParam]**](TemplateParam.md) |  | [optional] 
**callback** | [**CallbackParam**](CallbackParam.md) |  | [optional] 
**format** | [**FormatParam**](FormatParam.md) |  | [optional] [default to FormatParam.PDF]
**output** | [**AsyncOutputParam**](AsyncOutputParam.md) |  | [optional] [default to AsyncOutputParam.BASE64]
**name** | **str** | Generated document name (optional) | [optional] [default to '']
**testing** | **bool** | When set to true the generation is not counted as merge (monthly usage), but a large PREVIEW stamp is added. | [optional] [default to False]

## Example

```python
from pdf_generator_api_client.models.generate_document_batch_asynchronous_request import GenerateDocumentBatchAsynchronousRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocumentBatchAsynchronousRequest from a JSON string
generate_document_batch_asynchronous_request_instance = GenerateDocumentBatchAsynchronousRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateDocumentBatchAsynchronousRequest.to_json())

# convert the object into a dict
generate_document_batch_asynchronous_request_dict = generate_document_batch_asynchronous_request_instance.to_dict()
# create an instance of GenerateDocumentBatchAsynchronousRequest from a dict
generate_document_batch_asynchronous_request_from_dict = GenerateDocumentBatchAsynchronousRequest.from_dict(generate_document_batch_asynchronous_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


