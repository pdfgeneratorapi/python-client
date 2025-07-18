# coding: utf-8

# flake8: noqa

"""
    PDF Generator API

    # Introduction [PDF Generator API](https://pdfgeneratorapi.com) allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.  The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.  ## Base URL The base URL for all the API endpoints is `https://us1.pdfgeneratorapi.com/api/v4`  For example * `https://us1.pdfgeneratorapi.com/api/v4/templates` * `https://us1.pdfgeneratorapi.com/api/v4/workspaces` * `https://us1.pdfgeneratorapi.com/api/v4/templates/123123`  ## Editor PDF Generator API comes with a powerful drag & drop editor that allows to create any kind of document templates, from barcode labels to invoices, quotes and reports. You can find tutorials and videos from our [Support Portal](https://support.pdfgeneratorapi.com). * [Component specification](https://support.pdfgeneratorapi.com/en/category/components-1ffseaj/) * [Expression Language documentation](https://support.pdfgeneratorapi.com/en/category/expression-language-q203pa/) * [Frequently asked questions and answers](https://support.pdfgeneratorapi.com/en/category/qanda-1ov519d/)  ## Definitions  ### Organization Organization is a group of workspaces owned by your account.  ### Workspace Workspace contains templates. Each workspace has access to their own templates and organization default templates.  ### Master Workspace Master Workspace is the main/default workspace of your Organization. The Master Workspace identifier is the email you signed up with.  ### Default Template Default template is a template that is available for all workspaces by default. You can set the template access type under Page Setup. If template has \"Organization\" access then your users can use them from the \"New\" menu in the Editor.  ### Data Field Data Field is a placeholder for the specific data in your JSON data set. In this example JSON you can access the buyer name using Data Field `{paymentDetails::buyerName}`. The separator between depth levels is :: (two colons). When designing the template you don’t have to know every Data Field, our editor automatically extracts all the available fields from your data set and provides an easy way to insert them into the template. ``` {     \"documentNumber\": 1,     \"paymentDetails\": {         \"method\": \"Credit Card\",         \"buyerName\": \"John Smith\"     },     \"items\": [         {             \"id\": 1,             \"name\": \"Item one\"         }     ] } ```  ## Rate limiting Our API endpoints use IP-based rate limiting and allow you to make up to 2 requests per second and 60 requests per minute. If you make more requests, you will receive a response with HTTP code 429.  Response headers contain additional values:  | Header   | Description                    | |--------|--------------------------------| | X-RateLimit-Limit    | Maximum requests per minute                   | | X-RateLimit-Remaining    | The requests remaining in the current minute               | | Retry-After     | How many seconds you need to wait until you are allowed to make requests |  *  *  *  *  *  # Libraries and SDKs ## Postman Collection We have created a [Postman Collection](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/overview) so you can easily test all the API endpoints without developing and code. You can download the collection [here](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/collection/11578263-42fed446-af7e-4266-84e1-69e8c1752e93).  ## Client Libraries All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.  * [PHP Client](https://github.com/pdfgeneratorapi/php-client) * [Java Client](https://github.com/pdfgeneratorapi/java-client) * [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client) * [Python Client](https://github.com/pdfgeneratorapi/python-client) * [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)  We have validated the generated libraries, but let us know if you find any anomalies in the client code. *  *  *  *  *  # Authentication The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret. When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.   <SecurityDefinitions />  ## Accessing your API Key and Secret You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).  ## Creating a JWT JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.  The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form: ``` {Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature} ```  We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.  ### Header Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256. Property `typ` defines the type of token and it is always JWT. ``` {   \"alg\": \"HS256\",   \"typ\": \"JWT\" } ```  ### Payload The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required. It is mandatory to specify the following claims: * issuer (`iss`): Your API key * subject (`sub`): Workspace identifier * expiration time (`exp`): Timestamp (unix epoch time) until the token is valid. It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"exp\": 1586112639 } ```  ### Payload for Partners Our partners can send their unique identifier (provided by us) in JWT's partner_id claim. If the `partner_id` value is specified in the JWT, the organization making the request is automatically connected to the partner account. * Partner ID (`partner_id`): Unique identifier provide by PDF Generator API team  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"partner_id\": \"my-partner-identifier\",   \"exp\": 1586112639 } ```  ### Signature To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is. ``` HMACSHA256(     base64UrlEncode(header) + \".\" +     base64UrlEncode(payload),     API_SECRET) ```  ### Putting all together The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret. ``` eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q  // Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 // Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0 // Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q ```  ## Temporary JWTs You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __15 minutes__. You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications. *  *  *  *  *  # Error codes  | Code   | Description                    | |--------|--------------------------------| | 401    | Unauthorized                   | | 402    | Payment Required               | | 403    | Forbidden                      | | 404    | Not Found                      | | 422    | Unprocessable Entity           | | 429    | Too Many Requests              | | 500    | Internal Server Error          |  ## 401 Unauthorized | Description                                                             | |-------------------------------------------------------------------------| | Authentication failed: request expired                                  | | Authentication failed: workspace missing                                | | Authentication failed: key missing                                      | | Authentication failed: property 'iss' (issuer) missing in JWT           | | Authentication failed: property 'sub' (subject) missing in JWT          | | Authentication failed: property 'exp' (expiration time) missing in JWT  | | Authentication failed: incorrect signature                              |  ## 402 Payment Required | Description                                                             | |-------------------------------------------------------------------------| | Your account is suspended, please upgrade your account                  |  ## 403 Forbidden | Description                                                             | |-------------------------------------------------------------------------| | Your account has exceeded the monthly document generation limit.        | | Access not granted: You cannot delete master workspace via API          | | Access not granted: Template is not accessible by this organization     | | Your session has expired, please close and reopen the editor.           |  ## 404 Entity not found | Description                                                             | |-------------------------------------------------------------------------| | Entity not found                                                        | | Resource not found                                                      | | None of the templates is available for the workspace.                   |  ## 422 Unprocessable Entity | Description                                                             | |-------------------------------------------------------------------------| | Unable to parse JSON, please check formatting                           | | Required parameter missing                                              | | Required parameter missing: template definition not defined             | | Required parameter missing: template not defined                        |  ## 429 Too Many Requests | Description                                                             | |-------------------------------------------------------------------------| | You can make up to 2 requests per second and 60 requests per minute.   |  *  *  *  *  * 

    The version of the OpenAPI document: 4.0.12
    Contact: support@pdfgeneratorapi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from pdf_generator_api_client.api.conversion_api import ConversionApi
from pdf_generator_api_client.api.documents_api import DocumentsApi
from pdf_generator_api_client.api.forms_api import FormsApi
from pdf_generator_api_client.api.misc_api import MiscApi
from pdf_generator_api_client.api.services_api import ServicesApi
from pdf_generator_api_client.api.templates_api import TemplatesApi
from pdf_generator_api_client.api.workspaces_api import WorkspacesApi

# import ApiClient
from pdf_generator_api_client.api_response import ApiResponse
from pdf_generator_api_client.api_client import ApiClient
from pdf_generator_api_client.configuration import Configuration
from pdf_generator_api_client.exceptions import OpenApiException
from pdf_generator_api_client.exceptions import ApiTypeError
from pdf_generator_api_client.exceptions import ApiValueError
from pdf_generator_api_client.exceptions import ApiKeyError
from pdf_generator_api_client.exceptions import ApiAttributeError
from pdf_generator_api_client.exceptions import ApiException

# import models into sdk package
from pdf_generator_api_client.models.add_watermark201_response import AddWatermark201Response
from pdf_generator_api_client.models.add_watermark201_response_meta import AddWatermark201ResponseMeta
from pdf_generator_api_client.models.add_watermark401_response import AddWatermark401Response
from pdf_generator_api_client.models.add_watermark402_response import AddWatermark402Response
from pdf_generator_api_client.models.add_watermark403_response import AddWatermark403Response
from pdf_generator_api_client.models.add_watermark404_response import AddWatermark404Response
from pdf_generator_api_client.models.add_watermark422_response import AddWatermark422Response
from pdf_generator_api_client.models.add_watermark429_response import AddWatermark429Response
from pdf_generator_api_client.models.add_watermark500_response import AddWatermark500Response
from pdf_generator_api_client.models.add_watermark_request import AddWatermarkRequest
from pdf_generator_api_client.models.async_output_param import AsyncOutputParam
from pdf_generator_api_client.models.callback_param import CallbackParam
from pdf_generator_api_client.models.component import Component
from pdf_generator_api_client.models.convert_html2_pdf_request import ConvertHTML2PDFRequest
from pdf_generator_api_client.models.convert_url2_pdf_request import ConvertURL2PDFRequest
from pdf_generator_api_client.models.copy_template_request import CopyTemplateRequest
from pdf_generator_api_client.models.create_from201_response import CreateFrom201Response
from pdf_generator_api_client.models.create_template201_response import CreateTemplate201Response
from pdf_generator_api_client.models.create_workspace201_response import CreateWorkspace201Response
from pdf_generator_api_client.models.create_workspace_request import CreateWorkspaceRequest
from pdf_generator_api_client.models.data_batch_inner import DataBatchInner
from pdf_generator_api_client.models.document import Document
from pdf_generator_api_client.models.encrypt_and_decrypt_base64 import EncryptAndDecryptBase64
from pdf_generator_api_client.models.encrypt_and_decrypt_url import EncryptAndDecryptUrl
from pdf_generator_api_client.models.encrypt_document_request import EncryptDocumentRequest
from pdf_generator_api_client.models.extract_form_fields200_response import ExtractFormFields200Response
from pdf_generator_api_client.models.extract_form_fields200_response_response_value import ExtractFormFields200ResponseResponseValue
from pdf_generator_api_client.models.extract_form_fields200_response_response_value_default import ExtractFormFields200ResponseResponseValueDefault
from pdf_generator_api_client.models.extract_form_fields200_response_response_value_value import ExtractFormFields200ResponseResponseValueValue
from pdf_generator_api_client.models.extract_form_fields_request import ExtractFormFieldsRequest
from pdf_generator_api_client.models.fill_form_fields_request import FillFormFieldsRequest
from pdf_generator_api_client.models.form_action_download import FormActionDownload
from pdf_generator_api_client.models.form_action_store import FormActionStore
from pdf_generator_api_client.models.form_configuration import FormConfiguration
from pdf_generator_api_client.models.form_configuration_new import FormConfigurationNew
from pdf_generator_api_client.models.form_configuration_new_actions_inner import FormConfigurationNewActionsInner
from pdf_generator_api_client.models.form_fields_base64 import FormFieldsBase64
from pdf_generator_api_client.models.form_fields_inner import FormFieldsInner
from pdf_generator_api_client.models.form_fields_url import FormFieldsUrl
from pdf_generator_api_client.models.form_fill_base64 import FormFillBase64
from pdf_generator_api_client.models.form_fill_url import FormFillUrl
from pdf_generator_api_client.models.format_param import FormatParam
from pdf_generator_api_client.models.generate_document_asynchronous201_response import GenerateDocumentAsynchronous201Response
from pdf_generator_api_client.models.generate_document_asynchronous201_response_response import GenerateDocumentAsynchronous201ResponseResponse
from pdf_generator_api_client.models.generate_document_asynchronous_request import GenerateDocumentAsynchronousRequest
from pdf_generator_api_client.models.generate_document_batch_asynchronous_request import GenerateDocumentBatchAsynchronousRequest
from pdf_generator_api_client.models.generate_document_batch_request import GenerateDocumentBatchRequest
from pdf_generator_api_client.models.generate_document_request import GenerateDocumentRequest
from pdf_generator_api_client.models.get_document200_response import GetDocument200Response
from pdf_generator_api_client.models.get_document200_response_meta import GetDocument200ResponseMeta
from pdf_generator_api_client.models.get_documents200_response import GetDocuments200Response
from pdf_generator_api_client.models.get_forms200_response import GetForms200Response
from pdf_generator_api_client.models.get_status200_response import GetStatus200Response
from pdf_generator_api_client.models.get_template_data200_response import GetTemplateData200Response
from pdf_generator_api_client.models.get_templates200_response import GetTemplates200Response
from pdf_generator_api_client.models.get_workspaces200_response import GetWorkspaces200Response
from pdf_generator_api_client.models.inline_object import InlineObject
from pdf_generator_api_client.models.inline_object_response import InlineObjectResponse
from pdf_generator_api_client.models.open_editor200_response import OpenEditor200Response
from pdf_generator_api_client.models.open_editor_request import OpenEditorRequest
from pdf_generator_api_client.models.open_editor_request_data import OpenEditorRequestData
from pdf_generator_api_client.models.optimize_base64 import OptimizeBase64
from pdf_generator_api_client.models.optimize_document201_response import OptimizeDocument201Response
from pdf_generator_api_client.models.optimize_document201_response_meta import OptimizeDocument201ResponseMeta
from pdf_generator_api_client.models.optimize_document201_response_meta_stats import OptimizeDocument201ResponseMetaStats
from pdf_generator_api_client.models.optimize_document_request import OptimizeDocumentRequest
from pdf_generator_api_client.models.optimize_url import OptimizeUrl
from pdf_generator_api_client.models.output_param import OutputParam
from pdf_generator_api_client.models.pagination_meta import PaginationMeta
from pdf_generator_api_client.models.share_form201_response import ShareForm201Response
from pdf_generator_api_client.models.share_form201_response_meta import ShareForm201ResponseMeta
from pdf_generator_api_client.models.template import Template
from pdf_generator_api_client.models.template_definition import TemplateDefinition
from pdf_generator_api_client.models.template_definition_data_settings import TemplateDefinitionDataSettings
from pdf_generator_api_client.models.template_definition_editor import TemplateDefinitionEditor
from pdf_generator_api_client.models.template_definition_new import TemplateDefinitionNew
from pdf_generator_api_client.models.template_definition_new_data_settings import TemplateDefinitionNewDataSettings
from pdf_generator_api_client.models.template_definition_new_editor import TemplateDefinitionNewEditor
from pdf_generator_api_client.models.template_definition_new_layout import TemplateDefinitionNewLayout
from pdf_generator_api_client.models.template_definition_new_layout_margins import TemplateDefinitionNewLayoutMargins
from pdf_generator_api_client.models.template_definition_new_layout_repeat_layout import TemplateDefinitionNewLayoutRepeatLayout
from pdf_generator_api_client.models.template_definition_new_pages_inner import TemplateDefinitionNewPagesInner
from pdf_generator_api_client.models.template_definition_new_pages_inner_margins import TemplateDefinitionNewPagesInnerMargins
from pdf_generator_api_client.models.template_definition_pages_inner import TemplateDefinitionPagesInner
from pdf_generator_api_client.models.template_param import TemplateParam
from pdf_generator_api_client.models.template_param_data import TemplateParamData
from pdf_generator_api_client.models.validate_template200_response import ValidateTemplate200Response
from pdf_generator_api_client.models.validate_template200_response_response import ValidateTemplate200ResponseResponse
from pdf_generator_api_client.models.watermark_base64 import WatermarkBase64
from pdf_generator_api_client.models.watermark_file_url_watermark import WatermarkFileUrlWatermark
from pdf_generator_api_client.models.watermark_image import WatermarkImage
from pdf_generator_api_client.models.watermark_image_content_base64 import WatermarkImageContentBase64
from pdf_generator_api_client.models.watermark_image_content_url import WatermarkImageContentUrl
from pdf_generator_api_client.models.watermark_position import WatermarkPosition
from pdf_generator_api_client.models.watermark_text import WatermarkText
from pdf_generator_api_client.models.workspace import Workspace
