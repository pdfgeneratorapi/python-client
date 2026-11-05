# AttachmentsParamInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name, must end with &#x60;.pdf&#x60; or &#x60;.xml&#x60; | 
**content** | **bytearray** | Base64 encoded file content | 

## Example

```python
from pdf_generator_api_client.models.attachments_param_inner import AttachmentsParamInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsParamInner from a JSON string
attachments_param_inner_instance = AttachmentsParamInner.from_json(json)
# print the JSON string representation of the object
print(AttachmentsParamInner.to_json())

# convert the object into a dict
attachments_param_inner_dict = attachments_param_inner_instance.to_dict()
# create an instance of AttachmentsParamInner from a dict
attachments_param_inner_from_dict = AttachmentsParamInner.from_dict(attachments_param_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


