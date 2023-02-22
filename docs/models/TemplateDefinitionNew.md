# pdf_generator_api_client.model.template_definition_new.TemplateDefinitionNew

Template configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Template configuration | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Template name | 
**[tags](#tags)** | list, tuple,  | tuple,  | A list of tags assigned to a template | [optional] 
**isDraft** | bool,  | BoolClass,  | Indicates if the template is a draft or published. | [optional] 
**[layout](#layout)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines template layout (e.g page format, margins). | [optional] 
**[pages](#pages)** | list, tuple,  | tuple,  | Defines page or label size, margins and components on page or label | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

A list of tags assigned to a template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of tags assigned to a template | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# layout

Defines template layout (e.g page format, margins).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines template layout (e.g page format, margins). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**format** | str,  | str,  | Defines template page size | [optional] must be one of ["A4", "letter", "custom", ] 
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page width in units | [optional] 
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page height in units | [optional] 
**unit** | str,  | str,  | Measure unit | [optional] must be one of ["cm", "in", ] 
**orientation** | str,  | str,  | Page orientation | [optional] must be one of ["portrait", "landscape", ] 
**rotaion** | decimal.Decimal, int,  | decimal.Decimal,  | Page rotation in degrees | [optional] must be one of [0, 90, 180, 270, ] 
**[margins](#margins)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Page margins in units | [optional] 
**[repeatLayout](#repeatLayout)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Defines page size if layout is repeated on the page e.g sheet labels | [optional] 
**emptyLabels** | decimal.Decimal, int,  | decimal.Decimal,  | Defines how many pages or labels should be empty | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# margins

Page margins in units

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Page margins in units | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**top** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**right** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**bottom** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**left** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# repeatLayout

Defines page size if layout is repeated on the page e.g sheet labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Defines page size if layout is repeated on the page e.g sheet labels | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**format** | str,  | str,  | Defines template page size | [optional] must be one of ["A4", "letter", "custom", ] 
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page width in units | [optional] 
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page height in units | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pages

Defines page or label size, margins and components on page or label

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Defines page or label size, margins and components on page or label | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page width in units | [optional] 
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page height in units | [optional] 
**[margins](#margins)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[components](#components)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# margins

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**right** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page or label margin from right | [optional] 
**bottom** | decimal.Decimal, int, float,  | decimal.Decimal,  | Page or label margin from bottom | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# components

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Component**](Component.md) | [**Component**](Component.md) | [**Component**](Component.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

