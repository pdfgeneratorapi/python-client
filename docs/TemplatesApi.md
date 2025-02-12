# pdf_generator_api_client.TemplatesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_template**](TemplatesApi.md#copy_template) | **POST** /templates/{templateId}/copy | Copy template
[**create_template**](TemplatesApi.md#create_template) | **POST** /templates | Create template
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /templates/{templateId} | Delete template
[**get_template**](TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Get template
[**get_template_data**](TemplatesApi.md#get_template_data) | **GET** /templates/{templateId}/data | Get template data fields
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /templates | Get templates
[**open_editor**](TemplatesApi.md#open_editor) | **POST** /templates/{templateId}/editor | Open editor
[**update_template**](TemplatesApi.md#update_template) | **PUT** /templates/{templateId} | Update template


# **copy_template**
> CreateTemplate201Response copy_template(template_id, copy_template_request=copy_template_request)

Copy template

Creates a copy of a template to the workspace specified in authentication parameters.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.copy_template_request import CopyTemplateRequest
from pdf_generator_api_client.models.create_template201_response import CreateTemplate201Response
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
    copy_template_request = pdf_generator_api_client.CopyTemplateRequest() # CopyTemplateRequest |  (optional)

    try:
        # Copy template
        api_response = api_instance.copy_template(template_id, copy_template_request=copy_template_request)
        print("The response of TemplatesApi->copy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->copy_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 
 **copy_template_request** | [**CopyTemplateRequest**](CopyTemplateRequest.md)|  | [optional] 

### Return type

[**CreateTemplate201Response**](CreateTemplate201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> CreateTemplate201Response create_template(template_definition_new)

Create template

Creates a new template. If template configuration is not specified in the request body then an empty template is created. Template is placed to the workspace specified in authentication params. Template configuration must be sent in the request body.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_template201_response import CreateTemplate201Response
from pdf_generator_api_client.models.template_definition_new import TemplateDefinitionNew
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_definition_new = pdf_generator_api_client.TemplateDefinitionNew() # TemplateDefinitionNew | Template configuration

    try:
        # Create template
        api_response = api_instance.create_template(template_definition_new)
        print("The response of TemplatesApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_definition_new** | [**TemplateDefinitionNew**](TemplateDefinitionNew.md)| Template configuration | 

### Return type

[**CreateTemplate201Response**](CreateTemplate201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(template_id)

Delete template

Deletes the template from workspace

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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    try:
        # Delete template
        api_instance.delete_template(template_id)
    except Exception as e:
        print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 

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

# **get_template**
> CreateTemplate201Response get_template(template_id)

Get template

Returns template configuration

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_template201_response import CreateTemplate201Response
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    try:
        # Get template
        api_response = api_instance.get_template(template_id)
        print("The response of TemplatesApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 

### Return type

[**CreateTemplate201Response**](CreateTemplate201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_data**
> GetTemplateData200Response get_template_data(template_id)

Get template data fields

Returns all data fields used in the template. Returns structured JSON data that can be used to check which data fields are used in template or autogenerate sample data. 

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_template_data200_response import GetTemplateData200Response
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    try:
        # Get template data fields
        api_response = api_instance.get_template_data(template_id)
        print("The response of TemplatesApi->get_template_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_template_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 

### Return type

[**GetTemplateData200Response**](GetTemplateData200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template data structure |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> GetTemplates200Response get_templates(name=name, tags=tags, access=access, page=page, per_page=per_page)

Get templates

Returns a list of templates available for the authenticated workspace

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_templates200_response import GetTemplates200Response
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    name = 'name_example' # str | Filter template by name (optional)
    tags = 'tags_example' # str | Filter template by tags (optional)
    access =  # str | Filter template by access type. No values returns all templates. private - returns only private templates, organization - returns only organization templates. (optional) (default to )
    page = 1 # int | Pagination: page to return (optional) (default to 1)
    per_page = 15 # int | Pagination: How many records to return per page (optional) (default to 15)

    try:
        # Get templates
        api_response = api_instance.get_templates(name=name, tags=tags, access=access, page=page, per_page=per_page)
        print("The response of TemplatesApi->get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter template by name | [optional] 
 **tags** | **str**| Filter template by tags | [optional] 
 **access** | **str**| Filter template by access type. No values returns all templates. private - returns only private templates, organization - returns only organization templates. | [optional] [default to ]
 **page** | **int**| Pagination: page to return | [optional] [default to 1]
 **per_page** | **int**| Pagination: How many records to return per page | [optional] [default to 15]

### Return type

[**GetTemplates200Response**](GetTemplates200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of template objects |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_editor**
> OpenEditor200Response open_editor(template_id, open_editor_request)

Open editor

Returns an unique URL which you can use to redirect your user to the editor from your application or use the generated URL as iframe source to show the editor within your application. When using iframe, make sure that your browser allows third-party cookies. 

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.open_editor200_response import OpenEditor200Response
from pdf_generator_api_client.models.open_editor_request import OpenEditorRequest
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
    open_editor_request = pdf_generator_api_client.OpenEditorRequest() # OpenEditorRequest | 

    try:
        # Open editor
        api_response = api_instance.open_editor(template_id, open_editor_request)
        print("The response of TemplatesApi->open_editor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->open_editor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 
 **open_editor_request** | [**OpenEditorRequest**](OpenEditorRequest.md)|  | 

### Return type

[**OpenEditor200Response**](OpenEditor200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an URL which you can use to redirect your user to the editor or use as iframe source |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> CreateTemplate201Response update_template(template_id, template_definition_new)

Update template

Updates template configuration. The template configuration for pages and layout must be complete as the entire configuration is replaced and not merged.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.create_template201_response import CreateTemplate201Response
from pdf_generator_api_client.models.template_definition_new import TemplateDefinitionNew
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
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
    template_definition_new = pdf_generator_api_client.TemplateDefinitionNew() # TemplateDefinitionNew | Template configuration

    try:
        # Update template
        api_response = api_instance.update_template(template_id, template_definition_new)
        print("The response of TemplatesApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 
 **template_definition_new** | [**TemplateDefinitionNew**](TemplateDefinitionNew.md)| Template configuration | 

### Return type

[**CreateTemplate201Response**](CreateTemplate201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

