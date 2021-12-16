# pdf_generator_api_client.DocumentsApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merge_template**](DocumentsApi.md#merge_template) | **POST** /templates/{templateId}/output | Generate document
[**merge_templates**](DocumentsApi.md#merge_templates) | **POST** /templates/output | Generate document (multiple templates)


# **merge_template**
> InlineResponse2004 merge_template(template_id, data)

Generate document

Merges template with data and returns base64 encoded document or a public URL to a document. You can send json encoded data in request body or a public URL to your json file as the data parameter. NB! When the public URL option is used, the document is stored for 30 days and automatically deleted.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import documents_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.data import Data
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pdf_generator_api_client.model.inline_response2004 import InlineResponse2004
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
    api_instance = documents_api.DocumentsApi(api_client)
    template_id = 19375 # int | Template unique identifier
    data = Data(
        id=12312,
        name="Sample Data",
    ) # Data | Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
    name = "My document" # str | Document name, returned in the meta data. (optional)
    format = "pdf" # str | Document format. The zip option will return a ZIP file with PDF files. (optional) if omitted the server will use the default value of "pdf"
    output = "base64" # str | Response format. With the url option, the document is stored for 30 days and automatically deleted. (optional) if omitted the server will use the default value of "base64"

    # example passing only required values which don't have defaults set
    try:
        # Generate document
        api_response = api_instance.merge_template(template_id, data)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->merge_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate document
        api_response = api_instance.merge_template(template_id, data, name=name, format=format, output=output)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->merge_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template unique identifier |
 **data** | [**Data**](Data.md)| Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file. |
 **name** | **str**| Document name, returned in the meta data. | [optional]
 **format** | **str**| Document format. The zip option will return a ZIP file with PDF files. | [optional] if omitted the server will use the default value of "pdf"
 **output** | **str**| Response format. With the url option, the document is stored for 30 days and automatically deleted. | [optional] if omitted the server will use the default value of "base64"

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
> InlineResponse2004 merge_templates(batch_data)

Generate document (multiple templates)

Allows to merge multiple templated with data and returns base64 encoded document or public URL to a document. NB! When the public URL option is used, the document is stored for 30 days and automatically deleted.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import documents_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.batch_data import BatchData
from pdf_generator_api_client.model.inline_response403 import InlineResponse403
from pdf_generator_api_client.model.inline_response2004 import InlineResponse2004
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
    api_instance = documents_api.DocumentsApi(api_client)
    batch_data = BatchData([{"template":52272,"data":{"key":"value"}},{"template":52273,"data":{"key2":"value2"}}]) # BatchData | Data used to specify templates and data objects which are used to merge the template
    name = "My document" # str | Document name, returned in the meta data. (optional)
    format = "pdf" # str | Document format. The zip option will return a ZIP file with PDF files. (optional) if omitted the server will use the default value of "pdf"
    output = "base64" # str | Response format. With the url option, the document is stored for 30 days and automatically deleted. (optional) if omitted the server will use the default value of "base64"

    # example passing only required values which don't have defaults set
    try:
        # Generate document (multiple templates)
        api_response = api_instance.merge_templates(batch_data)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->merge_templates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate document (multiple templates)
        api_response = api_instance.merge_templates(batch_data, name=name, format=format, output=output)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling DocumentsApi->merge_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_data** | [**BatchData**](BatchData.md)| Data used to specify templates and data objects which are used to merge the template |
 **name** | **str**| Document name, returned in the meta data. | [optional]
 **format** | **str**| Document format. The zip option will return a ZIP file with PDF files. | [optional] if omitted the server will use the default value of "pdf"
 **output** | **str**| Response format. With the url option, the document is stored for 30 days and automatically deleted. | [optional] if omitted the server will use the default value of "base64"

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

