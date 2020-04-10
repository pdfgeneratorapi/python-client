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
    api_instance = pdf_generator_api_client.WorkspacesApi(api_client)
    workspace_id = 'demo.example@actualreports.com' # str | Workspace identifier

    try:
        # Delete workspace
        api_response = api_instance.delete_workspace(workspace_id)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = pdf_generator_api_client.WorkspacesApi(api_client)
    workspace_id = 'demo.example@actualreports.com' # str | Workspace identifier

    try:
        # Get workspace
        api_response = api_instance.get_workspace(workspace_id)
        pprint(api_response)
    except ApiException as e:
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

