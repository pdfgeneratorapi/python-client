# GenerateDocument201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** | Base64 encoded document if the output&#x3D;base64 is used or URL to the document when the output&#x3D;url is used. | [optional] 
**meta** | [**GenerateDocument201ResponseMeta**](GenerateDocument201ResponseMeta.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.generate_document201_response import GenerateDocument201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocument201Response from a JSON string
generate_document201_response_instance = GenerateDocument201Response.from_json(json)
# print the JSON string representation of the object
print(GenerateDocument201Response.to_json())

# convert the object into a dict
generate_document201_response_dict = generate_document201_response_instance.to_dict()
# create an instance of GenerateDocument201Response from a dict
generate_document201_response_from_dict = GenerateDocument201Response.from_dict(generate_document201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


