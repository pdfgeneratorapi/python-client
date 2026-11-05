# pdf_generator_api_client.MiscApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](MiscApi.md#get_status) | **GET** /status | Get Service Status


# **get_status**
> GetStatus200Response get_status()

Get Service Status

Returns service status / health

### Example


```python
import pdf_generator_api_client
from pdf_generator_api_client.models.get_status200_response import GetStatus200Response
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
    api_instance = pdf_generator_api_client.MiscApi(api_client)

    try:
        # Get Service Status
        api_response = api_instance.get_status()
        print("The response of MiscApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatus200Response**](GetStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns service status |  -  |
**500** | At least one check failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

