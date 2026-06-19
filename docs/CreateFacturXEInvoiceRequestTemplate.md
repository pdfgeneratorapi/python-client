# CreateFacturXEInvoiceRequestTemplate

Template id, version, version id and data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template ID | [optional] 
**version_id** | **int** | Template version ID | [optional] 
**data** | **object** | JSON payload that represents the Peppol BIS Billing 3.0 UBL Invoice (https://docs.peppol.eu/poacc/billing/3.0/) Use the Get schema endpoint to see the detailed payload structure. | [optional] 

## Example

```python
from pdf_generator_api_client.models.create_factur_xe_invoice_request_template import CreateFacturXEInvoiceRequestTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFacturXEInvoiceRequestTemplate from a JSON string
create_factur_xe_invoice_request_template_instance = CreateFacturXEInvoiceRequestTemplate.from_json(json)
# print the JSON string representation of the object
print(CreateFacturXEInvoiceRequestTemplate.to_json())

# convert the object into a dict
create_factur_xe_invoice_request_template_dict = create_factur_xe_invoice_request_template_instance.to_dict()
# create an instance of CreateFacturXEInvoiceRequestTemplate from a dict
create_factur_xe_invoice_request_template_from_dict = CreateFacturXEInvoiceRequestTemplate.from_dict(create_factur_xe_invoice_request_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


