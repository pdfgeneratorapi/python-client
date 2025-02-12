# GenerateDocumentAsynchronousRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**TemplateParam**](TemplateParam.md) |  | [optional] 
**callback** | [**CallbackParam**](CallbackParam.md) |  | [optional] 
**format** | [**FormatParam**](FormatParam.md) |  | [optional] [default to FormatParam.PDF]
**output** | [**AsyncOutputParam**](AsyncOutputParam.md) |  | [optional] [default to AsyncOutputParam.BASE64]
**name** | **str** | Generated document name (optional) | [optional] [default to '']
**testing** | **bool** | When set to true the generation is not counted as merge (monthly usage), but a large PREVIEW stamp is added. | [optional] [default to False]

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


