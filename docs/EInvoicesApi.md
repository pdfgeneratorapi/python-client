# pdf_generator_api_client.EInvoicesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_e_invoice**](EInvoicesApi.md#create_e_invoice) | **POST** /einvoice | Create eInvoice
[**create_factur_xe_invoice**](EInvoicesApi.md#create_factur_xe_invoice) | **POST** /einvoice/facturx | Create Factur-X eInvoice
[**create_x_rechnung_e_invoice**](EInvoicesApi.md#create_x_rechnung_e_invoice) | **POST** /einvoice/xrechnung | Create XRechnung eInvoice
[**get_e_invoice_schema**](EInvoicesApi.md#get_e_invoice_schema) | **GET** /einvoice/schema | Get schema


# **create_e_invoice**
> InlineObject create_e_invoice(create_e_invoice_request)

Create eInvoice

This endpoint transforms a JSON payload into an XML-based e-invoice that is fully compliant with the European EN 16931 standard. The generated output can be formatted in either UBL (Universal Business Language) or CII (Cross-Industry Invoice) syntax, ensuring interoperability across B2B and B2G platforms. The JSON payload follows Peppol BIS Billing 3.0 UBL Invoice described here: https://docs.peppol.eu/poacc/billing/3.0/

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_e_invoice_request import CreateEInvoiceRequest
from pdf_generator_api_client.models.inline_object import InlineObject
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.EInvoicesApi(api_client)
    create_e_invoice_request = pdf_generator_api_client.CreateEInvoiceRequest() # CreateEInvoiceRequest | eInvoice conversion

    try:
        # Create eInvoice
        api_response = api_instance.create_e_invoice(create_e_invoice_request)
        print("The response of EInvoicesApi->create_e_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EInvoicesApi->create_e_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_e_invoice_request** | [**CreateEInvoiceRequest**](CreateEInvoiceRequest.md)| eInvoice conversion | 

### Return type

[**InlineObject**](InlineObject.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | XML-based e-invoice response |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_factur_xe_invoice**
> InlineObject9 create_factur_xe_invoice(create_factur_xe_invoice_request)

Create Factur-X eInvoice

This endpoint transforms a JSON payload a Factur-X e-invoice that is fully compliant with the European EN 16931 standard. The generated output is always a PDF document, embedding a structured CII (Cross-Industry Invoice) XML according to the Factur-X format into a human-readable invoice, ensuring interoperability across B2B and B2G platforms. The JSON payload follows Peppol BIS Billing 3.0 UBL Invoice described here: https://docs.peppol.eu/poacc/billing/3.0/

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_factur_xe_invoice_request import CreateFacturXEInvoiceRequest
from pdf_generator_api_client.models.inline_object9 import InlineObject9
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.EInvoicesApi(api_client)
    create_factur_xe_invoice_request = pdf_generator_api_client.CreateFacturXEInvoiceRequest() # CreateFacturXEInvoiceRequest | eInvoice conversion

    try:
        # Create Factur-X eInvoice
        api_response = api_instance.create_factur_xe_invoice(create_factur_xe_invoice_request)
        print("The response of EInvoicesApi->create_factur_xe_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EInvoicesApi->create_factur_xe_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_factur_xe_invoice_request** | [**CreateFacturXEInvoiceRequest**](CreateFacturXEInvoiceRequest.md)| eInvoice conversion | 

### Return type

[**InlineObject9**](InlineObject9.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document data |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_x_rechnung_e_invoice**
> InlineObject create_x_rechnung_e_invoice(create_e_invoice_request)

Create XRechnung eInvoice

This endpoint transforms a JSON payload into an XML-based XRechnung e-invoice that is fully compliant with the European EN 16931 standard. The generated output follows the XRechnung format and can be formatted in either UBL (Universal Business Language) or CII (Cross-Industry Invoice) syntax, ensuring interoperability across B2B and B2G platforms. The JSON payload follows Peppol BIS Billing 3.0 UBL Invoice described here: https://docs.peppol.eu/poacc/billing/3.0/

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_e_invoice_request import CreateEInvoiceRequest
from pdf_generator_api_client.models.inline_object import InlineObject
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.EInvoicesApi(api_client)
    create_e_invoice_request = pdf_generator_api_client.CreateEInvoiceRequest() # CreateEInvoiceRequest | eInvoice conversion

    try:
        # Create XRechnung eInvoice
        api_response = api_instance.create_x_rechnung_e_invoice(create_e_invoice_request)
        print("The response of EInvoicesApi->create_x_rechnung_e_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EInvoicesApi->create_x_rechnung_e_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_e_invoice_request** | [**CreateEInvoiceRequest**](CreateEInvoiceRequest.md)| eInvoice conversion | 

### Return type

[**InlineObject**](InlineObject.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | XML-based e-invoice response |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_e_invoice_schema**
> object get_e_invoice_schema()

Get schema

Returns e-invoice JSON schema which defines the structure of the e-invoice.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v4"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.EInvoicesApi(api_client)

    try:
        # Get schema
        api_response = api_instance.get_e_invoice_schema()
        print("The response of EInvoicesApi->get_e_invoice_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EInvoicesApi->get_e_invoice_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template JSON Schema |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

