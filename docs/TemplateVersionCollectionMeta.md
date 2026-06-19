# TemplateVersionCollectionMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_version_collection_meta import TemplateVersionCollectionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionCollectionMeta from a JSON string
template_version_collection_meta_instance = TemplateVersionCollectionMeta.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionCollectionMeta.to_json())

# convert the object into a dict
template_version_collection_meta_dict = template_version_collection_meta_instance.to_dict()
# create an instance of TemplateVersionCollectionMeta from a dict
template_version_collection_meta_from_dict = TemplateVersionCollectionMeta.from_dict(template_version_collection_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


