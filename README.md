# pdf-generator-api
# Introduction
[PDF Generator API](https://pdfgeneratorapi.com) allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.

The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.

## Base URL
The base URL for all the API endpoints is `https://us1.pdfgeneratorapi.com/api/v4`

For example
* `https://us1.pdfgeneratorapi.com/api/v4/templates`
* `https://us1.pdfgeneratorapi.com/api/v4/workspaces`
* `https://us1.pdfgeneratorapi.com/api/v4/templates/123123`

## Editor
PDF Generator API comes with a powerful drag & drop editor that allows to create any kind of document templates, from barcode labels to invoices, quotes and reports. You can find tutorials and videos from our [Support Portal](https://support.pdfgeneratorapi.com).
* [Component specification](https://support.pdfgeneratorapi.com/en/category/components-1ffseaj/)
* [Expression Language documentation](https://support.pdfgeneratorapi.com/en/category/expression-language-q203pa/)
* [Frequently asked questions and answers](https://support.pdfgeneratorapi.com/en/category/qanda-1ov519d/)

## Definitions

### Organization
Organization is a group of workspaces owned by your account.

### Workspace
Workspace contains templates. Each workspace has access to their own templates and organization default templates.

### Master Workspace
Master Workspace is the main/default workspace of your Organization. The Master Workspace identifier is the email you signed up with.

### Default Template
Default template is a template that is available for all workspaces by default. You can set the template access type under Page Setup. If template has "Organization" access then your users can use them from the "New" menu in the Editor.

### Data Field
Data Field is a placeholder for the specific data in your JSON data set. In this example JSON you can access the buyer name using Data Field `{paymentDetails::buyerName}`. The separator between depth levels is :: (two colons). When designing the template you don’t have to know every Data Field, our editor automatically extracts all the available fields from your data set and provides an easy way to insert them into the template.
```
{
    "documentNumber": 1,
    "paymentDetails": {
        "method": "Credit Card",
        "buyerName": "John Smith"
    },
    "items": [
        {
            "id": 1,
            "name": "Item one"
        }
    ]
}
```

## Rate limiting
Our API endpoints use IP-based rate limiting and allow you to make up to 2 requests per second and 60 requests per minute. If you make more requests, you will receive a response with HTTP code 429.

Response headers contain additional values:

| Header   | Description                    |
|--------|--------------------------------|
| X-RateLimit-Limit    | Maximum requests per minute                   |
| X-RateLimit-Remaining    | The requests remaining in the current minute               |
| Retry-After     | How many seconds you need to wait until you are allowed to make requests |

*  *  *  *  *

# Libraries and SDKs
## Postman Collection
We have created a [Postman Collection](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/overview) so you can easily test all the API endpoints without developing and code. You can download the collection [here](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/collection/11578263-42fed446-af7e-4266-84e1-69e8c1752e93).

## Client Libraries
All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.

* [PHP Client](https://github.com/pdfgeneratorapi/php-client)
* [Java Client](https://github.com/pdfgeneratorapi/java-client)
* [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client)
* [Python Client](https://github.com/pdfgeneratorapi/python-client)
* [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)

We have validated the generated libraries, but let us know if you find any anomalies in the client code.
*  *  *  *  *

# Authentication
The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret.
When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.


<SecurityDefinitions />

## Accessing your API Key and Secret
You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).

## Creating a JWT
JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.

The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form:
```
{Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature}
```

We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.

### Header
Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256.
Property `typ` defines the type of token and it is always JWT.
```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### Payload
The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required.
It is mandatory to specify the following claims:
* issuer (`iss`): Your API key
* subject (`sub`): Workspace identifier
* expiration time (`exp`): Timestamp (unix epoch time) until the token is valid. It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.

```
{
  "iss": "ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a",
  "sub": "demo.example@actualreports.com",
  "exp": 1586112639
}
```

### Signature
To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is.
```
HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    API_SECRET)
```

### Putting all together
The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret.
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q

// Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
// Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0
// Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q
```

## Temporary JWTs
You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __15 minutes__.
You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications.
*  *  *  *  *

# Error codes

| Code   | Description                    |
|--------|--------------------------------|
| 401    | Unauthorized                   |
| 402    | Payment Required               |
| 403    | Forbidden                      |
| 404    | Not Found                      |
| 422    | Unprocessable Entity           |
| 429    | Too Many Requests              |
| 500    | Internal Server Error          |

## 401 Unauthorized
| Description                                                             |
|-------------------------------------------------------------------------|
| Authentication failed: request expired                                  |
| Authentication failed: workspace missing                                |
| Authentication failed: key missing                                      |
| Authentication failed: property 'iss' (issuer) missing in JWT           |
| Authentication failed: property 'sub' (subject) missing in JWT          |
| Authentication failed: property 'exp' (expiration time) missing in JWT  |
| Authentication failed: incorrect signature                              |

## 402 Payment Required
| Description                                                             |
|-------------------------------------------------------------------------|
| Your account is suspended, please upgrade your account                  |

## 403 Forbidden
| Description                                                             |
|-------------------------------------------------------------------------|
| Your account has exceeded the monthly document generation limit.        |
| Access not granted: You cannot delete master workspace via API          |
| Access not granted: Template is not accessible by this organization     |
| Your session has expired, please close and reopen the editor.           |

## 404 Entity not found
| Description                                                             |
|-------------------------------------------------------------------------|
| Entity not found                                                        |
| Resource not found                                                      |
| None of the templates is available for the workspace.                   |

## 422 Unprocessable Entity
| Description                                                             |
|-------------------------------------------------------------------------|
| Unable to parse JSON, please check formatting                           |
| Required parameter missing                                              |
| Required parameter missing: template definition not defined             |
| Required parameter missing: template not defined                        |

## 429 Too Many Requests
| Description                                                             |
|-------------------------------------------------------------------------|
| You can make up to 2 requests per second and 60 requests per minute.   |

*  *  *  *  *


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4.0.8
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.pdfgeneratorapi.com](https://support.pdfgeneratorapi.com)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/pdfgeneratorapi/python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/pdfgeneratorapi/python-client.git`)

Then import the package:
```python
import pdf_generator_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pdf_generator_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pdf_generator_api_client
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
    except ApiException as e:
        print("Exception when calling ConversionApi->convert_html2_pdf: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConversionApi* | [**convert_html2_pdf**](docs/ConversionApi.md#convert_html2_pdf) | **POST** /conversion/html2pdf | HTML to PDF
*ConversionApi* | [**convert_url2_pdf**](docs/ConversionApi.md#convert_url2_pdf) | **POST** /conversion/url2pdf | URL to PDF
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /documents/{publicId} | Delete document
*DocumentsApi* | [**generate_document**](docs/DocumentsApi.md#generate_document) | **POST** /documents/generate | Generate document
*DocumentsApi* | [**generate_document_asynchronous**](docs/DocumentsApi.md#generate_document_asynchronous) | **POST** /documents/generate/async | Generate document (async)
*DocumentsApi* | [**generate_document_batch**](docs/DocumentsApi.md#generate_document_batch) | **POST** /documents/generate/batch | Generate document (batch)
*DocumentsApi* | [**generate_document_batch_asynchronous**](docs/DocumentsApi.md#generate_document_batch_asynchronous) | **POST** /documents/generate/batch/async | Generate document (batch + async)
*DocumentsApi* | [**get_document**](docs/DocumentsApi.md#get_document) | **GET** /documents/{publicId} | Get document
*DocumentsApi* | [**get_documents**](docs/DocumentsApi.md#get_documents) | **GET** /documents | Get documents
*FormsApi* | [**create_from**](docs/FormsApi.md#create_from) | **POST** /forms | Create form
*FormsApi* | [**delete_form**](docs/FormsApi.md#delete_form) | **DELETE** /forms/{formId} | Delete form
*FormsApi* | [**get_form**](docs/FormsApi.md#get_form) | **GET** /forms/{formId} | Get form
*FormsApi* | [**get_forms**](docs/FormsApi.md#get_forms) | **GET** /forms | Get forms
*FormsApi* | [**share_form**](docs/FormsApi.md#share_form) | **POST** /forms/{formId}/share | Share form
*FormsApi* | [**update_form**](docs/FormsApi.md#update_form) | **PUT** /forms/{formId} | Update form
*TemplatesApi* | [**copy_template**](docs/TemplatesApi.md#copy_template) | **POST** /templates/{templateId}/copy | Copy template
*TemplatesApi* | [**create_template**](docs/TemplatesApi.md#create_template) | **POST** /templates | Create template
*TemplatesApi* | [**delete_template**](docs/TemplatesApi.md#delete_template) | **DELETE** /templates/{templateId} | Delete template
*TemplatesApi* | [**get_template**](docs/TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Get template
*TemplatesApi* | [**get_template_data**](docs/TemplatesApi.md#get_template_data) | **GET** /templates/{templateId}/data | Get template data fields
*TemplatesApi* | [**get_templates**](docs/TemplatesApi.md#get_templates) | **GET** /templates | Get templates
*TemplatesApi* | [**open_editor**](docs/TemplatesApi.md#open_editor) | **POST** /templates/{templateId}/editor | Open editor
*TemplatesApi* | [**update_template**](docs/TemplatesApi.md#update_template) | **PUT** /templates/{templateId} | Update template
*WorkspacesApi* | [**create_workspace**](docs/WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create workspace
*WorkspacesApi* | [**delete_workspace**](docs/WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspaceIdentifier} | Delete workspace
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspaceIdentifier} | Get workspace
*WorkspacesApi* | [**get_workspaces**](docs/WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get workspaces


## Documentation For Models

 - [AsyncOutputParam](docs/AsyncOutputParam.md)
 - [CallbackParam](docs/CallbackParam.md)
 - [Component](docs/Component.md)
 - [ConvertHTML2PDFRequest](docs/ConvertHTML2PDFRequest.md)
 - [ConvertURL2PDFRequest](docs/ConvertURL2PDFRequest.md)
 - [CopyTemplateRequest](docs/CopyTemplateRequest.md)
 - [CreateFrom201Response](docs/CreateFrom201Response.md)
 - [CreateTemplate201Response](docs/CreateTemplate201Response.md)
 - [CreateWorkspace201Response](docs/CreateWorkspace201Response.md)
 - [CreateWorkspaceRequest](docs/CreateWorkspaceRequest.md)
 - [DataBatchInner](docs/DataBatchInner.md)
 - [Document](docs/Document.md)
 - [FormActionDownload](docs/FormActionDownload.md)
 - [FormActionStore](docs/FormActionStore.md)
 - [FormConfiguration](docs/FormConfiguration.md)
 - [FormConfigurationNew](docs/FormConfigurationNew.md)
 - [FormConfigurationNewActionsInner](docs/FormConfigurationNewActionsInner.md)
 - [FormFieldsInner](docs/FormFieldsInner.md)
 - [FormatParam](docs/FormatParam.md)
 - [GenerateDocument201Response](docs/GenerateDocument201Response.md)
 - [GenerateDocument201ResponseMeta](docs/GenerateDocument201ResponseMeta.md)
 - [GenerateDocumentAsynchronous201Response](docs/GenerateDocumentAsynchronous201Response.md)
 - [GenerateDocumentAsynchronous201ResponseResponse](docs/GenerateDocumentAsynchronous201ResponseResponse.md)
 - [GenerateDocumentAsynchronousRequest](docs/GenerateDocumentAsynchronousRequest.md)
 - [GenerateDocumentBatchAsynchronousRequest](docs/GenerateDocumentBatchAsynchronousRequest.md)
 - [GenerateDocumentBatchRequest](docs/GenerateDocumentBatchRequest.md)
 - [GenerateDocumentRequest](docs/GenerateDocumentRequest.md)
 - [GetDocument200Response](docs/GetDocument200Response.md)
 - [GetDocument200ResponseMeta](docs/GetDocument200ResponseMeta.md)
 - [GetDocuments200Response](docs/GetDocuments200Response.md)
 - [GetForms200Response](docs/GetForms200Response.md)
 - [GetTemplateData200Response](docs/GetTemplateData200Response.md)
 - [GetTemplates200Response](docs/GetTemplates200Response.md)
 - [GetTemplates401Response](docs/GetTemplates401Response.md)
 - [GetTemplates402Response](docs/GetTemplates402Response.md)
 - [GetTemplates403Response](docs/GetTemplates403Response.md)
 - [GetTemplates404Response](docs/GetTemplates404Response.md)
 - [GetTemplates422Response](docs/GetTemplates422Response.md)
 - [GetTemplates429Response](docs/GetTemplates429Response.md)
 - [GetTemplates500Response](docs/GetTemplates500Response.md)
 - [GetWorkspaces200Response](docs/GetWorkspaces200Response.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObjectResponse](docs/InlineObjectResponse.md)
 - [OpenEditor200Response](docs/OpenEditor200Response.md)
 - [OpenEditorRequest](docs/OpenEditorRequest.md)
 - [OpenEditorRequestData](docs/OpenEditorRequestData.md)
 - [OutputParam](docs/OutputParam.md)
 - [PaginationMeta](docs/PaginationMeta.md)
 - [ShareForm201Response](docs/ShareForm201Response.md)
 - [ShareForm201ResponseMeta](docs/ShareForm201ResponseMeta.md)
 - [Template](docs/Template.md)
 - [TemplateDefinition](docs/TemplateDefinition.md)
 - [TemplateDefinitionDataSettings](docs/TemplateDefinitionDataSettings.md)
 - [TemplateDefinitionEditor](docs/TemplateDefinitionEditor.md)
 - [TemplateDefinitionNew](docs/TemplateDefinitionNew.md)
 - [TemplateDefinitionNewDataSettings](docs/TemplateDefinitionNewDataSettings.md)
 - [TemplateDefinitionNewEditor](docs/TemplateDefinitionNewEditor.md)
 - [TemplateDefinitionNewLayout](docs/TemplateDefinitionNewLayout.md)
 - [TemplateDefinitionNewLayoutMargins](docs/TemplateDefinitionNewLayoutMargins.md)
 - [TemplateDefinitionNewLayoutRepeatLayout](docs/TemplateDefinitionNewLayoutRepeatLayout.md)
 - [TemplateDefinitionNewPagesInner](docs/TemplateDefinitionNewPagesInner.md)
 - [TemplateDefinitionNewPagesInnerMargins](docs/TemplateDefinitionNewPagesInnerMargins.md)
 - [TemplateDefinitionPagesInner](docs/TemplateDefinitionPagesInner.md)
 - [TemplateParam](docs/TemplateParam.md)
 - [TemplateParamData](docs/TemplateParamData.md)
 - [Workspace](docs/Workspace.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JSONWebTokenAuth"></a>
### JSONWebTokenAuth

- **Type**: Bearer authentication (JWT)


## Author

support@pdfgeneratorapi.com


