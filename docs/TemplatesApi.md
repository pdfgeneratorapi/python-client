# pdf_generator_api_client.TemplatesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_template**](TemplatesApi.md#copy_template) | **POST** /templates/templateId/copy | Copy template
[**create_template**](TemplatesApi.md#create_template) | **POST** /templates | Create template
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /templates/templateId | Delete template
[**get_editor_url**](TemplatesApi.md#get_editor_url) | **POST** /templates/templateId/editor | Open editor
[**get_template**](TemplatesApi.md#get_template) | **GET** /templates/templateId | Get template
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /templates | Get templates
[**update_template**](TemplatesApi.md#update_template) | **PUT** /templates/templateId | Update template


# **copy_template**
> InlineResponse2001 copy_template(template_id)

Copy template

Creates a copy of a template to the workspace specified in authentication parameters.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response2001 import InlineResponse2001
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
    name = "My copied template" # str | Name for the copied template. If name is not specified then the original name is used. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Copy template
        api_response = api_instance.copy_template(template_id)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->copy_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy template
        api_response = api_instance.copy_template(template_id, name=name)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->copy_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier |
 **name** | **str**| Name for the copied template. If name is not specified then the original name is used. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration as JSON object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> InlineResponse2001 create_template(template_definition_new)

Create template

Creates a new template. If template configuration is not specified in the request body then an empty template is created. Template is placed to the workspace specified in authentication params. Template configuration must be sent in the request body.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response2001 import InlineResponse2001
from pdf_generator_api_client.model.template_definition_new import TemplateDefinitionNew
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_definition_new = TemplateDefinitionNew(
        name="Invoice template",
        tags=["invoice","orders"],
        is_draft=True,
        layout=TemplateDefinitionNewLayout(
            format="A4",
            width=21,
            height=29.7,
            unit="cm",
            orientation="portrait",
            rotaion=0,
            margins=TemplateDefinitionNewLayoutMargins(
                top=0.5,
                right=0.5,
                bottom=0.5,
                left=0.5,
            ),
            repeat_layout=TemplateDefinitionNewLayoutRepeatLayout(
                format="A4",
                width=21,
                height=29.7,
            ),
            empty_labels=0,
        ),
        pages=[
            TemplateDefinitionNewPages(
                width=21,
                height=29.7,
                margins=TemplateDefinitionNewMargins(
                    right=0.5,
                    bottom=0.5,
                ),
                components=[
                    Component(
                        cls="labelComponent",
                        id="component-12313",
                        width=3.5,
                        height=1,
                        top=4.2,
                        left=2.5,
                        zindex=102,
                        value="${price}",
                        data_index="line_items",
                    ),
                ],
            ),
        ],
    ) # TemplateDefinitionNew | Template configuration as JSON string

    # example passing only required values which don't have defaults set
    try:
        # Create template
        api_response = api_instance.create_template(template_definition_new)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_definition_new** | [**TemplateDefinitionNew**](TemplateDefinitionNew.md)| Template configuration as JSON string |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration as JSON object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> InlineResponse2002 delete_template(template_id)

Delete template

Deletes the template from workspace

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response2002 import InlineResponse2002
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete template
        api_response = api_instance.delete_template(template_id)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successfully executed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editor_url**
> InlineResponse2003 get_editor_url(template_id, body)

Open editor

Returns an unique URL which you can use to redirect your user to the editor from your application or use the generated URL as iframe source to show the editor within your application. 

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response2003 import InlineResponse2003
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
    language = "en" # str | Specify the editor UI language. Defaults to organization editor language. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Open editor
        api_response = api_instance.get_editor_url(template_id, body)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_editor_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Open editor
        api_response = api_instance.get_editor_url(template_id, body, language=language)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_editor_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file. |
 **language** | **str**| Specify the editor UI language. Defaults to organization editor language. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> InlineResponse2001 get_template(template_id)

Get template

Returns template configuration

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response2001 import InlineResponse2001
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    # example passing only required values which don't have defaults set
    try:
        # Get template
        api_response = api_instance.get_template(template_id)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration as JSON object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> InlineResponse200 get_templates()

Get templates

Returns a list of templates available for the authenticated workspace

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response200 import InlineResponse200
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get templates
        api_response = api_instance.get_templates()
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> InlineResponse2001 update_template(template_id, template_definition_new)

Update template

Updates template configuration. The template configuration for pages and layout must be complete as the entire configuration is replaced and not merged.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import templates_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response2001 import InlineResponse2001
from pdf_generator_api_client.model.template_definition_new import TemplateDefinitionNew
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://us1.pdfgeneratorapi.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = pdf_generator_api_client.Configuration(
    host = "https://us1.pdfgeneratorapi.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration = pdf_generator_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
    template_definition_new = TemplateDefinitionNew(
        name="Invoice template",
        tags=["invoice","orders"],
        is_draft=True,
        layout=TemplateDefinitionNewLayout(
            format="A4",
            width=21,
            height=29.7,
            unit="cm",
            orientation="portrait",
            rotaion=0,
            margins=TemplateDefinitionNewLayoutMargins(
                top=0.5,
                right=0.5,
                bottom=0.5,
                left=0.5,
            ),
            repeat_layout=TemplateDefinitionNewLayoutRepeatLayout(
                format="A4",
                width=21,
                height=29.7,
            ),
            empty_labels=0,
        ),
        pages=[
            TemplateDefinitionNewPages(
                width=21,
                height=29.7,
                margins=TemplateDefinitionNewMargins(
                    right=0.5,
                    bottom=0.5,
                ),
                components=[
                    Component(
                        cls="labelComponent",
                        id="component-12313",
                        width=3.5,
                        height=1,
                        top=4.2,
                        left=2.5,
                        zindex=102,
                        value="${price}",
                        data_index="line_items",
                    ),
                ],
            ),
        ],
    ) # TemplateDefinitionNew | Template configuration as JSON string

    # example passing only required values which don't have defaults set
    try:
        # Update template
        api_response = api_instance.update_template(template_id, template_definition_new)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier |
 **template_definition_new** | [**TemplateDefinitionNew**](TemplateDefinitionNew.md)| Template configuration as JSON string |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template configuration as JSON object |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

