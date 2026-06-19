# ImportFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | PDF file from remote URL to import | 
**form** | [**FormConfigurationNew**](FormConfigurationNew.md) |  | [optional] 
**file_base64** | **str** | PDF file from base64 string to import | 

## Example

```python
from pdf_generator_api_client.models.import_form_request import ImportFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportFormRequest from a JSON string
import_form_request_instance = ImportFormRequest.from_json(json)
# print the JSON string representation of the object
print(ImportFormRequest.to_json())

# convert the object into a dict
import_form_request_dict = import_form_request_instance.to_dict()
# create an instance of ImportFormRequest from a dict
import_form_request_from_dict = ImportFormRequest.from_dict(import_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


