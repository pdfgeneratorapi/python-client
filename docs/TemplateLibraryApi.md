# pdf_generator_api_client.TemplateLibraryApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template_library**](TemplateLibraryApi.md#get_template_library) | **GET** /templates/library | Get template library
[**get_template_library_item**](TemplateLibraryApi.md#get_template_library_item) | **GET** /templates/library/{publicId} | Open template from the library


# **get_template_library**
> GetTemplateLibrary200Response get_template_library(tags=tags)

Get template library

Returns a list of publicly available templates from the template library.


### Example


```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_template_library200_response import GetTemplateLibrary200Response
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v4"
)


# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplateLibraryApi(api_client)
    tags = 'tags_example' # str | Filter template by tags (optional)

    try:
        # Get template library
        api_response = api_instance.get_template_library(tags=tags)
        print("The response of TemplateLibraryApi->get_template_library:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateLibraryApi->get_template_library: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Filter template by tags | [optional] 

### Return type

[**GetTemplateLibrary200Response**](GetTemplateLibrary200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of public templates |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_library_item**
> InlineObject16 get_template_library_item(public_id)

Open template from the library

Returns the template definition for a public template identified by its `public_id`.


### Example


```python
import pdf_generator_api_client
from pdf_generator_api_client.models.inline_object16 import InlineObject16
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v4"
)


# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplateLibraryApi(api_client)
    public_id = 'bac8381bce1982e5f6957a0f52371336' # str | Resource public id

    try:
        # Open template from the library
        api_response = api_instance.get_template_library_item(public_id)
        print("The response of TemplateLibraryApi->get_template_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateLibraryApi->get_template_library_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**| Resource public id | 

### Return type

[**InlineObject16**](InlineObject16.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

