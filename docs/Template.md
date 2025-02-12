# Template

Template object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**name** | **str** | Template name | [optional] 
**owner** | **bool** | Indicates if the workspace is the owner of the template | [optional] 
**created_at** | **str** | Timestamp when the template was created | [optional] 
**updated_at** | **str** | Timestamp when the template was updated | [optional] 
**tags** | **List[str]** | A list of tags assigned to a template | [optional] 

## Example

```python
from pdf_generator_api_client.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


