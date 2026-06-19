# PublicTemplateLibraryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique public identifier of the template | [optional] 
**name** | **str** | Template name | [optional] 
**tags** | **List[str]** | A list of tags assigned to a public template | [optional] 
**preview_image_url** | **str** | URL to the template preview image | [optional] 
**sample_data_url** | **str** | URL to the template sample data | [optional] 

## Example

```python
from pdf_generator_api_client.models.public_template_library_item import PublicTemplateLibraryItem

# TODO update the JSON string below
json = "{}"
# create an instance of PublicTemplateLibraryItem from a JSON string
public_template_library_item_instance = PublicTemplateLibraryItem.from_json(json)
# print the JSON string representation of the object
print(PublicTemplateLibraryItem.to_json())

# convert the object into a dict
public_template_library_item_dict = public_template_library_item_instance.to_dict()
# create an instance of PublicTemplateLibraryItem from a dict
public_template_library_item_from_dict = PublicTemplateLibraryItem.from_dict(public_template_library_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


