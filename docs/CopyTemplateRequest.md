# CopyTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the copied template. If name is not specified then the original name is used. | [optional] 

## Example

```python
from pdf_generator_api_client.models.copy_template_request import CopyTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyTemplateRequest from a JSON string
copy_template_request_instance = CopyTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CopyTemplateRequest.to_json())

# convert the object into a dict
copy_template_request_dict = copy_template_request_instance.to_dict()
# create an instance of CopyTemplateRequest from a dict
copy_template_request_from_dict = CopyTemplateRequest.from_dict(copy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


