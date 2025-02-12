# pdf_generator_api_client.FormsApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_from**](FormsApi.md#create_from) | **POST** /forms | Create form
[**delete_form**](FormsApi.md#delete_form) | **DELETE** /forms/{formId} | Delete form
[**get_form**](FormsApi.md#get_form) | **GET** /forms/{formId} | Get form
[**get_forms**](FormsApi.md#get_forms) | **GET** /forms | Get forms
[**share_form**](FormsApi.md#share_form) | **POST** /forms/{formId}/share | Share form
[**update_form**](FormsApi.md#update_form) | **PUT** /forms/{formId} | Update form


# **create_from**
> CreateFrom201Response create_from(form_configuration_new)

Create form

Creates a new form based on the configuration sent in the request body.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_from201_response import CreateFrom201Response
from pdf_generator_api_client.models.form_configuration_new import FormConfigurationNew
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
    api_instance = pdf_generator_api_client.FormsApi(api_client)
    form_configuration_new = pdf_generator_api_client.FormConfigurationNew() # FormConfigurationNew | Form configuration

    try:
        # Create form
        api_response = api_instance.create_from(form_configuration_new)
        print("The response of FormsApi->create_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->create_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_configuration_new** | [**FormConfigurationNew**](FormConfigurationNew.md)| Form configuration | 

### Return type

[**CreateFrom201Response**](CreateFrom201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Form configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form**
> delete_form(form_id)

Delete form

Deletes the form with specified id

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
    api_instance = pdf_generator_api_client.FormsApi(api_client)
    form_id = 1 # int | Form unique identifier

    try:
        # Delete form
        api_instance.delete_form(form_id)
    except Exception as e:
        print("Exception when calling FormsApi->delete_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_id** | **int**| Form unique identifier | 

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

# **get_form**
> CreateFrom201Response get_form(form_id)

Get form

Returns form configuration

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_from201_response import CreateFrom201Response
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
    api_instance = pdf_generator_api_client.FormsApi(api_client)
    form_id = 1 # int | Form unique identifier

    try:
        # Get form
        api_response = api_instance.get_form(form_id)
        print("The response of FormsApi->get_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_id** | **int**| Form unique identifier | 

### Return type

[**CreateFrom201Response**](CreateFrom201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms**
> GetForms200Response get_forms(page=page, per_page=per_page)

Get forms

Returns a list of forms available for the organization

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_forms200_response import GetForms200Response
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
    api_instance = pdf_generator_api_client.FormsApi(api_client)
    page = 1 # int | Pagination: page to return (optional) (default to 1)
    per_page = 15 # int | Pagination: How many records to return per page (optional) (default to 15)

    try:
        # Get forms
        api_response = api_instance.get_forms(page=page, per_page=per_page)
        print("The response of FormsApi->get_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_forms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Pagination: page to return | [optional] [default to 1]
 **per_page** | **int**| Pagination: How many records to return per page | [optional] [default to 15]

### Return type

[**GetForms200Response**](GetForms200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of form objects |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_form**
> ShareForm201Response share_form(form_id)

Share form

Creates an unique sharing URL to collect form data

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.share_form201_response import ShareForm201Response
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
    api_instance = pdf_generator_api_client.FormsApi(api_client)
    form_id = 1 # int | Form unique identifier

    try:
        # Share form
        api_response = api_instance.share_form(form_id)
        print("The response of FormsApi->share_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->share_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_id** | **int**| Form unique identifier | 

### Return type

[**ShareForm201Response**](ShareForm201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Form sharing URL |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form**
> CreateFrom201Response update_form(form_id, form_configuration_new)

Update form

Updates the form configuration. The form configuration must be complete as the entire configuration is replaced and not merged.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_from201_response import CreateFrom201Response
from pdf_generator_api_client.models.form_configuration_new import FormConfigurationNew
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
    api_instance = pdf_generator_api_client.FormsApi(api_client)
    form_id = 1 # int | Form unique identifier
    form_configuration_new = pdf_generator_api_client.FormConfigurationNew() # FormConfigurationNew | Form configuration

    try:
        # Update form
        api_response = api_instance.update_form(form_id, form_configuration_new)
        print("The response of FormsApi->update_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->update_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_id** | **int**| Form unique identifier | 
 **form_configuration_new** | [**FormConfigurationNew**](FormConfigurationNew.md)| Form configuration | 

### Return type

[**CreateFrom201Response**](CreateFrom201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

