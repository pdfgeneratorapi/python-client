# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** | Document unique identifier | [optional] 
**public_url** | **str** | Public URL of the document | [optional] 
**template_id** | **int** | Template used to generate the document | [optional] 
**created_at** | **str** | Date time when the document was generated | [optional] 
**expires_at** | **str** | Date time when the document url will expire. Document is stored for 30 days. | [optional] 

## Example

```python
from pdf_generator_api_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


