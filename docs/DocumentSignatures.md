# DocumentSignatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The one-line answer, reduced from every signature worst case first. &#x60;unavailable&#x60; means signature validation is not enabled on this deployment — it says nothing about the document.  | [optional] 
**status_label** | **str** | The status in words, ready to display. | [optional] 
**has_long_term_validation** | **bool** | The document carries the certificate and revocation data needed to verify it after the signing certificates expire.  | [optional] 
**covers_whole_document** | **bool** | The last signature covers every byte, so nothing was appended after it. | [optional] 
**document_timestamps** | **int** | Timestamp-only signatures, counted rather than listed: they are machinery, not people, and would double every signer.  | [optional] 
**signatures** | [**List[DocumentSignature]**](DocumentSignature.md) | One entry per signature, excluding document timestamps. | [optional] 

## Example

```python
from pdf_generator_api_client.models.document_signatures import DocumentSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSignatures from a JSON string
document_signatures_instance = DocumentSignatures.from_json(json)
# print the JSON string representation of the object
print(DocumentSignatures.to_json())

# convert the object into a dict
document_signatures_dict = document_signatures_instance.to_dict()
# create an instance of DocumentSignatures from a dict
document_signatures_from_dict = DocumentSignatures.from_dict(document_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


