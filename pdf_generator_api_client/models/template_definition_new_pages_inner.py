# coding: utf-8

"""
    PDF Generator API

    # Introduction [PDF Generator API](https://pdfgeneratorapi.com) allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.  The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.  ## Base URL The base URL for all the API endpoints is `https://us1.pdfgeneratorapi.com/api/v4`  For example * `https://us1.pdfgeneratorapi.com/api/v4/templates` * `https://us1.pdfgeneratorapi.com/api/v4/workspaces` * `https://us1.pdfgeneratorapi.com/api/v4/templates/123123`  ## Editor PDF Generator API comes with a powerful drag & drop editor that allows to create any kind of document templates, from barcode labels to invoices, quotes and reports. You can find tutorials and videos from our [Support Portal](https://support.pdfgeneratorapi.com). * [Component specification](https://support.pdfgeneratorapi.com/en/category/components-1ffseaj/) * [Expression Language documentation](https://support.pdfgeneratorapi.com/en/category/expression-language-q203pa/) * [Frequently asked questions and answers](https://support.pdfgeneratorapi.com/en/category/qanda-1ov519d/)  ## Definitions  ### Organization Organization is a group of workspaces owned by your account.  ### Workspace Workspace contains templates. Each workspace has access to their own templates and organization default templates.  ### Master Workspace Master Workspace is the main/default workspace of your Organization. The Master Workspace identifier is the email you signed up with.  ### Default Template Default template is a template that is available for all workspaces by default. You can set the template access type under Page Setup. If template has \"Organization\" access then your users can use them from the \"New\" menu in the Editor.  ### Data Field Data Field is a placeholder for the specific data in your JSON data set. In this example JSON you can access the buyer name using Data Field `{paymentDetails::buyerName}`. The separator between depth levels is :: (two colons). When designing the template you don’t have to know every Data Field, our editor automatically extracts all the available fields from your data set and provides an easy way to insert them into the template. ``` {     \"documentNumber\": 1,     \"paymentDetails\": {         \"method\": \"Credit Card\",         \"buyerName\": \"John Smith\"     },     \"items\": [         {             \"id\": 1,             \"name\": \"Item one\"         }     ] } ```  ## Rate limiting Our API endpoints use IP-based rate limiting and allow you to make up to 2 requests per second and 60 requests per minute. If you make more requests, you will receive a response with HTTP code 429.  Response headers contain additional values:  | Header   | Description                    | |--------|--------------------------------| | X-RateLimit-Limit    | Maximum requests per minute                   | | X-RateLimit-Remaining    | The requests remaining in the current minute               | | Retry-After     | How many seconds you need to wait until you are allowed to make requests |  *  *  *  *  *  # Libraries and SDKs ## Postman Collection We have created a [Postman Collection](https://www.postman.com/pdfgeneratorapi/workspace/pdf-generator-api-public-workspace/overview) so you can easily test all the API endpoints without developing and code.   ## Client Libraries All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.  * [PHP Client](https://github.com/pdfgeneratorapi/php-client) * [Java Client](https://github.com/pdfgeneratorapi/java-client) * [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client) * [Python Client](https://github.com/pdfgeneratorapi/python-client) * [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)  We have validated the generated libraries, but let us know if you find any anomalies in the client code.  ## Model Context Protocol (MCP) Server Integrate document generation directly into your AI agents and LLM applications using our official Model Context Protocol (MCP) Server.  The MCP server provides a standardized interface that allows AI assistants (like Claude Desktop and other MCP-compatible clients) to securely interact with the PDF Generator API. With it, your AI applications can automatically fetch workspaces, retrieve templates, merge data, and generate PDF documents on the fly.  [Get PDF Generator API MCP Server](https://github.com/pdfgeneratorapi/mcp-server) *  *  *  *  *   # Authentication The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret. When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.   <SecurityDefinitions />  ## Accessing your API Key and Secret You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).  ## Creating a JWT JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.  The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form: ``` {Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature} ```  We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.  ### Header Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256. Property `typ` defines the type of token and it is always JWT. ``` {   \"alg\": \"HS256\",   \"typ\": \"JWT\" } ```  ### Payload The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required. It is mandatory to specify the following claims: * issuer (`iss`): Your API key * subject (`sub`): Workspace identifier * expiration time (`exp`): Timestamp (unix epoch time) until the token is valid. It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"exp\": 1586112639 } ```  ### Payload for Partners Our partners can send their unique identifier (provided by us) in JWT's partner_id claim. If the `partner_id` value is specified in the JWT, the organization making the request is automatically connected to the partner account. * Partner ID (`partner_id`): Unique identifier provide by PDF Generator API team  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"partner_id\": \"my-partner-identifier\",   \"exp\": 1586112639 } ```  ### Signature To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is. ``` HMACSHA256(     base64UrlEncode(header) + \".\" +     base64UrlEncode(payload),     API_SECRET) ```  ### Putting all together The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret. ``` eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q  // Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 // Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0 // Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q ```  ## Temporary JWTs You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __15 minutes__. You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications. *  *  *  *  *  # Error codes  Every error response is a JSON object with a `message` string. Request validation failures (422) also include an `errors` object keyed by the field that failed.  ```json {   \"message\": \"The identifier field is required.\",   \"errors\": {     \"identifier\": [\"The identifier field is required.\"]   } } ```  | Code   | Description                    | |--------|--------------------------------| | 400    | Bad Request                    | | 401    | Unauthorized                   | | 402    | Payment Required               | | 403    | Forbidden                      | | 404    | Not Found                      | | 405    | Method Not Allowed             | | 409    | Conflict                       | | 410    | Gone                           | | 422    | Unprocessable Entity           | | 429    | Too Many Requests              | | 500    | Internal Server Error          | | 503    | Service Unavailable            |  ## 401 Unauthorized | Description                                                                       | |-----------------------------------------------------------------------------------| | Authentication failed: JWT Token missing.                                         | | Authentication failed: Malformed JWT Token.                                       | | Authentication failed: Expired JWT Token.                                         | | Authentication failed: Invalid workspace.                                         | | Authentication failed: Invalid organization.                                      | | Authentication failed: This application no longer has access to the workspace.   | | Authentication failed: The sub field is required. (also `iss` and `exp`)          |  ## 402 Payment Required | Description                                                                       | |-----------------------------------------------------------------------------------| | Your account is suspended, please upgrade your account or contact support@pdfgeneratorapi.com. |  ## 403 Forbidden | Description                                                                       | |-----------------------------------------------------------------------------------| | You don't have permission to access this content. Please get in touch with your organization administrator to update your access permissions. | | This application was not granted permission for this request.                    | | Deleting own user is not allowed.                                                 | | Deleting organization owner is not allowed.                                       |  ## 404 Not Found | Description                                                                       | |-----------------------------------------------------------------------------------| | Entity not found.                                                                 | | Route not found.                                                                  | | Workspace doesn’t have access to read the template.                               |  ## 422 Unprocessable Entity | Description                                                                       | |-----------------------------------------------------------------------------------| | Unable to parse JSON, please check formatting.                                    | | Template id should be a numeric value.                                            | | The per page must be at least 1. (with `errors.per_page`)                         |  ## 429 Too Many Requests | Description                                                                       | |-----------------------------------------------------------------------------------| | Per-second rate limit exceeded. Please slow down your requests.                   | | Per-minute rate limit exceeded. Please try again in a minute.                     | | Global per-second rate limit exceeded. Please slow down your requests.            | | Global per-minute rate limit exceeded. Please try again in a minute.              |  *  *  *  *  * 

    The version of the OpenAPI document: 4.0.35
    Contact: support@pdfgeneratorapi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pdf_generator_api_client.models.template_definition_new_pages_inner_layout import TemplateDefinitionNewPagesInnerLayout
from pdf_generator_api_client.models.template_definition_new_pages_inner_margins import TemplateDefinitionNewPagesInnerMargins
from typing import Optional, Set
from typing_extensions import Self

class TemplateDefinitionNewPagesInner(BaseModel):
    """
    TemplateDefinitionNewPagesInner
    """ # noqa: E501
    width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Page width in units")
    height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Page height in units")
    margins: Optional[TemplateDefinitionNewPagesInnerMargins] = None
    border: Optional[StrictBool] = Field(default=False, description="Stored for older templates. It draws nothing.")
    components: Optional[List[Dict[str, Any]]] = Field(default=None, description="The page's components. The fields of each depend on its cls; the template schema (Get schema endpoint) lists them.")
    layout: Optional[TemplateDefinitionNewPagesInnerLayout] = None
    conditional_formats: Optional[List[Dict[str, Any]]] = Field(default=None, alias="conditionalFormats")
    background_image: Optional[StrictStr] = Field(default=None, description="The page's background image: an image URL, a data URI or a {data field} placeholder, PNG, JPEG, GIF or SVG. It is drawn over the background color and under everything else on the page, as backgroundImageFit says. A template with a background PDF does not draw it. Empty or null for none.", alias="backgroundImage")
    background_color: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The page's background color in hex color code, #RRGGBB or #RGB, or with an alpha, #RRGGBBAA, #RGBA or rgba(r, g, b, a); a translucent one is lighter, the white of the paper showing through. It fills every sheet the page runs onto, edge to edge, under everything on it, the background image included; on a sheet of labels it fills each label. A template with a background PDF is not filled. Empty or null for none.", alias="backgroundColor")
    background_image_fit: Optional[StrictStr] = Field(default=None, description="How the background image covers the page, centred: `stretch`, stretched to the page, as when none is set; `contain`, fitted inside the page, keeping its proportions; `cover`, filling the page, keeping its proportions, with what overflows cut off. Null for stretch.", alias="backgroundImageFit")
    __properties: ClassVar[List[str]] = ["width", "height", "margins", "border", "components", "layout", "conditionalFormats", "backgroundImage", "backgroundColor", "backgroundImageFit"]

    @field_validator('background_color')
    def background_color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})|[rR][gG][bB][aA]?\(\s*(\d+(\.\d+)?|\.\d+)%?\s*,\s*(\d+(\.\d+)?|\.\d+)%?\s*,\s*(\d+(\.\d+)?|\.\d+)%?\s*(,\s*(\d+(\.\d+)?|\.\d+)%?\s*)?\))?$", value):
            raise ValueError(r"must validate the regular expression /^(#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})|[rR][gG][bB][aA]?\(\s*(\d+(\.\d+)?|\.\d+)%?\s*,\s*(\d+(\.\d+)?|\.\d+)%?\s*,\s*(\d+(\.\d+)?|\.\d+)%?\s*(,\s*(\d+(\.\d+)?|\.\d+)%?\s*)?\))?$/")
        return value

    @field_validator('background_image_fit')
    def background_image_fit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['stretch', 'contain', 'cover']):
            raise ValueError("must be one of enum values ('stretch', 'contain', 'cover')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TemplateDefinitionNewPagesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of margins
        if self.margins:
            _dict['margins'] = self.margins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of layout
        if self.layout:
            _dict['layout'] = self.layout.to_dict()
        # set to None if background_image (nullable) is None
        # and model_fields_set contains the field
        if self.background_image is None and "background_image" in self.model_fields_set:
            _dict['backgroundImage'] = None

        # set to None if background_color (nullable) is None
        # and model_fields_set contains the field
        if self.background_color is None and "background_color" in self.model_fields_set:
            _dict['backgroundColor'] = None

        # set to None if background_image_fit (nullable) is None
        # and model_fields_set contains the field
        if self.background_image_fit is None and "background_image_fit" in self.model_fields_set:
            _dict['backgroundImageFit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemplateDefinitionNewPagesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "width": obj.get("width"),
            "height": obj.get("height"),
            "margins": TemplateDefinitionNewPagesInnerMargins.from_dict(obj["margins"]) if obj.get("margins") is not None else None,
            "border": obj.get("border") if obj.get("border") is not None else False,
            "components": obj.get("components"),
            "layout": TemplateDefinitionNewPagesInnerLayout.from_dict(obj["layout"]) if obj.get("layout") is not None else None,
            "conditionalFormats": obj.get("conditionalFormats"),
            "backgroundImage": obj.get("backgroundImage"),
            "backgroundColor": obj.get("backgroundColor"),
            "backgroundImageFit": obj.get("backgroundImageFit")
        })
        return _obj


