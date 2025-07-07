# pdf_generator_api_client.ServicesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_watermark**](ServicesApi.md#add_watermark) | **POST** /pdfservices/watermark | Add watermark
[**decrypt_document**](ServicesApi.md#decrypt_document) | **POST** /pdfservices/decrypt | Decrypt document
[**encrypt_document**](ServicesApi.md#encrypt_document) | **POST** /pdfservices/encrypt | Encrypt document
[**extract_form_fields**](ServicesApi.md#extract_form_fields) | **POST** /pdfservices/form/fields | Extract form fields
[**fill_form_fields**](ServicesApi.md#fill_form_fields) | **POST** /pdfservices/form/fill | Fill form fields
[**optimize_document**](ServicesApi.md#optimize_document) | **POST** /pdfservices/optimize | Optimize document


# **add_watermark**
> AddWatermark201Response add_watermark(add_watermark_request)

Add watermark

Adds a text or an image watermark to PDF document from base64 string or a remote URL.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.add_watermark_request import AddWatermarkRequest
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
    api_instance = pdf_generator_api_client.ServicesApi(api_client)
    add_watermark_request = pdf_generator_api_client.AddWatermarkRequest() # AddWatermarkRequest | 

    try:
        # Add watermark
        api_response = api_instance.add_watermark(add_watermark_request)
        print("The response of ServicesApi->add_watermark:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->add_watermark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_watermark_request** | [**AddWatermarkRequest**](AddWatermarkRequest.md)|  | 

### Return type

[**AddWatermark201Response**](AddWatermark201Response.md)

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

# **decrypt_document**
> AddWatermark201Response decrypt_document(encrypt_document_request)

Decrypt document

Decrypts an encrypted PDF document from base64 string or a remote URL.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.encrypt_document_request import EncryptDocumentRequest
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
    api_instance = pdf_generator_api_client.ServicesApi(api_client)
    encrypt_document_request = pdf_generator_api_client.EncryptDocumentRequest() # EncryptDocumentRequest | 

    try:
        # Decrypt document
        api_response = api_instance.decrypt_document(encrypt_document_request)
        print("The response of ServicesApi->decrypt_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->decrypt_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypt_document_request** | [**EncryptDocumentRequest**](EncryptDocumentRequest.md)|  | 

### Return type

[**AddWatermark201Response**](AddWatermark201Response.md)

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

# **encrypt_document**
> AddWatermark201Response encrypt_document(encrypt_document_request)

Encrypt document

Encrypts a PDF document from base64 string or a remote URL.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.encrypt_document_request import EncryptDocumentRequest
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
    api_instance = pdf_generator_api_client.ServicesApi(api_client)
    encrypt_document_request = pdf_generator_api_client.EncryptDocumentRequest() # EncryptDocumentRequest | 

    try:
        # Encrypt document
        api_response = api_instance.encrypt_document(encrypt_document_request)
        print("The response of ServicesApi->encrypt_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->encrypt_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypt_document_request** | [**EncryptDocumentRequest**](EncryptDocumentRequest.md)|  | 

### Return type

[**AddWatermark201Response**](AddWatermark201Response.md)

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

# **extract_form_fields**
> ExtractFormFields200Response extract_form_fields(extract_form_fields_request)

Extract form fields

Extracts form fields and their metadata from a PDF document using base64 string or a remote URL.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.extract_form_fields200_response import ExtractFormFields200Response
from pdf_generator_api_client.models.extract_form_fields_request import ExtractFormFieldsRequest
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
    api_instance = pdf_generator_api_client.ServicesApi(api_client)
    extract_form_fields_request = pdf_generator_api_client.ExtractFormFieldsRequest() # ExtractFormFieldsRequest | 

    try:
        # Extract form fields
        api_response = api_instance.extract_form_fields(extract_form_fields_request)
        print("The response of ServicesApi->extract_form_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->extract_form_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_form_fields_request** | [**ExtractFormFieldsRequest**](ExtractFormFieldsRequest.md)|  | 

### Return type

[**ExtractFormFields200Response**](ExtractFormFields200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form fields data |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_form_fields**
> AddWatermark201Response fill_form_fields(fill_form_fields_request)

Fill form fields

Fills form fields in a PDF document with provided data from base64 string or a remote URL.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.fill_form_fields_request import FillFormFieldsRequest
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
    api_instance = pdf_generator_api_client.ServicesApi(api_client)
    fill_form_fields_request = pdf_generator_api_client.FillFormFieldsRequest() # FillFormFieldsRequest | 

    try:
        # Fill form fields
        api_response = api_instance.fill_form_fields(fill_form_fields_request)
        print("The response of ServicesApi->fill_form_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->fill_form_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fill_form_fields_request** | [**FillFormFieldsRequest**](FillFormFieldsRequest.md)|  | 

### Return type

[**AddWatermark201Response**](AddWatermark201Response.md)

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

# **optimize_document**
> OptimizeDocument201Response optimize_document(optimize_document_request)

Optimize document

Optimizes the size of a PDF document from base64 string or a remote URL.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.optimize_document201_response import OptimizeDocument201Response
from pdf_generator_api_client.models.optimize_document_request import OptimizeDocumentRequest
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
    api_instance = pdf_generator_api_client.ServicesApi(api_client)
    optimize_document_request = pdf_generator_api_client.OptimizeDocumentRequest() # OptimizeDocumentRequest | 

    try:
        # Optimize document
        api_response = api_instance.optimize_document(optimize_document_request)
        print("The response of ServicesApi->optimize_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->optimize_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optimize_document_request** | [**OptimizeDocumentRequest**](OptimizeDocumentRequest.md)|  | 

### Return type

[**OptimizeDocument201Response**](OptimizeDocument201Response.md)

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

