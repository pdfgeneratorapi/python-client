# pdf_generator_api_client.WorkspacesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspaceId} | Delete workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspaceId} | Get workspace


# **delete_workspace**
> InlineResponse2002 delete_workspace(workspace_id)

Delete workspace

Deletes the workspace

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import workspaces_api
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
    api_instance = workspaces_api.WorkspacesApi(api_client)
    workspace_id = "demo.example@actualreports.com" # str | Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete workspace
        api_response = api_instance.delete_workspace(workspace_id)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier |

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

# **get_workspace**
> InlineResponse2005 get_workspace(workspace_id)

Get workspace

Returns workspace information

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):
```python
import time
import pdf_generator_api_client
from pdf_generator_api_client.api import workspaces_api
from pdf_generator_api_client.model.inline_response401 import InlineResponse401
from pdf_generator_api_client.model.inline_response422 import InlineResponse422
from pdf_generator_api_client.model.inline_response404 import InlineResponse404
from pdf_generator_api_client.model.inline_response500 import InlineResponse500
from pdf_generator_api_client.model.inline_response2005 import InlineResponse2005
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
    api_instance = workspaces_api.WorkspacesApi(api_client)
    workspace_id = "demo.example@actualreports.com" # str | Workspace identifier

    # example passing only required values which don't have defaults set
    try:
        # Get workspace
        api_response = api_instance.get_workspace(workspace_id)
        pprint(api_response)
    except pdf_generator_api_client.ApiException as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier |

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace information |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

