# ImportTemplateUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**ImportTemplateUrlTemplate**](ImportTemplateUrlTemplate.md) |  | 
**file_url** | **str** | PDF file from remote URL to import | 

## Example

```python
from pdf_generator_api_client.models.import_template_url import ImportTemplateUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTemplateUrl from a JSON string
import_template_url_instance = ImportTemplateUrl.from_json(json)
# print the JSON string representation of the object
print(ImportTemplateUrl.to_json())

# convert the object into a dict
import_template_url_dict = import_template_url_instance.to_dict()
# create an instance of ImportTemplateUrl from a dict
import_template_url_from_dict = ImportTemplateUrl.from_dict(import_template_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


