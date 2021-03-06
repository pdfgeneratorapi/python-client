# pdf_generator_api_client.TemplatesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_template**](TemplatesApi.md#copy_template) | **POST** /templates/{templateId}/copy | Copy template
[**create_template**](TemplatesApi.md#create_template) | **POST** /templates | Create template
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /templates/{templateId} | Delete template
[**get_editor_url**](TemplatesApi.md#get_editor_url) | **POST** /templates/{templateId}/editor | Open editor
[**get_template**](TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Get template
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /templates | Get templates
[**merge_template**](TemplatesApi.md#merge_template) | **POST** /templates/{templateId}/output | Merge template
[**merge_templates**](TemplatesApi.md#merge_templates) | **POST** /templates/output | Merge multiple templates
[**update_template**](TemplatesApi.md#update_template) | **PUT** /templates/{templateId} | Update template


# **copy_template**
> InlineResponse2001 copy_template(template_id, name=name)

Copy template

Creates a copy of a template to the workspace specified in authentication parameters.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
name = 'My copied template' # str | Name for the copied template. If name is not specified then the original name is used. (optional)

    try:
        # Copy template
        api_response = api_instance.copy_template(template_id, name=name)
        pprint(api_response)
    except ApiException as e:
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
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_definition_new = pdf_generator_api_client.TemplateDefinitionNew() # TemplateDefinitionNew | Template configuration as JSON string

    try:
        # Create template
        api_response = api_instance.create_template(template_definition_new)
        pprint(api_response)
    except ApiException as e:
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
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    try:
        # Delete template
        api_response = api_instance.delete_template(template_id)
        pprint(api_response)
    except ApiException as e:
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
> InlineResponse2003 get_editor_url(template_id, body, language=language)

Open editor

Returns an unique URL which you can use to redirect your user to the editor form your application or use the generated URL as iframe source to show the editor within your application. 

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
body = None # object | Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
language = 'en' # str | Specify the editor UI language. Defaults to organization editor language. (optional)

    try:
        # Open editor
        api_response = api_instance.get_editor_url(template_id, body, language=language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TemplatesApi->get_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 
 **body** | **object**| Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file. | 
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
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier

    try:
        # Get template
        api_response = api_instance.get_template(template_id)
        pprint(api_response)
    except ApiException as e:
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
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    
    try:
        # Get templates
        api_response = api_instance.get_templates()
        pprint(api_response)
    except ApiException as e:
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

# **merge_template**
> InlineResponse2004 merge_template(template_id, data, name=name, format=format, output=output)

Merge template

Merges template with data and returns base64 encoded document or a public URL to a document. You can send json encoded data in request body or a public URL to your json file as the data parameter.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
data = pdf_generator_api_client.Data() # Data | Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
name = 'My document' # str | Document name, returned in the meta data. (optional)
format = 'pdf' # str | Document format. The zip option will return a ZIP file with PDF files. (optional) (default to 'pdf')
output = 'base64' # str | Response format. (optional) (default to 'base64')

    try:
        # Merge template
        api_response = api_instance.merge_template(template_id, data, name=name, format=format, output=output)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TemplatesApi->merge_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier | 
 **data** | [**Data**](Data.md)| Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file. | 
 **name** | **str**| Document name, returned in the meta data. | [optional] 
 **format** | **str**| Document format. The zip option will return a ZIP file with PDF files. | [optional] [default to &#39;pdf&#39;]
 **output** | **str**| Response format. | [optional] [default to &#39;base64&#39;]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document data |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_templates**
> InlineResponse2004 merge_templates(request_body, name=name, format=format, output=output)

Merge multiple templates

Allows to merge multiples template with data and returns base64 encoded document or public url to a document.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    request_body = None # list[object] | Data used to specify templates and data objects which are used to merge the template
name = 'My document' # str | Document name, returned in the meta data. (optional)
format = 'pdf' # str | Document format. The zip option will return a ZIP file with PDF files. (optional) (default to 'pdf')
output = 'base64' # str | Response format. (optional) (default to 'base64')

    try:
        # Merge multiple templates
        api_response = api_instance.merge_templates(request_body, name=name, format=format, output=output)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TemplatesApi->merge_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[object]**](object.md)| Data used to specify templates and data objects which are used to merge the template | 
 **name** | **str**| Document name, returned in the meta data. | [optional] 
 **format** | **str**| Document format. The zip option will return a ZIP file with PDF files. | [optional] [default to &#39;pdf&#39;]
 **output** | **str**| Response format. | [optional] [default to &#39;base64&#39;]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document data |  -  |
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
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint
configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
template_definition_new = pdf_generator_api_client.TemplateDefinitionNew() # TemplateDefinitionNew | Template configuration as JSON string

    try:
        # Update template
        api_response = api_instance.update_template(template_id, template_definition_new)
        pprint(api_response)
    except ApiException as e:
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

