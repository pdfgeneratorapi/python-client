# ImportFormBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_base64** | **str** | PDF file from base64 string to import | 
**form** | [**FormConfigurationNew**](FormConfigurationNew.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.import_form_base64 import ImportFormBase64

# TODO update the JSON string below
json = "{}"
# create an instance of ImportFormBase64 from a JSON string
import_form_base64_instance = ImportFormBase64.from_json(json)
# print the JSON string representation of the object
print(ImportFormBase64.to_json())

# convert the object into a dict
import_form_base64_dict = import_form_base64_instance.to_dict()
# create an instance of ImportFormBase64 from a dict
import_form_base64_from_dict = ImportFormBase64.from_dict(import_form_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


