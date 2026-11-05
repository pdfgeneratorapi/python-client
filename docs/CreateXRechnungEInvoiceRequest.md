# CreateXRechnungEInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | JSON payload that represents the Peppol BIS Billing 3.0 UBL Invoice (https://docs.peppol.eu/poacc/billing/3.0/) Use the Get schema endpoint to see the detailed payload structure. | 
**type** | **str** | Syntax of the XRechnung invoice. &#x60;CII&#x60; produces XRechnung CII; any other value produces XRechnung UBL. | [optional] [default to 'UBL']
**output** | **str** | Response format. When the \&quot;file\&quot; option is used the API returns the file inline. | [optional] [default to 'base64']

## Example

```python
from pdf_generator_api_client.models.create_x_rechnung_e_invoice_request import CreateXRechnungEInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateXRechnungEInvoiceRequest from a JSON string
create_x_rechnung_e_invoice_request_instance = CreateXRechnungEInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateXRechnungEInvoiceRequest.to_json())

# convert the object into a dict
create_x_rechnung_e_invoice_request_dict = create_x_rechnung_e_invoice_request_instance.to_dict()
# create an instance of CreateXRechnungEInvoiceRequest from a dict
create_x_rechnung_e_invoice_request_from_dict = CreateXRechnungEInvoiceRequest.from_dict(create_x_rechnung_e_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


