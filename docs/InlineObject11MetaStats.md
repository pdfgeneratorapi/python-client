# InlineObject11MetaStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **float** | Document original size in kilobytes | [optional] 
**optimized_size** | **float** | Document size after optimization in kilobytes | [optional] 
**unit** | **str** | Unit of the sizes | [optional] 

## Example

```python
from pdf_generator_api_client.models.inline_object11_meta_stats import InlineObject11MetaStats

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject11MetaStats from a JSON string
inline_object11_meta_stats_instance = InlineObject11MetaStats.from_json(json)
# print the JSON string representation of the object
print(InlineObject11MetaStats.to_json())

# convert the object into a dict
inline_object11_meta_stats_dict = inline_object11_meta_stats_instance.to_dict()
# create an instance of InlineObject11MetaStats from a dict
inline_object11_meta_stats_from_dict = InlineObject11MetaStats.from_dict(inline_object11_meta_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


