# OptimizeDocument201ResponseMetaStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_size** | **float** | Document original size | [optional] 
**optimized_size** | **float** | Document size after optimization | [optional] 

## Example

```python
from pdf_generator_api_client.models.optimize_document201_response_meta_stats import OptimizeDocument201ResponseMetaStats

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeDocument201ResponseMetaStats from a JSON string
optimize_document201_response_meta_stats_instance = OptimizeDocument201ResponseMetaStats.from_json(json)
# print the JSON string representation of the object
print(OptimizeDocument201ResponseMetaStats.to_json())

# convert the object into a dict
optimize_document201_response_meta_stats_dict = optimize_document201_response_meta_stats_instance.to_dict()
# create an instance of OptimizeDocument201ResponseMetaStats from a dict
optimize_document201_response_meta_stats_from_dict = OptimizeDocument201ResponseMetaStats.from_dict(optimize_document201_response_meta_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


