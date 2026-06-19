# pdf_generator_api_client.AssetsApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_qr_code**](AssetsApi.md#generate_qr_code) | **POST** /assets/qrcode | Generate QR Code


# **generate_qr_code**
> GenerateQRCode201Response generate_qr_code(generate_qr_code_request)

Generate QR Code

Creates a QR code based on the configuration

### Example

* Bearer (JWT) Authentication (JSONWebTokenAuth):

```python
import pdf_generator_api_client
from pdf_generator_api_client.models.generate_qr_code201_response import GenerateQRCode201Response
from pdf_generator_api_client.models.generate_qr_code_request import GenerateQRCodeRequest
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
    api_instance = pdf_generator_api_client.AssetsApi(api_client)
    generate_qr_code_request = pdf_generator_api_client.GenerateQRCodeRequest() # GenerateQRCodeRequest | QR Code configuration

    try:
        # Generate QR Code
        api_response = api_instance.generate_qr_code(generate_qr_code_request)
        print("The response of AssetsApi->generate_qr_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->generate_qr_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_qr_code_request** | [**GenerateQRCodeRequest**](GenerateQRCodeRequest.md)| QR Code configuration | 

### Return type

[**GenerateQRCode201Response**](GenerateQRCode201Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | QR code response |  -  |
**401** | Unauthorized |  -  |
**402** | Account Suspended |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

