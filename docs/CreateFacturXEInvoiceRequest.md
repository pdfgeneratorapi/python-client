# CreateFacturXEInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**CreateFacturXEInvoiceRequestTemplate**](CreateFacturXEInvoiceRequestTemplate.md) |  | 
**profile** | **str** | Factur-X conformance level. | [optional] [default to 'basic']
**output** | [**OutputParam**](OutputParam.md) |  | [optional] [default to OutputParam.BASE64]
**name** | **str** | Generated document name (optional) | [optional] [default to '']
**metadata** | [**MetadataParam**](MetadataParam.md) |  | [optional] 

## Example

```python
from pdf_generator_api_client.models.create_factur_xe_invoice_request import CreateFacturXEInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFacturXEInvoiceRequest from a JSON string
create_factur_xe_invoice_request_instance = CreateFacturXEInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFacturXEInvoiceRequest.to_json())

# convert the object into a dict
create_factur_xe_invoice_request_dict = create_factur_xe_invoice_request_instance.to_dict()
# create an instance of CreateFacturXEInvoiceRequest from a dict
create_factur_xe_invoice_request_from_dict = CreateFacturXEInvoiceRequest.from_dict(create_factur_xe_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


