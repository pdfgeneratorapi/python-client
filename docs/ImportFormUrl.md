# ImportFormUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | PDF file from remote URL to import | 
**form** | [**FormConfigurationNew**](FormConfigurationNew.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.import_form_url import ImportFormUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ImportFormUrl from a JSON string
import_form_url_instance = ImportFormUrl.from_json(json)
# print the JSON string representation of the object
print(ImportFormUrl.to_json())

# convert the object into a dict
import_form_url_dict = import_form_url_instance.to_dict()
# create an instance of ImportFormUrl from a dict
import_form_url_from_dict = ImportFormUrl.from_dict(import_form_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


