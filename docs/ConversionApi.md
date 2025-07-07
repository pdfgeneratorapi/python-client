# pdf_generator_api_client.ConversionApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_html2_pdf**](ConversionApi.md#convert_html2_pdf) | **POST** /conversion/html2pdf | HTML to PDF
[**convert_url2_pdf**](ConversionApi.md#convert_url2_pdf) | **POST** /conversion/url2pdf | URL to PDF


# **convert_html2_pdf**
> AddWatermark201Response convert_html2_pdf(convert_html2_pdf_request)

HTML to PDF

Converts HTML content to PDF

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.convert_html2_pdf_request import ConvertHTML2PDFRequest
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
    api_instance = pdf_generator_api_client.ConversionApi(api_client)
    convert_html2_pdf_request = pdf_generator_api_client.ConvertHTML2PDFRequest() # ConvertHTML2PDFRequest | 

    try:
        # HTML to PDF
        api_response = api_instance.convert_html2_pdf(convert_html2_pdf_request)
        print("The response of ConversionApi->convert_html2_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversionApi->convert_html2_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_html2_pdf_request** | [**ConvertHTML2PDFRequest**](ConvertHTML2PDFRequest.md)|  | 

### Return type

[**AddWatermark201Response**](AddWatermark201Response.md)

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

# **convert_url2_pdf**
> AddWatermark201Response convert_url2_pdf(convert_url2_pdf_request)

URL to PDF

Converts public URL to PDF

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.convert_url2_pdf_request import ConvertURL2PDFRequest
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
    api_instance = pdf_generator_api_client.ConversionApi(api_client)
    convert_url2_pdf_request = pdf_generator_api_client.ConvertURL2PDFRequest() # ConvertURL2PDFRequest | 

    try:
        # URL to PDF
        api_response = api_instance.convert_url2_pdf(convert_url2_pdf_request)
        print("The response of ConversionApi->convert_url2_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversionApi->convert_url2_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_url2_pdf_request** | [**ConvertURL2PDFRequest**](ConvertURL2PDFRequest.md)|  | 

### Return type

[**AddWatermark201Response**](AddWatermark201Response.md)

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

