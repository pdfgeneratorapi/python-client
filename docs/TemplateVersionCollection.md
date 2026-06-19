# TemplateVersionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[TemplateVersion]**](TemplateVersion.md) |  | [optional] 
**meta** | [**TemplateVersionCollectionMeta**](TemplateVersionCollectionMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.template_version_collection import TemplateVersionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionCollection from a JSON string
template_version_collection_instance = TemplateVersionCollection.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionCollection.to_json())

# convert the object into a dict
template_version_collection_dict = template_version_collection_instance.to_dict()
# create an instance of TemplateVersionCollection from a dict
template_version_collection_from_dict = TemplateVersionCollection.from_dict(template_version_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


