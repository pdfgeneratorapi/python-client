# DataBatchInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **int** | Template id | [optional] 
**data** | **object** | JSON data used to replace data fields in the template | [optional] 

## Example

```python
from pdf_generator_api_client.models.data_batch_inner import DataBatchInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataBatchInner from a JSON string
data_batch_inner_instance = DataBatchInner.from_json(json)
# print the JSON string representation of the object
print(DataBatchInner.to_json())

# convert the object into a dict
data_batch_inner_dict = data_batch_inner_instance.to_dict()
# create an instance of DataBatchInner from a dict
data_batch_inner_from_dict = DataBatchInner.from_dict(data_batch_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


