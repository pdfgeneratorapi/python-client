# pdf_generator_api_client.model.component.Component

Template component definition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Template component definition | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cls** | str,  | str,  | Defines component class/type | [optional] must be one of ["labelComponent", "numberComponent", "textComponent", "imageComponent", "dateComponent", "hlineComponent", "vlineComponent", "tableComponent", "compositeComponent", "barcodeComponent", "qrcodeComponent", "chartComponent", "rectangleComponent", "headerComponent", "footerComponent", "checkboxComponent", "radioComponent", ] 
**id** | str,  | str,  | Component id | [optional] 
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | Width in units | [optional] 
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | Height in units | [optional] 
**top** | decimal.Decimal, int, float,  | decimal.Decimal,  | Position from the page top in units | [optional] 
**left** | decimal.Decimal, int, float,  | decimal.Decimal,  | Position from the page left in units | [optional] 
**zindex** | decimal.Decimal, int,  | decimal.Decimal,  | Defines the rendering order on page. Components with smaller zindex are rendered before | [optional] 
**value** | str,  | str,  | Component value | [optional] 
**dataIndex** | str,  | str,  | Defines data field for Table and Container components which are used to iterate over list of items | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

