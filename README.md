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
We have created a [Postman Collection](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/overview) so you can easily test all the API endpoints without developing and code.


## Client Libraries
All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.

* [PHP Client](https://github.com/pdfgeneratorapi/php-client)
* [Java Client](https://github.com/pdfgeneratorapi/java-client)
* [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client)
* [Python Client](https://github.com/pdfgeneratorapi/python-client)
* [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)

We have validated the generated libraries, but let us know if you find any anomalies in the client code.

## Model Context Protocol (MCP) Server
Integrate document generation directly into your AI agents and LLM applications using our official Model Context Protocol (MCP) Server.

The MCP server provides a standardized interface that allows AI assistants (like Claude Desktop and other MCP-compatible clients) to securely interact with the PDF Generator API. With it, your AI applications can automatically fetch workspaces, retrieve templates, merge data, and generate PDF documents on the fly.

[Get PDF Generator API MCP Server](https://github.com/pdfgeneratorapi/mcp-server)
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

### Payload for Partners
Our partners can send their unique identifier (provided by us) in JWT's partner_id claim. If the `partner_id` value is specified in the JWT, the organization making the request is automatically connected to the partner account.
* Partner ID (`partner_id`): Unique identifier provide by PDF Generator API team

```
{
  "iss": "ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a",
  "sub": "demo.example@actualreports.com",
  "partner_id": "my-partner-identifier",
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

- API version: 4.0.26
- Package version: 8.0.26
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.pdfgeneratorapi.com](https://support.pdfgeneratorapi.com)

## Requirements.

Python 3.9+

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
    api_instance = pdf_generator_api_client.AssetsApi(api_client)
    generate_qr_code_request = pdf_generator_api_client.GenerateQRCodeRequest() # GenerateQRCodeRequest | QR Code configuration

    try:
        # Generate QR Code
        api_response = api_instance.generate_qr_code(generate_qr_code_request)
        print("The response of AssetsApi->generate_qr_code:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->generate_qr_code: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssetsApi* | [**generate_qr_code**](docs/AssetsApi.md#generate_qr_code) | **POST** /assets/qrcode | Generate QR Code
*ConversionApi* | [**convert_html2_pdf**](docs/ConversionApi.md#convert_html2_pdf) | **POST** /conversion/html2pdf | HTML to PDF
*ConversionApi* | [**convert_pdf2_image**](docs/ConversionApi.md#convert_pdf2_image) | **POST** /conversion/pdf2image | PDF to Image
*ConversionApi* | [**convert_url2_pdf**](docs/ConversionApi.md#convert_url2_pdf) | **POST** /conversion/url2pdf | URL to PDF
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /documents/{publicId}/actions | Delete document
*DocumentsApi* | [**generate_document**](docs/DocumentsApi.md#generate_document) | **POST** /documents/generate | Generate document
*DocumentsApi* | [**generate_document_asynchronous**](docs/DocumentsApi.md#generate_document_asynchronous) | **POST** /documents/generate/async | Generate document (async)
*DocumentsApi* | [**generate_document_batch**](docs/DocumentsApi.md#generate_document_batch) | **POST** /documents/generate/batch | Generate document (batch)
*DocumentsApi* | [**generate_document_batch_asynchronous**](docs/DocumentsApi.md#generate_document_batch_asynchronous) | **POST** /documents/generate/batch/async | Generate document (batch + async)
*DocumentsApi* | [**get_async_job_status**](docs/DocumentsApi.md#get_async_job_status) | **GET** /documents/async/{jobId} | Get job status
*DocumentsApi* | [**get_document**](docs/DocumentsApi.md#get_document) | **GET** /documents/{publicId} | Get document
*DocumentsApi* | [**get_document_actions**](docs/DocumentsApi.md#get_document_actions) | **GET** /documents/{publicId}/actions | Get document actions
*DocumentsApi* | [**get_document_versions**](docs/DocumentsApi.md#get_document_versions) | **GET** /documents/{publicId}/versions | Get document versions
*DocumentsApi* | [**get_documents**](docs/DocumentsApi.md#get_documents) | **GET** /documents | Get documents
*DocumentsApi* | [**store_document**](docs/DocumentsApi.md#store_document) | **POST** /documents | Store document
*FormsApi* | [**create_form**](docs/FormsApi.md#create_form) | **POST** /forms | Create form
*FormsApi* | [**delete_form**](docs/FormsApi.md#delete_form) | **DELETE** /forms/{formId} | Delete form
*FormsApi* | [**get_form**](docs/FormsApi.md#get_form) | **GET** /forms/{formId} | Get form
*FormsApi* | [**get_forms**](docs/FormsApi.md#get_forms) | **GET** /forms | Get forms
*FormsApi* | [**import_form**](docs/FormsApi.md#import_form) | **POST** /forms/import | Import Form
*FormsApi* | [**open_form_builder**](docs/FormsApi.md#open_form_builder) | **POST** /forms/open | Open new form builder
*FormsApi* | [**open_form_builder_for_existing_form**](docs/FormsApi.md#open_form_builder_for_existing_form) | **POST** /forms/{formId}/open | Open existing form builder
*FormsApi* | [**share_form**](docs/FormsApi.md#share_form) | **POST** /forms/{formId}/share | Share form
*FormsApi* | [**update_form**](docs/FormsApi.md#update_form) | **PUT** /forms/{formId} | Update form
*MiscApi* | [**get_status**](docs/MiscApi.md#get_status) | **GET** /status | Get Service Status
*ServicesApi* | [**add_watermark**](docs/ServicesApi.md#add_watermark) | **POST** /pdfservices/watermark | Add watermark
*ServicesApi* | [**decrypt_document**](docs/ServicesApi.md#decrypt_document) | **POST** /pdfservices/decrypt | Decrypt document
*ServicesApi* | [**encrypt_document**](docs/ServicesApi.md#encrypt_document) | **POST** /pdfservices/encrypt | Encrypt document
*ServicesApi* | [**extract_form_fields**](docs/ServicesApi.md#extract_form_fields) | **POST** /pdfservices/form/fields | Extract form fields
*ServicesApi* | [**fill_form_fields**](docs/ServicesApi.md#fill_form_fields) | **POST** /pdfservices/form/fill | Fill form fields
*ServicesApi* | [**make_accessible**](docs/ServicesApi.md#make_accessible) | **POST** /pdfservices/make-accessible | Make accessible
*ServicesApi* | [**optimize_document**](docs/ServicesApi.md#optimize_document) | **POST** /pdfservices/optimize | Optimize document
*TemplateLibraryApi* | [**get_template_library**](docs/TemplateLibraryApi.md#get_template_library) | **GET** /templates/library | Get template library
*TemplateLibraryApi* | [**get_template_library_item**](docs/TemplateLibraryApi.md#get_template_library_item) | **GET** /templates/library/{publicId} | Open template from the library
*TemplateVersionsApi* | [**delete_template_version**](docs/TemplateVersionsApi.md#delete_template_version) | **DELETE** /templates/{templateId}/versions/{templateVersion} | Delete template version
*TemplateVersionsApi* | [**get_template_version**](docs/TemplateVersionsApi.md#get_template_version) | **GET** /templates/{templateId}/versions/{templateVersion} | Get template version
*TemplateVersionsApi* | [**list_template_versions**](docs/TemplateVersionsApi.md#list_template_versions) | **GET** /templates/{templateId}/versions | List template versions
*TemplateVersionsApi* | [**promote_template_version**](docs/TemplateVersionsApi.md#promote_template_version) | **PUT** /templates/{templateId}/versions/{templateVersion}/promote | Promote template version
*TemplatesApi* | [**copy_template**](docs/TemplatesApi.md#copy_template) | **POST** /templates/{templateId}/copy | Copy template
*TemplatesApi* | [**create_template**](docs/TemplatesApi.md#create_template) | **POST** /templates | Create template
*TemplatesApi* | [**delete_template**](docs/TemplatesApi.md#delete_template) | **DELETE** /templates/{templateId} | Delete template
*TemplatesApi* | [**get_template**](docs/TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Get template
*TemplatesApi* | [**get_template_data**](docs/TemplatesApi.md#get_template_data) | **GET** /templates/{templateId}/data | Get template data fields
*TemplatesApi* | [**get_template_schema**](docs/TemplatesApi.md#get_template_schema) | **GET** /templates/schema | Get schema
*TemplatesApi* | [**get_templates**](docs/TemplatesApi.md#get_templates) | **GET** /templates | Get templates
*TemplatesApi* | [**import_template**](docs/TemplatesApi.md#import_template) | **POST** /templates/import | Import template
*TemplatesApi* | [**open_editor**](docs/TemplatesApi.md#open_editor) | **POST** /templates/{templateId}/editor | Open editor
*TemplatesApi* | [**update_template**](docs/TemplatesApi.md#update_template) | **PUT** /templates/{templateId} | Update template
*TemplatesApi* | [**validate_template**](docs/TemplatesApi.md#validate_template) | **POST** /templates/validate | Validate template
*WorkspacesApi* | [**create_workspace**](docs/WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create workspace
*WorkspacesApi* | [**delete_workspace**](docs/WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspaceIdentifier} | Delete workspace
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspaceIdentifier} | Get workspace
*WorkspacesApi* | [**get_workspaces**](docs/WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get workspaces
*EInvoicesApi* | [**create_e_invoice**](docs/EInvoicesApi.md#create_e_invoice) | **POST** /einvoice | Create eInvoice
*EInvoicesApi* | [**create_factur_xe_invoice**](docs/EInvoicesApi.md#create_factur_xe_invoice) | **POST** /einvoice/facturx | Create Factur-X eInvoice
*EInvoicesApi* | [**create_x_rechnung_e_invoice**](docs/EInvoicesApi.md#create_x_rechnung_e_invoice) | **POST** /einvoice/xrechnung | Create XRechnung eInvoice
*EInvoicesApi* | [**get_e_invoice_schema**](docs/EInvoicesApi.md#get_e_invoice_schema) | **GET** /einvoice/schema | Get schema


## Documentation For Models

 - [AccessibilityOption](docs/AccessibilityOption.md)
 - [AddWatermarkRequest](docs/AddWatermarkRequest.md)
 - [AsyncOutputParam](docs/AsyncOutputParam.md)
 - [CallbackParam](docs/CallbackParam.md)
 - [Component](docs/Component.md)
 - [ConvertHTML2PDFRequest](docs/ConvertHTML2PDFRequest.md)
 - [ConvertPDF2ImageRequest](docs/ConvertPDF2ImageRequest.md)
 - [ConvertURL2PDFRequest](docs/ConvertURL2PDFRequest.md)
 - [CopyTemplateRequest](docs/CopyTemplateRequest.md)
 - [CreateEInvoiceRequest](docs/CreateEInvoiceRequest.md)
 - [CreateFacturXEInvoiceRequest](docs/CreateFacturXEInvoiceRequest.md)
 - [CreateFacturXEInvoiceRequestTemplate](docs/CreateFacturXEInvoiceRequestTemplate.md)
 - [CreateWorkspaceRequest](docs/CreateWorkspaceRequest.md)
 - [DataBatchInner](docs/DataBatchInner.md)
 - [Document](docs/Document.md)
 - [DocumentAction](docs/DocumentAction.md)
 - [DocumentUser](docs/DocumentUser.md)
 - [DocumentVersion](docs/DocumentVersion.md)
 - [EncryptAndDecryptBase64](docs/EncryptAndDecryptBase64.md)
 - [EncryptAndDecryptUrl](docs/EncryptAndDecryptUrl.md)
 - [EncryptDocumentRequest](docs/EncryptDocumentRequest.md)
 - [ExtractFormFieldsRequest](docs/ExtractFormFieldsRequest.md)
 - [FillFormFieldsRequest](docs/FillFormFieldsRequest.md)
 - [FormActionDownload](docs/FormActionDownload.md)
 - [FormActionSend](docs/FormActionSend.md)
 - [FormActionSendSendDocument](docs/FormActionSendSendDocument.md)
 - [FormActionSendSendDocumentHeadersInner](docs/FormActionSendSendDocumentHeadersInner.md)
 - [FormActionStore](docs/FormActionStore.md)
 - [FormConfiguration](docs/FormConfiguration.md)
 - [FormConfigurationNew](docs/FormConfigurationNew.md)
 - [FormConfigurationNewActionsInner](docs/FormConfigurationNewActionsInner.md)
 - [FormFieldsBase64](docs/FormFieldsBase64.md)
 - [FormFieldsInner](docs/FormFieldsInner.md)
 - [FormFieldsUrl](docs/FormFieldsUrl.md)
 - [FormFillBase64](docs/FormFillBase64.md)
 - [FormFillUrl](docs/FormFillUrl.md)
 - [FormatParam](docs/FormatParam.md)
 - [GenerateDocumentAsynchronousRequest](docs/GenerateDocumentAsynchronousRequest.md)
 - [GenerateDocumentBatchAsynchronousRequest](docs/GenerateDocumentBatchAsynchronousRequest.md)
 - [GenerateDocumentBatchRequest](docs/GenerateDocumentBatchRequest.md)
 - [GenerateDocumentRequest](docs/GenerateDocumentRequest.md)
 - [GenerateQRCode201Response](docs/GenerateQRCode201Response.md)
 - [GenerateQRCode201ResponseMeta](docs/GenerateQRCode201ResponseMeta.md)
 - [GenerateQRCodeRequest](docs/GenerateQRCodeRequest.md)
 - [GetStatus200Response](docs/GetStatus200Response.md)
 - [GetTemplateLibrary200Response](docs/GetTemplateLibrary200Response.md)
 - [GetTemplateVersion422Response](docs/GetTemplateVersion422Response.md)
 - [ImportFormBase64](docs/ImportFormBase64.md)
 - [ImportFormRequest](docs/ImportFormRequest.md)
 - [ImportFormUrl](docs/ImportFormUrl.md)
 - [ImportTemplateBase64](docs/ImportTemplateBase64.md)
 - [ImportTemplateRequest](docs/ImportTemplateRequest.md)
 - [ImportTemplateUrl](docs/ImportTemplateUrl.md)
 - [ImportTemplateUrlTemplate](docs/ImportTemplateUrlTemplate.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject10](docs/InlineObject10.md)
 - [InlineObject10Meta](docs/InlineObject10Meta.md)
 - [InlineObject11](docs/InlineObject11.md)
 - [InlineObject11Meta](docs/InlineObject11Meta.md)
 - [InlineObject12](docs/InlineObject12.md)
 - [InlineObject12Meta](docs/InlineObject12Meta.md)
 - [InlineObject12MetaStats](docs/InlineObject12MetaStats.md)
 - [InlineObject13](docs/InlineObject13.md)
 - [InlineObject14](docs/InlineObject14.md)
 - [InlineObject14ResponseValue](docs/InlineObject14ResponseValue.md)
 - [InlineObject14ResponseValueDefault](docs/InlineObject14ResponseValueDefault.md)
 - [InlineObject14ResponseValueValue](docs/InlineObject14ResponseValueValue.md)
 - [InlineObject15](docs/InlineObject15.md)
 - [InlineObject16](docs/InlineObject16.md)
 - [InlineObject17](docs/InlineObject17.md)
 - [InlineObject18](docs/InlineObject18.md)
 - [InlineObject19](docs/InlineObject19.md)
 - [InlineObject1Response](docs/InlineObject1Response.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject20](docs/InlineObject20.md)
 - [InlineObject20Meta](docs/InlineObject20Meta.md)
 - [InlineObject21](docs/InlineObject21.md)
 - [InlineObject22](docs/InlineObject22.md)
 - [InlineObject22Response](docs/InlineObject22Response.md)
 - [InlineObject23](docs/InlineObject23.md)
 - [InlineObject24](docs/InlineObject24.md)
 - [InlineObject25](docs/InlineObject25.md)
 - [InlineObject26](docs/InlineObject26.md)
 - [InlineObject27](docs/InlineObject27.md)
 - [InlineObject28](docs/InlineObject28.md)
 - [InlineObject29](docs/InlineObject29.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineObject6](docs/InlineObject6.md)
 - [InlineObject7](docs/InlineObject7.md)
 - [InlineObject7Response](docs/InlineObject7Response.md)
 - [InlineObject8](docs/InlineObject8.md)
 - [InlineObject9](docs/InlineObject9.md)
 - [InlineObject9Meta](docs/InlineObject9Meta.md)
 - [InlineObjectMeta](docs/InlineObjectMeta.md)
 - [KeyFieldParam](docs/KeyFieldParam.md)
 - [MakeAccessibleBase64](docs/MakeAccessibleBase64.md)
 - [MakeAccessibleRequest](docs/MakeAccessibleRequest.md)
 - [MakeAccessibleUrl](docs/MakeAccessibleUrl.md)
 - [MetadataParam](docs/MetadataParam.md)
 - [OpenEditorRequest](docs/OpenEditorRequest.md)
 - [OpenEditorRequestData](docs/OpenEditorRequestData.md)
 - [OptimizeBase64](docs/OptimizeBase64.md)
 - [OptimizeDocumentRequest](docs/OptimizeDocumentRequest.md)
 - [OptimizeUrl](docs/OptimizeUrl.md)
 - [OutputParam](docs/OutputParam.md)
 - [PaginationMeta](docs/PaginationMeta.md)
 - [PromoteTemplateVersion200Response](docs/PromoteTemplateVersion200Response.md)
 - [PublicTemplateLibraryItem](docs/PublicTemplateLibraryItem.md)
 - [StatusParam](docs/StatusParam.md)
 - [StoreDocumentRequest](docs/StoreDocumentRequest.md)
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
 - [TemplateParamId](docs/TemplateParamId.md)
 - [TemplateVersion](docs/TemplateVersion.md)
 - [TemplateVersionCollection](docs/TemplateVersionCollection.md)
 - [TemplateVersionCollectionMeta](docs/TemplateVersionCollectionMeta.md)
 - [WatermarkBase64](docs/WatermarkBase64.md)
 - [WatermarkFileUrlWatermark](docs/WatermarkFileUrlWatermark.md)
 - [WatermarkImage](docs/WatermarkImage.md)
 - [WatermarkImageContentBase64](docs/WatermarkImageContentBase64.md)
 - [WatermarkImageContentUrl](docs/WatermarkImageContentUrl.md)
 - [WatermarkPosition](docs/WatermarkPosition.md)
 - [WatermarkText](docs/WatermarkText.md)
 - [Workspace](docs/Workspace.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JSONWebTokenAuth"></a>
### JSONWebTokenAuth

- **Type**: Bearer authentication (JWT)


## Author

support@pdfgeneratorapi.com


