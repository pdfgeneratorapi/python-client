# pdf_generator_api_client.ConversionApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_html2_pdf**](ConversionApi.md#convert_html2_pdf) | **POST** /conversion/html2pdf | HTML to PDF
[**convert_pdf2_image**](ConversionApi.md#convert_pdf2_image) | **POST** /conversion/pdf2image | PDF to Image
[**convert_url2_pdf**](ConversionApi.md#convert_url2_pdf) | **POST** /conversion/url2pdf | URL to PDF


# **convert_html2_pdf**
> InlineObject8 convert_html2_pdf(convert_html2_pdf_request)

HTML to PDF

Converts HTML content to PDF

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.convert_html2_pdf_request import ConvertHTML2PDFRequest
from pdf_generator_api_client.models.inline_object8 import InlineObject8
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

[**InlineObject8**](InlineObject8.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document data |  -  |
**401** | Unauthorized. The message starts with &#x60;Authentication failed:&#x60; followed by the reason: * &#x60;JWT Token missing.&#x60; * &#x60;Malformed JWT Token.&#x60; * &#x60;Expired JWT Token.&#x60; * &#x60;Invalid workspace.&#x60; * &#x60;Invalid organization.&#x60; * &#x60;This application no longer has access to the workspace.&#x60; * a missing &#x60;iss&#x60;, &#x60;sub&#x60; or &#x60;exp&#x60; claim, e.g. &#x60;The sub field is required.&#x60;  |  -  |
**402** | Payment Required. The account is suspended. |  -  |
**403** | Forbidden. The workspace is not allowed to perform the request, for example a regular workspace calling an endpoint reserved for the master workspace. Requests made with an OAuth application credential that lacks the scope for the endpoint also get a &#x60;WWW-Authenticate&#x60; header.  |  * WWW-Authenticate - Sent only when an OAuth application credential lacks the required scope. <br>  |
**404** | Not Found. The resource does not exist or the workspace cannot access it. |  -  |
**422** | Unprocessable Entity. Request validation failures, including an invalid &#x60;page&#x60; or &#x60;per_page&#x60;, return an &#x60;errors&#x60; object keyed by field. Other 422 errors, such as a malformed JSON body or a failed conversion, return only &#x60;message&#x60;.  |  -  |
**429** | Too Many Requests. Wait for the number of seconds in the &#x60;Retry-After&#x60; header before retrying. |  * Retry-After - Seconds to wait before the next request is allowed. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_pdf2_image**
> bytearray convert_pdf2_image(convert_pdf2_image_request)

PDF to Image

Converts PDF document to images. Provide either a base64 encoded PDF or a public URL to a PDF file.

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.convert_pdf2_image_request import ConvertPDF2ImageRequest
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
    convert_pdf2_image_request = pdf_generator_api_client.ConvertPDF2ImageRequest() # ConvertPDF2ImageRequest | 

    try:
        # PDF to Image
        api_response = api_instance.convert_pdf2_image(convert_pdf2_image_request)
        print("The response of ConversionApi->convert_pdf2_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversionApi->convert_pdf2_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_pdf2_image_request** | [**ConvertPDF2ImageRequest**](ConvertPDF2ImageRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PDF to image conversion result. &#x60;output&#x3D;file&#x60; returns a ZIP archive with one image per page. |  -  |
**401** | Unauthorized. The message starts with &#x60;Authentication failed:&#x60; followed by the reason: * &#x60;JWT Token missing.&#x60; * &#x60;Malformed JWT Token.&#x60; * &#x60;Expired JWT Token.&#x60; * &#x60;Invalid workspace.&#x60; * &#x60;Invalid organization.&#x60; * &#x60;This application no longer has access to the workspace.&#x60; * a missing &#x60;iss&#x60;, &#x60;sub&#x60; or &#x60;exp&#x60; claim, e.g. &#x60;The sub field is required.&#x60;  |  -  |
**402** | Payment Required. The account is suspended. |  -  |
**403** | Forbidden. The workspace is not allowed to perform the request, for example a regular workspace calling an endpoint reserved for the master workspace. Requests made with an OAuth application credential that lacks the scope for the endpoint also get a &#x60;WWW-Authenticate&#x60; header.  |  * WWW-Authenticate - Sent only when an OAuth application credential lacks the required scope. <br>  |
**404** | Not Found. The resource does not exist or the workspace cannot access it. |  -  |
**422** | Unprocessable Entity. Request validation failures, including an invalid &#x60;page&#x60; or &#x60;per_page&#x60;, return an &#x60;errors&#x60; object keyed by field. Other 422 errors, such as a malformed JSON body or a failed conversion, return only &#x60;message&#x60;.  |  -  |
**429** | Too Many Requests. Wait for the number of seconds in the &#x60;Retry-After&#x60; header before retrying. |  * Retry-After - Seconds to wait before the next request is allowed. <br>  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable. PDF Services is not available on this deployment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_url2_pdf**
> InlineObject8 convert_url2_pdf(convert_url2_pdf_request)

URL to PDF

Converts public URL to PDF.

By default the page is printed once its network activity settles. Pages that keep making background requests (e.g. single-page applications) can signal when they have finished rendering with `wait_for_css` and/or `wait_for_js`; the page is then printed as soon as the signal is met. When both are given, both must be met.


### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.convert_url2_pdf_request import ConvertURL2PDFRequest
from pdf_generator_api_client.models.inline_object8 import InlineObject8
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

[**InlineObject8**](InlineObject8.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document data |  -  |
**400** | Bad Request. The page at the URL could not be converted to PDF.  |  -  |
**401** | Unauthorized. The message starts with &#x60;Authentication failed:&#x60; followed by the reason: * &#x60;JWT Token missing.&#x60; * &#x60;Malformed JWT Token.&#x60; * &#x60;Expired JWT Token.&#x60; * &#x60;Invalid workspace.&#x60; * &#x60;Invalid organization.&#x60; * &#x60;This application no longer has access to the workspace.&#x60; * a missing &#x60;iss&#x60;, &#x60;sub&#x60; or &#x60;exp&#x60; claim, e.g. &#x60;The sub field is required.&#x60;  |  -  |
**402** | Payment Required. The account is suspended. |  -  |
**403** | Forbidden. The workspace is not allowed to perform the request, for example a regular workspace calling an endpoint reserved for the master workspace. Requests made with an OAuth application credential that lacks the scope for the endpoint also get a &#x60;WWW-Authenticate&#x60; header.  |  * WWW-Authenticate - Sent only when an OAuth application credential lacks the required scope. <br>  |
**404** | Not Found. The resource does not exist or the workspace cannot access it. |  -  |
**422** | Unprocessable Entity. Request validation failures, including an invalid &#x60;page&#x60; or &#x60;per_page&#x60;, return an &#x60;errors&#x60; object keyed by field. Other 422 errors, such as a malformed JSON body or a failed conversion, return only &#x60;message&#x60;.  |  -  |
**429** | Too Many Requests. Wait for the number of seconds in the &#x60;Retry-After&#x60; header before retrying. |  * Retry-After - Seconds to wait before the next request is allowed. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

