# MetadataParam

Metadata object (optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | Document author | [optional] [default to 'Organization name']
**language** | **str** | Document language | [optional] [default to 'en']

## Example

```python
from pdf_generator_api_client.models.metadata_param import MetadataParam

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataParam from a JSON string
metadata_param_instance = MetadataParam.from_json(json)
# print the JSON string representation of the object
print(MetadataParam.to_json())

# convert the object into a dict
metadata_param_dict = metadata_param_instance.to_dict()
# create an instance of MetadataParam from a dict
metadata_param_from_dict = MetadataParam.from_dict(metadata_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


