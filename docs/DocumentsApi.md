# pdf_generator_api_client.DocumentsApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents/{publicId} | Delete document
[**generate_document**](DocumentsApi.md#generate_document) | **POST** /documents/generate | Generate document
[**generate_document_asynchronous**](DocumentsApi.md#generate_document_asynchronous) | **POST** /documents/generate/async | Generate document (async)
[**generate_document_batch**](DocumentsApi.md#generate_document_batch) | **POST** /documents/generate/batch | Generate document (batch)
[**generate_document_batch_asynchronous**](DocumentsApi.md#generate_document_batch_asynchronous) | **POST** /documents/generate/batch/async | Generate document (batch + async)
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents/{publicId} | Get document
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /documents | Get documents


# **delete_document**
> delete_document(public_id)

Delete document

Delete document from the Document Storage

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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    public_id = 'bac8381bce1982e5f6957a0f52371336' # str | Resource public id

    try:
        # Delete document
        api_instance.delete_document(public_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| Resource public id | 

### Return type

void (empty response body)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_document**
> GenerateDocument201Response generate_document(generate_document_request)

Generate document

Merges template with data and returns base64 encoded document or a public URL to a document. NB! When the public URL option is used, the document is stored for 30 days and automatically deleted.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.generate_document201_response import GenerateDocument201Response
from pdf_generator_api_client.models.generate_document_request import GenerateDocumentRequest
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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    generate_document_request = pdf_generator_api_client.GenerateDocumentRequest() # GenerateDocumentRequest | Request parameters, including template id, data and formats.

    try:
        # Generate document
        api_response = api_instance.generate_document(generate_document_request)
        print("The response of DocumentsApi->generate_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->generate_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_document_request** | [**GenerateDocumentRequest**](GenerateDocumentRequest.md)| Request parameters, including template id, data and formats. | 

### Return type

[**GenerateDocument201Response**](GenerateDocument201Response.md)

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

# **generate_document_asynchronous**
> GenerateDocumentAsynchronous201Response generate_document_asynchronous(generate_document_asynchronous_request)

Generate document (async)

Merges template with data as asynchronous job and makes POST request to callback URL defined in the request. Request uses the same format as response of synchronous generation endpoint. The job id is also added to the callback request as header PDF-API-Job-Id  *Example payload for callback URL:* ``` {   \"response\": \"https://us1.pdfgeneratorapi.com/share/12821/VBERi0xLjcKJeLjz9MKNyAwIG9i\",   \"meta\": {     \"name\": \"a2bd25b8921f3dc7a440fd7f427f90a4.pdf\",     \"display_name\": \"a2bd25b8921f3dc7a440fd7f427f90a4\",     \"encoding\": \"binary\",     \"content-type\": \"application/pdf\"   } } ``` 

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.generate_document_asynchronous201_response import GenerateDocumentAsynchronous201Response
from pdf_generator_api_client.models.generate_document_asynchronous_request import GenerateDocumentAsynchronousRequest
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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    generate_document_asynchronous_request = pdf_generator_api_client.GenerateDocumentAsynchronousRequest() # GenerateDocumentAsynchronousRequest | Request parameters, including template id, data and formats.

    try:
        # Generate document (async)
        api_response = api_instance.generate_document_asynchronous(generate_document_asynchronous_request)
        print("The response of DocumentsApi->generate_document_asynchronous:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->generate_document_asynchronous: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_document_asynchronous_request** | [**GenerateDocumentAsynchronousRequest**](GenerateDocumentAsynchronousRequest.md)| Request parameters, including template id, data and formats. | 

### Return type

[**GenerateDocumentAsynchronous201Response**](GenerateDocumentAsynchronous201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Async job response |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_document_batch**
> GenerateDocument201Response generate_document_batch(generate_document_batch_request)

Generate document (batch)

Allows to merge multiple templates with data and returns base64 encoded document or public URL to a document. NB! When the public URL option is used, the document is stored for 30 days and automatically deleted.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.generate_document201_response import GenerateDocument201Response
from pdf_generator_api_client.models.generate_document_batch_request import GenerateDocumentBatchRequest
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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    generate_document_batch_request = pdf_generator_api_client.GenerateDocumentBatchRequest() # GenerateDocumentBatchRequest | Request parameters, including template id, data and formats.

    try:
        # Generate document (batch)
        api_response = api_instance.generate_document_batch(generate_document_batch_request)
        print("The response of DocumentsApi->generate_document_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->generate_document_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_document_batch_request** | [**GenerateDocumentBatchRequest**](GenerateDocumentBatchRequest.md)| Request parameters, including template id, data and formats. | 

### Return type

[**GenerateDocument201Response**](GenerateDocument201Response.md)

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

# **generate_document_batch_asynchronous**
> GenerateDocumentAsynchronous201Response generate_document_batch_asynchronous(generate_document_batch_asynchronous_request)

Generate document (batch + async)

Merges template with data as asynchronous job and makes POST request to callback URL defined in the request. Request uses the same format as response of synchronous generation endpoint. The job id is also added to the callback request as header PDF-API-Job-Id  *Example payload for callback URL:* ``` {   \"response\": \"https://us1.pdfgeneratorapi.com/share/12821/VBERi0xLjcKJeLjz9MKNyAwIG9i\",   \"meta\": {     \"name\": \"a2bd25b8921f3dc7a440fd7f427f90a4.pdf\",     \"display_name\": \"a2bd25b8921f3dc7a440fd7f427f90a4\",     \"encoding\": \"binary\",     \"content-type\": \"application/pdf\"   } } ``` 

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.generate_document_asynchronous201_response import GenerateDocumentAsynchronous201Response
from pdf_generator_api_client.models.generate_document_batch_asynchronous_request import GenerateDocumentBatchAsynchronousRequest
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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    generate_document_batch_asynchronous_request = pdf_generator_api_client.GenerateDocumentBatchAsynchronousRequest() # GenerateDocumentBatchAsynchronousRequest | Request parameters, including template id, data and formats.

    try:
        # Generate document (batch + async)
        api_response = api_instance.generate_document_batch_asynchronous(generate_document_batch_asynchronous_request)
        print("The response of DocumentsApi->generate_document_batch_asynchronous:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->generate_document_batch_asynchronous: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_document_batch_asynchronous_request** | [**GenerateDocumentBatchAsynchronousRequest**](GenerateDocumentBatchAsynchronousRequest.md)| Request parameters, including template id, data and formats. | 

### Return type

[**GenerateDocumentAsynchronous201Response**](GenerateDocumentAsynchronous201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Async job response |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> GetDocument200Response get_document(public_id)

Get document

Returns document stored in the Document Storage

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_document200_response import GetDocument200Response
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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    public_id = 'bac8381bce1982e5f6957a0f52371336' # str | Resource public id

    try:
        # Get document
        api_response = api_instance.get_document(public_id)
        print("The response of DocumentsApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| Resource public id | 

### Return type

[**GetDocument200Response**](GetDocument200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document data |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> GetDocuments200Response get_documents(template_id=template_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)

Get documents

Returns a list of generated documents created by authorized workspace and stored in PDF Generator API. If master user is specified as workspace in JWT then all documents created in the organization are returned. NB! This endpoint returns only documents generated using the output=url option.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_documents200_response import GetDocuments200Response
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
    api_instance = pdf_generator_api_client.DocumentsApi(api_client)
    template_id = 19375 # int | Template unique identifier (optional)
    start_date = '2022-08-01 12:00:00' # str | Start date. Format: Y-m-d H:i:s (optional)
    end_date = '2022-08-05 12:00:00' # str | End date. Format: Y-m-d H:i:s. Defaults to current timestamp (optional)
    page = 1 # int | Pagination: page to return (optional) (default to 1)
    per_page = 15 # int | Pagination: How many records to return per page (optional) (default to 15)

    try:
        # Get documents
        api_response = api_instance.get_documents(template_id=template_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)
        print("The response of DocumentsApi->get_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | [optional] 
 **start_date** | **str**| Start date. Format: Y-m-d H:i:s | [optional] 
 **end_date** | **str**| End date. Format: Y-m-d H:i:s. Defaults to current timestamp | [optional] 
 **page** | **int**| Pagination: page to return | [optional] [default to 1]
 **per_page** | **int**| Pagination: How many records to return per page | [optional] [default to 15]

### Return type

[**GetDocuments200Response**](GetDocuments200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of generated documents |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

