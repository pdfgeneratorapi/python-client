# TemplateVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**template_id** | **int** |  | [optional] 
**template_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**checksum** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**is_production** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_version import TemplateVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersion from a JSON string
template_version_instance = TemplateVersion.from_json(json)
# print the JSON string representation of the object
print(TemplateVersion.to_json())

# convert the object into a dict
template_version_dict = template_version_instance.to_dict()
# create an instance of TemplateVersion from a dict
template_version_from_dict = TemplateVersion.from_dict(template_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


