# ImportTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**ImportTemplateUrlTemplate**](ImportTemplateUrlTemplate.md) |  | 
**file_url** | **str** | PDF file from remote URL to import | 
**file_base64** | **str** | PDF file from base64 string to import | 

## Example

```python
from pdf_generator_api_client.models.import_template_request import ImportTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTemplateRequest from a JSON string
import_template_request_instance = ImportTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ImportTemplateRequest.to_json())

# convert the object into a dict
import_template_request_dict = import_template_request_instance.to_dict()
# create an instance of ImportTemplateRequest from a dict
import_template_request_from_dict = ImportTemplateRequest.from_dict(import_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


