# pdf_generator_api_client.model.document.Document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**public_id** | str,  | str,  | Document unique identifier | [optional] 
**public_url** | str,  | str,  | Public URL of the document | [optional] 
**template_id** | decimal.Decimal, int,  | decimal.Decimal,  | Template used to generate the document | [optional] 
**created_at** | str,  | str,  | Date time when the document was generated | [optional] 
**expires_at** | str,  | str,  | Date time when the document url will expire. Document is stored for 30 days. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

