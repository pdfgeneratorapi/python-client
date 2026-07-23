# coding: utf-8

# flake8: noqa

"""
    PDF Generator API

    # Introduction [PDF Generator API](https://pdfgeneratorapi.com) allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.  The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.  ## Base URL The base URL for all the API endpoints is `https://us1.pdfgeneratorapi.com/api/v4`  For example * `https://us1.pdfgeneratorapi.com/api/v4/templates` * `https://us1.pdfgeneratorapi.com/api/v4/workspaces` * `https://us1.pdfgeneratorapi.com/api/v4/templates/123123`  ## Editor PDF Generator API comes with a powerful drag & drop editor that allows to create any kind of document templates, from barcode labels to invoices, quotes and reports. You can find tutorials and videos from our [Support Portal](https://support.pdfgeneratorapi.com). * [Component specification](https://support.pdfgeneratorapi.com/en/category/components-1ffseaj/) * [Expression Language documentation](https://support.pdfgeneratorapi.com/en/category/expression-language-q203pa/) * [Frequently asked questions and answers](https://support.pdfgeneratorapi.com/en/category/qanda-1ov519d/)  ## Definitions  ### Organization Organization is a group of workspaces owned by your account.  ### Workspace Workspace contains templates. Each workspace has access to their own templates and organization default templates.  ### Master Workspace Master Workspace is the main/default workspace of your Organization. The Master Workspace identifier is the email you signed up with.  ### Default Template Default template is a template that is available for all workspaces by default. You can set the template access type under Page Setup. If template has \"Organization\" access then your users can use them from the \"New\" menu in the Editor.  ### Data Field Data Field is a placeholder for the specific data in your JSON data set. In this example JSON you can access the buyer name using Data Field `{paymentDetails::buyerName}`. The separator between depth levels is :: (two colons). When designing the template you don’t have to know every Data Field, our editor automatically extracts all the available fields from your data set and provides an easy way to insert them into the template. ``` {     \"documentNumber\": 1,     \"paymentDetails\": {         \"method\": \"Credit Card\",         \"buyerName\": \"John Smith\"     },     \"items\": [         {             \"id\": 1,             \"name\": \"Item one\"         }     ] } ```  ## Rate limiting Our API endpoints use IP-based rate limiting and allow you to make up to 2 requests per second and 60 requests per minute. If you make more requests, you will receive a response with HTTP code 429.  Response headers contain additional values:  | Header   | Description                    | |--------|--------------------------------| | X-RateLimit-Limit    | Maximum requests per minute                   | | X-RateLimit-Remaining    | The requests remaining in the current minute               | | Retry-After     | How many seconds you need to wait until you are allowed to make requests |  *  *  *  *  *  # Libraries and SDKs ## Postman Collection We have created a [Postman Collection](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/overview) so you can easily test all the API endpoints without developing and code.   ## Client Libraries All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.  * [PHP Client](https://github.com/pdfgeneratorapi/php-client) * [Java Client](https://github.com/pdfgeneratorapi/java-client) * [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client) * [Python Client](https://github.com/pdfgeneratorapi/python-client) * [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)  We have validated the generated libraries, but let us know if you find any anomalies in the client code.  ## Model Context Protocol (MCP) Server Integrate document generation directly into your AI agents and LLM applications using our official Model Context Protocol (MCP) Server.  The MCP server provides a standardized interface that allows AI assistants (like Claude Desktop and other MCP-compatible clients) to securely interact with the PDF Generator API. With it, your AI applications can automatically fetch workspaces, retrieve templates, merge data, and generate PDF documents on the fly.  [Get PDF Generator API MCP Server](https://github.com/pdfgeneratorapi/mcp-server) *  *  *  *  *   # Authentication The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret. When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.   <SecurityDefinitions />  ## Accessing your API Key and Secret You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).  ## Creating a JWT JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.  The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form: ``` {Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature} ```  We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.  ### Header Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256. Property `typ` defines the type of token and it is always JWT. ``` {   \"alg\": \"HS256\",   \"typ\": \"JWT\" } ```  ### Payload The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required. It is mandatory to specify the following claims: * issuer (`iss`): Your API key * subject (`sub`): Workspace identifier * expiration time (`exp`): Timestamp (unix epoch time) until the token is valid. It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"exp\": 1586112639 } ```  ### Payload for Partners Our partners can send their unique identifier (provided by us) in JWT's partner_id claim. If the `partner_id` value is specified in the JWT, the organization making the request is automatically connected to the partner account. * Partner ID (`partner_id`): Unique identifier provide by PDF Generator API team  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"partner_id\": \"my-partner-identifier\",   \"exp\": 1586112639 } ```  ### Signature To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is. ``` HMACSHA256(     base64UrlEncode(header) + \".\" +     base64UrlEncode(payload),     API_SECRET) ```  ### Putting all together The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret. ``` eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q  // Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 // Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0 // Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q ```  ## Temporary JWTs You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __15 minutes__. You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications. *  *  *  *  *  # Error codes  | Code   | Description                    | |--------|--------------------------------| | 401    | Unauthorized                   | | 402    | Payment Required               | | 403    | Forbidden                      | | 404    | Not Found                      | | 422    | Unprocessable Entity           | | 429    | Too Many Requests              | | 500    | Internal Server Error          |  ## 401 Unauthorized | Description                                                             | |-------------------------------------------------------------------------| | Authentication failed: request expired                                  | | Authentication failed: workspace missing                                | | Authentication failed: key missing                                      | | Authentication failed: property 'iss' (issuer) missing in JWT           | | Authentication failed: property 'sub' (subject) missing in JWT          | | Authentication failed: property 'exp' (expiration time) missing in JWT  | | Authentication failed: incorrect signature                              |  ## 402 Payment Required | Description                                                             | |-------------------------------------------------------------------------| | Your account is suspended, please upgrade your account                  |  ## 403 Forbidden | Description                                                             | |-------------------------------------------------------------------------| | Your account has exceeded the monthly document generation limit.        | | Access not granted: You cannot delete master workspace via API          | | Access not granted: Template is not accessible by this organization     | | Your session has expired, please close and reopen the editor.           |  ## 404 Entity not found | Description                                                             | |-------------------------------------------------------------------------| | Entity not found                                                        | | Resource not found                                                      | | None of the templates is available for the workspace.                   |  ## 422 Unprocessable Entity | Description                                                             | |-------------------------------------------------------------------------| | Unable to parse JSON, please check formatting                           | | Required parameter missing                                              | | Required parameter missing: template definition not defined             | | Required parameter missing: template not defined                        |  ## 429 Too Many Requests | Description                                                             | |-------------------------------------------------------------------------| | You can make up to 2 requests per second and 60 requests per minute.   |  *  *  *  *  * 

    The version of the OpenAPI document: 4.0.28
    Contact: support@pdfgeneratorapi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "8.0.28"

# Define package exports
__all__ = [
    "AssetsApi",
    "ConversionApi",
    "DocumentsApi",
    "FormsApi",
    "MiscApi",
    "ServicesApi",
    "TemplateLibraryApi",
    "TemplateVersionsApi",
    "TemplatesApi",
    "WorkspacesApi",
    "EInvoicesApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AccessibilityOption",
    "AddWatermarkRequest",
    "AsyncOutputParam",
    "CallbackParam",
    "Component",
    "ConvertHTML2PDFRequest",
    "ConvertPDF2ImageRequest",
    "ConvertURL2PDFRequest",
    "CopyTemplateRequest",
    "CreateEInvoiceRequest",
    "CreateFacturXEInvoiceRequest",
    "CreateFacturXEInvoiceRequestTemplate",
    "CreateWorkspaceRequest",
    "DataBatchInner",
    "Document",
    "DocumentAction",
    "DocumentUser",
    "DocumentVersion",
    "EncryptAndDecryptBase64",
    "EncryptAndDecryptUrl",
    "EncryptDocumentRequest",
    "ExtractFormFieldsRequest",
    "FillFormFieldsRequest",
    "FormActionDownload",
    "FormActionSend",
    "FormActionSendSendDocument",
    "FormActionSendSendDocumentHeadersInner",
    "FormActionStore",
    "FormConfiguration",
    "FormConfigurationNew",
    "FormConfigurationNewActionsInner",
    "FormFieldsBase64",
    "FormFieldsInner",
    "FormFieldsUrl",
    "FormFillBase64",
    "FormFillUrl",
    "FormatParam",
    "GenerateDocumentAsynchronousRequest",
    "GenerateDocumentBatchAsynchronousRequest",
    "GenerateDocumentBatchRequest",
    "GenerateDocumentRequest",
    "GenerateQRCode201Response",
    "GenerateQRCode201ResponseMeta",
    "GenerateQRCodeRequest",
    "GenerateViewerUrl200Response",
    "GenerateViewerUrl200ResponseMeta",
    "GenerateViewerUrlRequest",
    "GetStatus200Response",
    "GetTemplateLibrary200Response",
    "GetTemplateVersion422Response",
    "ImportFormBase64",
    "ImportFormRequest",
    "ImportFormUrl",
    "ImportTemplateBase64",
    "ImportTemplateRequest",
    "ImportTemplateUrl",
    "ImportTemplateUrlTemplate",
    "InlineObject",
    "InlineObject1",
    "InlineObject10",
    "InlineObject10Meta",
    "InlineObject11",
    "InlineObject11Meta",
    "InlineObject12",
    "InlineObject12Meta",
    "InlineObject12MetaStats",
    "InlineObject13",
    "InlineObject14",
    "InlineObject14ResponseValue",
    "InlineObject14ResponseValueDefault",
    "InlineObject14ResponseValueValue",
    "InlineObject15",
    "InlineObject16",
    "InlineObject17",
    "InlineObject18",
    "InlineObject19",
    "InlineObject1Response",
    "InlineObject2",
    "InlineObject20",
    "InlineObject20Meta",
    "InlineObject21",
    "InlineObject22",
    "InlineObject22Response",
    "InlineObject23",
    "InlineObject24",
    "InlineObject25",
    "InlineObject26",
    "InlineObject27",
    "InlineObject28",
    "InlineObject29",
    "InlineObject3",
    "InlineObject4",
    "InlineObject5",
    "InlineObject6",
    "InlineObject7",
    "InlineObject7Response",
    "InlineObject8",
    "InlineObject9",
    "InlineObject9Meta",
    "InlineObjectMeta",
    "KeyFieldParam",
    "MakeAccessibleBase64",
    "MakeAccessibleRequest",
    "MakeAccessibleUrl",
    "MetadataParam",
    "OpenEditorRequest",
    "OpenEditorRequestData",
    "OptimizeBase64",
    "OptimizeDocumentRequest",
    "OptimizeUrl",
    "OutputParam",
    "PaginationMeta",
    "PrefillParam",
    "PromoteTemplateVersion200Response",
    "PublicTemplateLibraryItem",
    "StatusParam",
    "StoreDocumentRequest",
    "Template",
    "TemplateDefinition",
    "TemplateDefinitionDataSettings",
    "TemplateDefinitionEditor",
    "TemplateDefinitionNew",
    "TemplateDefinitionNewDataSettings",
    "TemplateDefinitionNewEditor",
    "TemplateDefinitionNewLayout",
    "TemplateDefinitionNewLayoutMargins",
    "TemplateDefinitionNewLayoutRepeatLayout",
    "TemplateDefinitionNewPagesInner",
    "TemplateDefinitionNewPagesInnerMargins",
    "TemplateDefinitionPagesInner",
    "TemplateParam",
    "TemplateParamData",
    "TemplateParamId",
    "TemplateVersion",
    "TemplateVersionCollection",
    "TemplateVersionCollectionMeta",
    "WatermarkBase64",
    "WatermarkFileUrlWatermark",
    "WatermarkImage",
    "WatermarkImageContentBase64",
    "WatermarkImageContentUrl",
    "WatermarkPosition",
    "WatermarkText",
    "Workspace",
]

# import apis into sdk package
from pdf_generator_api_client.api.assets_api import AssetsApi as AssetsApi
from pdf_generator_api_client.api.conversion_api import ConversionApi as ConversionApi
from pdf_generator_api_client.api.documents_api import DocumentsApi as DocumentsApi
from pdf_generator_api_client.api.forms_api import FormsApi as FormsApi
from pdf_generator_api_client.api.misc_api import MiscApi as MiscApi
from pdf_generator_api_client.api.services_api import ServicesApi as ServicesApi
from pdf_generator_api_client.api.template_library_api import TemplateLibraryApi as TemplateLibraryApi
from pdf_generator_api_client.api.template_versions_api import TemplateVersionsApi as TemplateVersionsApi
from pdf_generator_api_client.api.templates_api import TemplatesApi as TemplatesApi
from pdf_generator_api_client.api.workspaces_api import WorkspacesApi as WorkspacesApi
from pdf_generator_api_client.api.e_invoices_api import EInvoicesApi as EInvoicesApi

# import ApiClient
from pdf_generator_api_client.api_response import ApiResponse as ApiResponse
from pdf_generator_api_client.api_client import ApiClient as ApiClient
from pdf_generator_api_client.configuration import Configuration as Configuration
from pdf_generator_api_client.exceptions import OpenApiException as OpenApiException
from pdf_generator_api_client.exceptions import ApiTypeError as ApiTypeError
from pdf_generator_api_client.exceptions import ApiValueError as ApiValueError
from pdf_generator_api_client.exceptions import ApiKeyError as ApiKeyError
from pdf_generator_api_client.exceptions import ApiAttributeError as ApiAttributeError
from pdf_generator_api_client.exceptions import ApiException as ApiException

# import models into sdk package
from pdf_generator_api_client.models.accessibility_option import AccessibilityOption as AccessibilityOption
from pdf_generator_api_client.models.add_watermark_request import AddWatermarkRequest as AddWatermarkRequest
from pdf_generator_api_client.models.async_output_param import AsyncOutputParam as AsyncOutputParam
from pdf_generator_api_client.models.callback_param import CallbackParam as CallbackParam
from pdf_generator_api_client.models.component import Component as Component
from pdf_generator_api_client.models.convert_html2_pdf_request import ConvertHTML2PDFRequest as ConvertHTML2PDFRequest
from pdf_generator_api_client.models.convert_pdf2_image_request import ConvertPDF2ImageRequest as ConvertPDF2ImageRequest
from pdf_generator_api_client.models.convert_url2_pdf_request import ConvertURL2PDFRequest as ConvertURL2PDFRequest
from pdf_generator_api_client.models.copy_template_request import CopyTemplateRequest as CopyTemplateRequest
from pdf_generator_api_client.models.create_e_invoice_request import CreateEInvoiceRequest as CreateEInvoiceRequest
from pdf_generator_api_client.models.create_factur_xe_invoice_request import CreateFacturXEInvoiceRequest as CreateFacturXEInvoiceRequest
from pdf_generator_api_client.models.create_factur_xe_invoice_request_template import CreateFacturXEInvoiceRequestTemplate as CreateFacturXEInvoiceRequestTemplate
from pdf_generator_api_client.models.create_workspace_request import CreateWorkspaceRequest as CreateWorkspaceRequest
from pdf_generator_api_client.models.data_batch_inner import DataBatchInner as DataBatchInner
from pdf_generator_api_client.models.document import Document as Document
from pdf_generator_api_client.models.document_action import DocumentAction as DocumentAction
from pdf_generator_api_client.models.document_user import DocumentUser as DocumentUser
from pdf_generator_api_client.models.document_version import DocumentVersion as DocumentVersion
from pdf_generator_api_client.models.encrypt_and_decrypt_base64 import EncryptAndDecryptBase64 as EncryptAndDecryptBase64
from pdf_generator_api_client.models.encrypt_and_decrypt_url import EncryptAndDecryptUrl as EncryptAndDecryptUrl
from pdf_generator_api_client.models.encrypt_document_request import EncryptDocumentRequest as EncryptDocumentRequest
from pdf_generator_api_client.models.extract_form_fields_request import ExtractFormFieldsRequest as ExtractFormFieldsRequest
from pdf_generator_api_client.models.fill_form_fields_request import FillFormFieldsRequest as FillFormFieldsRequest
from pdf_generator_api_client.models.form_action_download import FormActionDownload as FormActionDownload
from pdf_generator_api_client.models.form_action_send import FormActionSend as FormActionSend
from pdf_generator_api_client.models.form_action_send_send_document import FormActionSendSendDocument as FormActionSendSendDocument
from pdf_generator_api_client.models.form_action_send_send_document_headers_inner import FormActionSendSendDocumentHeadersInner as FormActionSendSendDocumentHeadersInner
from pdf_generator_api_client.models.form_action_store import FormActionStore as FormActionStore
from pdf_generator_api_client.models.form_configuration import FormConfiguration as FormConfiguration
from pdf_generator_api_client.models.form_configuration_new import FormConfigurationNew as FormConfigurationNew
from pdf_generator_api_client.models.form_configuration_new_actions_inner import FormConfigurationNewActionsInner as FormConfigurationNewActionsInner
from pdf_generator_api_client.models.form_fields_base64 import FormFieldsBase64 as FormFieldsBase64
from pdf_generator_api_client.models.form_fields_inner import FormFieldsInner as FormFieldsInner
from pdf_generator_api_client.models.form_fields_url import FormFieldsUrl as FormFieldsUrl
from pdf_generator_api_client.models.form_fill_base64 import FormFillBase64 as FormFillBase64
from pdf_generator_api_client.models.form_fill_url import FormFillUrl as FormFillUrl
from pdf_generator_api_client.models.format_param import FormatParam as FormatParam
from pdf_generator_api_client.models.generate_document_asynchronous_request import GenerateDocumentAsynchronousRequest as GenerateDocumentAsynchronousRequest
from pdf_generator_api_client.models.generate_document_batch_asynchronous_request import GenerateDocumentBatchAsynchronousRequest as GenerateDocumentBatchAsynchronousRequest
from pdf_generator_api_client.models.generate_document_batch_request import GenerateDocumentBatchRequest as GenerateDocumentBatchRequest
from pdf_generator_api_client.models.generate_document_request import GenerateDocumentRequest as GenerateDocumentRequest
from pdf_generator_api_client.models.generate_qr_code201_response import GenerateQRCode201Response as GenerateQRCode201Response
from pdf_generator_api_client.models.generate_qr_code201_response_meta import GenerateQRCode201ResponseMeta as GenerateQRCode201ResponseMeta
from pdf_generator_api_client.models.generate_qr_code_request import GenerateQRCodeRequest as GenerateQRCodeRequest
from pdf_generator_api_client.models.generate_viewer_url200_response import GenerateViewerUrl200Response as GenerateViewerUrl200Response
from pdf_generator_api_client.models.generate_viewer_url200_response_meta import GenerateViewerUrl200ResponseMeta as GenerateViewerUrl200ResponseMeta
from pdf_generator_api_client.models.generate_viewer_url_request import GenerateViewerUrlRequest as GenerateViewerUrlRequest
from pdf_generator_api_client.models.get_status200_response import GetStatus200Response as GetStatus200Response
from pdf_generator_api_client.models.get_template_library200_response import GetTemplateLibrary200Response as GetTemplateLibrary200Response
from pdf_generator_api_client.models.get_template_version422_response import GetTemplateVersion422Response as GetTemplateVersion422Response
from pdf_generator_api_client.models.import_form_base64 import ImportFormBase64 as ImportFormBase64
from pdf_generator_api_client.models.import_form_request import ImportFormRequest as ImportFormRequest
from pdf_generator_api_client.models.import_form_url import ImportFormUrl as ImportFormUrl
from pdf_generator_api_client.models.import_template_base64 import ImportTemplateBase64 as ImportTemplateBase64
from pdf_generator_api_client.models.import_template_request import ImportTemplateRequest as ImportTemplateRequest
from pdf_generator_api_client.models.import_template_url import ImportTemplateUrl as ImportTemplateUrl
from pdf_generator_api_client.models.import_template_url_template import ImportTemplateUrlTemplate as ImportTemplateUrlTemplate
from pdf_generator_api_client.models.inline_object import InlineObject as InlineObject
from pdf_generator_api_client.models.inline_object1 import InlineObject1 as InlineObject1
from pdf_generator_api_client.models.inline_object10 import InlineObject10 as InlineObject10
from pdf_generator_api_client.models.inline_object10_meta import InlineObject10Meta as InlineObject10Meta
from pdf_generator_api_client.models.inline_object11 import InlineObject11 as InlineObject11
from pdf_generator_api_client.models.inline_object11_meta import InlineObject11Meta as InlineObject11Meta
from pdf_generator_api_client.models.inline_object12 import InlineObject12 as InlineObject12
from pdf_generator_api_client.models.inline_object12_meta import InlineObject12Meta as InlineObject12Meta
from pdf_generator_api_client.models.inline_object12_meta_stats import InlineObject12MetaStats as InlineObject12MetaStats
from pdf_generator_api_client.models.inline_object13 import InlineObject13 as InlineObject13
from pdf_generator_api_client.models.inline_object14 import InlineObject14 as InlineObject14
from pdf_generator_api_client.models.inline_object14_response_value import InlineObject14ResponseValue as InlineObject14ResponseValue
from pdf_generator_api_client.models.inline_object14_response_value_default import InlineObject14ResponseValueDefault as InlineObject14ResponseValueDefault
from pdf_generator_api_client.models.inline_object14_response_value_value import InlineObject14ResponseValueValue as InlineObject14ResponseValueValue
from pdf_generator_api_client.models.inline_object15 import InlineObject15 as InlineObject15
from pdf_generator_api_client.models.inline_object16 import InlineObject16 as InlineObject16
from pdf_generator_api_client.models.inline_object17 import InlineObject17 as InlineObject17
from pdf_generator_api_client.models.inline_object18 import InlineObject18 as InlineObject18
from pdf_generator_api_client.models.inline_object19 import InlineObject19 as InlineObject19
from pdf_generator_api_client.models.inline_object1_response import InlineObject1Response as InlineObject1Response
from pdf_generator_api_client.models.inline_object2 import InlineObject2 as InlineObject2
from pdf_generator_api_client.models.inline_object20 import InlineObject20 as InlineObject20
from pdf_generator_api_client.models.inline_object20_meta import InlineObject20Meta as InlineObject20Meta
from pdf_generator_api_client.models.inline_object21 import InlineObject21 as InlineObject21
from pdf_generator_api_client.models.inline_object22 import InlineObject22 as InlineObject22
from pdf_generator_api_client.models.inline_object22_response import InlineObject22Response as InlineObject22Response
from pdf_generator_api_client.models.inline_object23 import InlineObject23 as InlineObject23
from pdf_generator_api_client.models.inline_object24 import InlineObject24 as InlineObject24
from pdf_generator_api_client.models.inline_object25 import InlineObject25 as InlineObject25
from pdf_generator_api_client.models.inline_object26 import InlineObject26 as InlineObject26
from pdf_generator_api_client.models.inline_object27 import InlineObject27 as InlineObject27
from pdf_generator_api_client.models.inline_object28 import InlineObject28 as InlineObject28
from pdf_generator_api_client.models.inline_object29 import InlineObject29 as InlineObject29
from pdf_generator_api_client.models.inline_object3 import InlineObject3 as InlineObject3
from pdf_generator_api_client.models.inline_object4 import InlineObject4 as InlineObject4
from pdf_generator_api_client.models.inline_object5 import InlineObject5 as InlineObject5
from pdf_generator_api_client.models.inline_object6 import InlineObject6 as InlineObject6
from pdf_generator_api_client.models.inline_object7 import InlineObject7 as InlineObject7
from pdf_generator_api_client.models.inline_object7_response import InlineObject7Response as InlineObject7Response
from pdf_generator_api_client.models.inline_object8 import InlineObject8 as InlineObject8
from pdf_generator_api_client.models.inline_object9 import InlineObject9 as InlineObject9
from pdf_generator_api_client.models.inline_object9_meta import InlineObject9Meta as InlineObject9Meta
from pdf_generator_api_client.models.inline_object_meta import InlineObjectMeta as InlineObjectMeta
from pdf_generator_api_client.models.key_field_param import KeyFieldParam as KeyFieldParam
from pdf_generator_api_client.models.make_accessible_base64 import MakeAccessibleBase64 as MakeAccessibleBase64
from pdf_generator_api_client.models.make_accessible_request import MakeAccessibleRequest as MakeAccessibleRequest
from pdf_generator_api_client.models.make_accessible_url import MakeAccessibleUrl as MakeAccessibleUrl
from pdf_generator_api_client.models.metadata_param import MetadataParam as MetadataParam
from pdf_generator_api_client.models.open_editor_request import OpenEditorRequest as OpenEditorRequest
from pdf_generator_api_client.models.open_editor_request_data import OpenEditorRequestData as OpenEditorRequestData
from pdf_generator_api_client.models.optimize_base64 import OptimizeBase64 as OptimizeBase64
from pdf_generator_api_client.models.optimize_document_request import OptimizeDocumentRequest as OptimizeDocumentRequest
from pdf_generator_api_client.models.optimize_url import OptimizeUrl as OptimizeUrl
from pdf_generator_api_client.models.output_param import OutputParam as OutputParam
from pdf_generator_api_client.models.pagination_meta import PaginationMeta as PaginationMeta
from pdf_generator_api_client.models.prefill_param import PrefillParam as PrefillParam
from pdf_generator_api_client.models.promote_template_version200_response import PromoteTemplateVersion200Response as PromoteTemplateVersion200Response
from pdf_generator_api_client.models.public_template_library_item import PublicTemplateLibraryItem as PublicTemplateLibraryItem
from pdf_generator_api_client.models.status_param import StatusParam as StatusParam
from pdf_generator_api_client.models.store_document_request import StoreDocumentRequest as StoreDocumentRequest
from pdf_generator_api_client.models.template import Template as Template
from pdf_generator_api_client.models.template_definition import TemplateDefinition as TemplateDefinition
from pdf_generator_api_client.models.template_definition_data_settings import TemplateDefinitionDataSettings as TemplateDefinitionDataSettings
from pdf_generator_api_client.models.template_definition_editor import TemplateDefinitionEditor as TemplateDefinitionEditor
from pdf_generator_api_client.models.template_definition_new import TemplateDefinitionNew as TemplateDefinitionNew
from pdf_generator_api_client.models.template_definition_new_data_settings import TemplateDefinitionNewDataSettings as TemplateDefinitionNewDataSettings
from pdf_generator_api_client.models.template_definition_new_editor import TemplateDefinitionNewEditor as TemplateDefinitionNewEditor
from pdf_generator_api_client.models.template_definition_new_layout import TemplateDefinitionNewLayout as TemplateDefinitionNewLayout
from pdf_generator_api_client.models.template_definition_new_layout_margins import TemplateDefinitionNewLayoutMargins as TemplateDefinitionNewLayoutMargins
from pdf_generator_api_client.models.template_definition_new_layout_repeat_layout import TemplateDefinitionNewLayoutRepeatLayout as TemplateDefinitionNewLayoutRepeatLayout
from pdf_generator_api_client.models.template_definition_new_pages_inner import TemplateDefinitionNewPagesInner as TemplateDefinitionNewPagesInner
from pdf_generator_api_client.models.template_definition_new_pages_inner_margins import TemplateDefinitionNewPagesInnerMargins as TemplateDefinitionNewPagesInnerMargins
from pdf_generator_api_client.models.template_definition_pages_inner import TemplateDefinitionPagesInner as TemplateDefinitionPagesInner
from pdf_generator_api_client.models.template_param import TemplateParam as TemplateParam
from pdf_generator_api_client.models.template_param_data import TemplateParamData as TemplateParamData
from pdf_generator_api_client.models.template_param_id import TemplateParamId as TemplateParamId
from pdf_generator_api_client.models.template_version import TemplateVersion as TemplateVersion
from pdf_generator_api_client.models.template_version_collection import TemplateVersionCollection as TemplateVersionCollection
from pdf_generator_api_client.models.template_version_collection_meta import TemplateVersionCollectionMeta as TemplateVersionCollectionMeta
from pdf_generator_api_client.models.watermark_base64 import WatermarkBase64 as WatermarkBase64
from pdf_generator_api_client.models.watermark_file_url_watermark import WatermarkFileUrlWatermark as WatermarkFileUrlWatermark
from pdf_generator_api_client.models.watermark_image import WatermarkImage as WatermarkImage
from pdf_generator_api_client.models.watermark_image_content_base64 import WatermarkImageContentBase64 as WatermarkImageContentBase64
from pdf_generator_api_client.models.watermark_image_content_url import WatermarkImageContentUrl as WatermarkImageContentUrl
from pdf_generator_api_client.models.watermark_position import WatermarkPosition as WatermarkPosition
from pdf_generator_api_client.models.watermark_text import WatermarkText as WatermarkText
from pdf_generator_api_client.models.workspace import Workspace as Workspace
