# PromoteTemplateVersion200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TemplateVersion**](TemplateVersion.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.promote_template_version200_response import PromoteTemplateVersion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteTemplateVersion200Response from a JSON string
promote_template_version200_response_instance = PromoteTemplateVersion200Response.from_json(json)
# print the JSON string representation of the object
print(PromoteTemplateVersion200Response.to_json())

# convert the object into a dict
promote_template_version200_response_dict = promote_template_version200_response_instance.to_dict()
# create an instance of PromoteTemplateVersion200Response from a dict
promote_template_version200_response_from_dict = PromoteTemplateVersion200Response.from_dict(promote_template_version200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


