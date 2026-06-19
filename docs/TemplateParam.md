# TemplateParam

Template id, version, version id and data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TemplateParamId**](TemplateParamId.md) |  | [optional] 
**version_id** | **int** | Template version ID | [optional] 
**data** | [**TemplateParamData**](TemplateParamData.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_param import TemplateParam

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateParam from a JSON string
template_param_instance = TemplateParam.from_json(json)
# print the JSON string representation of the object
print(TemplateParam.to_json())

# convert the object into a dict
template_param_dict = template_param_instance.to_dict()
# create an instance of TemplateParam from a dict
template_param_from_dict = TemplateParam.from_dict(template_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


