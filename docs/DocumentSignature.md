# DocumentSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Name of the signature field in the document. | [optional] 
**signer_name** | **str** | The name the signer signed under. | [optional] 
**signer** | **str** | Subject of the certificate that sealed it — an organization, not a person. | [optional] 
**issuer** | **str** | Subject of the certificate authority that issued it. | [optional] 
**signed_at** | **str** | When a timestamp authority attested the signature (ISO-8601). This is the defensible time; the signer&#39;s own clock proves nothing.  | [optional] 
**claimed_signed_at** | **str** | The time the signer&#39;s own software recorded (ISO-8601). | [optional] 
**timestamp_authority** | **str** | The timestamp authority that attested the signature. | [optional] 
**intact** | **bool** | The bytes this signature covers are unchanged. | [optional] 
**valid** | **bool** | The signature block itself adds up. On its own this does NOT mean the document is unchanged: a tampered file reports &#x60;valid&#x60; true with &#x60;intact&#x60; false, so a verdict needs intact AND valid AND trusted.  | [optional] 
**trusted** | **bool** | The certificate chains to a trusted root. | [optional] 
**coverage** | **str** | How much of the file this signature protects. | [optional] 
**ades_indication** | **str** | The ETSI EN 319 102-1 indication, when the AdES engine could run. | [optional] 
**ades_sub_indication** | **str** | The AdES sub-indication, naming why an indication is not PASSED. | [optional] 

## Example

```python
from pdf_generator_api_client.models.document_signature import DocumentSignature

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSignature from a JSON string
document_signature_instance = DocumentSignature.from_json(json)
# print the JSON string representation of the object
print(DocumentSignature.to_json())

# convert the object into a dict
document_signature_dict = document_signature_instance.to_dict()
# create an instance of DocumentSignature from a dict
document_signature_from_dict = DocumentSignature.from_dict(document_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


