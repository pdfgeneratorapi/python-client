# coding: utf-8

"""
    PDF Generator API

    # Introduction [PDF Generator API](https://pdfgeneratorapi.com) allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.  The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.  ## Base URL The base URL for all the API endpoints is `https://us1.pdfgeneratorapi.com/api/v4`  For example * `https://us1.pdfgeneratorapi.com/api/v4/templates` * `https://us1.pdfgeneratorapi.com/api/v4/workspaces` * `https://us1.pdfgeneratorapi.com/api/v4/templates/123123`  ## Editor PDF Generator API comes with a powerful drag & drop editor that allows to create any kind of document templates, from barcode labels to invoices, quotes and reports. You can find tutorials and videos from our [Support Portal](https://support.pdfgeneratorapi.com). * [Component specification](https://support.pdfgeneratorapi.com/en/category/components-1ffseaj/) * [Expression Language documentation](https://support.pdfgeneratorapi.com/en/category/expression-language-q203pa/) * [Frequently asked questions and answers](https://support.pdfgeneratorapi.com/en/category/qanda-1ov519d/)  ## Definitions  ### Organization Organization is a group of workspaces owned by your account.  ### Workspace Workspace contains templates. Each workspace has access to their own templates and organization default templates.  ### Master Workspace Master Workspace is the main/default workspace of your Organization. The Master Workspace identifier is the email you signed up with.  ### Default Template Default template is a template that is available for all workspaces by default. You can set the template access type under Page Setup. If template has \"Organization\" access then your users can use them from the \"New\" menu in the Editor.  ### Data Field Data Field is a placeholder for the specific data in your JSON data set. In this example JSON you can access the buyer name using Data Field `{paymentDetails::buyerName}`. The separator between depth levels is :: (two colons). When designing the template you don’t have to know every Data Field, our editor automatically extracts all the available fields from your data set and provides an easy way to insert them into the template. ``` {     \"documentNumber\": 1,     \"paymentDetails\": {         \"method\": \"Credit Card\",         \"buyerName\": \"John Smith\"     },     \"items\": [         {             \"id\": 1,             \"name\": \"Item one\"         }     ] } ```  ## Rate limiting Our API endpoints use IP-based rate limiting and allow you to make up to 2 requests per second and 60 requests per minute. If you make more requests, you will receive a response with HTTP code 429.  Response headers contain additional values:  | Header   | Description                    | |--------|--------------------------------| | X-RateLimit-Limit    | Maximum requests per minute                   | | X-RateLimit-Remaining    | The requests remaining in the current minute               | | Retry-After     | How many seconds you need to wait until you are allowed to make requests |  *  *  *  *  *  # Libraries and SDKs ## Postman Collection We have created a [Postman](https://www.postman.com) Collection so you can easily test all the API endpoints without developing and code. You can download the collection [here](https://god.gw.postman.com/run-collection/11578263-c6546175-de49-4b35-904b-29bb52a5a69a?action=collection%2Ffork&collection-url=entityId%3D11578263-c6546175-de49-4b35-904b-29bb52a5a69a%26entityType%3Dcollection%26workspaceId%3D5900d75f-c45d-4e61-9fb7-63aca23580df) or just click the button below.   [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/11578263-c6546175-de49-4b35-904b-29bb52a5a69a?action=collection%2Ffork&collection-url=entityId%3D11578263-c6546175-de49-4b35-904b-29bb52a5a69a%26entityType%3Dcollection%26workspaceId%3D5900d75f-c45d-4e61-9fb7-63aca23580df)  ## Client Libraries All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.  * [PHP Client](https://github.com/pdfgeneratorapi/php-client) * [Java Client](https://github.com/pdfgeneratorapi/java-client) * [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client) * [Python Client](https://github.com/pdfgeneratorapi/python-client) * [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)  We have validated the generated libraries, but let us know if you find any anomalies in the client code. *  *  *  *  *  # Authentication The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret. When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.   <SecurityDefinitions />  ## Accessing your API Key and Secret You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).  ## Creating a JWT JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.  The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form: ``` {Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature} ```  We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.  ### Header Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256. Property `typ` defines the type of token and it is always JWT. ``` {   \"alg\": \"HS256\",   \"typ\": \"JWT\" } ```  ### Payload The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required. It is mandatory to specify the following claims: * issuer (`iss`): Your API key * subject (`sub`): Workspace identifier * expiration time (`exp`): Timestamp (unix epoch time) until the token is valid. It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"exp\": 1586112639 } ```  ### Signature To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is. ``` HMACSHA256(     base64UrlEncode(header) + \".\" +     base64UrlEncode(payload),     API_SECRET) ```  ### Putting all together The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret. ``` eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q  // Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 // Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0 // Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q ```  ## Temporary JWTs You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __15 minutes__. You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications. *  *  *  *  *  # Error codes  | Code   | Description                    | |--------|--------------------------------| | 401    | Unauthorized                   | | 402    | Payment Required               | | 403    | Forbidden                      | | 404    | Not Found                      | | 422    | Unprocessable Entity           | | 429    | Too Many Requests              | | 500    | Internal Server Error          |  ## 401 Unauthorized | Description                                                             | |-------------------------------------------------------------------------| | Authentication failed: request expired                                  | | Authentication failed: workspace missing                                | | Authentication failed: key missing                                      | | Authentication failed: property 'iss' (issuer) missing in JWT           | | Authentication failed: property 'sub' (subject) missing in JWT          | | Authentication failed: property 'exp' (expiration time) missing in JWT  | | Authentication failed: incorrect signature                              |  ## 402 Payment Required | Description                                                             | |-------------------------------------------------------------------------| | Your account is suspended, please upgrade your account                  |  ## 403 Forbidden | Description                                                             | |-------------------------------------------------------------------------| | Your account has exceeded the monthly document generation limit.        | | Access not granted: You cannot delete master workspace via API          | | Access not granted: Template is not accessible by this organization     | | Your session has expired, please close and reopen the editor.           |  ## 404 Entity not found | Description                                                             | |-------------------------------------------------------------------------| | Entity not found                                                        | | Resource not found                                                      | | None of the templates is available for the workspace.                   |  ## 422 Unprocessable Entity | Description                                                             | |-------------------------------------------------------------------------| | Unable to parse JSON, please check formatting                           | | Required parameter missing                                              | | Required parameter missing: template definition not defined             | | Required parameter missing: template not defined                        |  ## 429 Too Many Requests | Description                                                             | |-------------------------------------------------------------------------| | You can make up to 2 requests per second and 60 requests per minute.   |  *  *  *  *  *   # noqa: E501

    The version of the OpenAPI document: 4.0.3
    Contact: support@pdfgeneratorapi.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pdf_generator_api_client import schemas  # noqa: F401


class TemplateDefinition(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            name = schemas.StrSchema
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            isDraft = schemas.BoolSchema
            
            
            class layout(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class format(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "A4": "A4",
                                    "letter": "LETTER",
                                    "custom": "CUSTOM",
                                }
                            
                            @schemas.classproperty
                            def A4(cls):
                                return cls("A4")
                            
                            @schemas.classproperty
                            def LETTER(cls):
                                return cls("letter")
                            
                            @schemas.classproperty
                            def CUSTOM(cls):
                                return cls("custom")
                        width = schemas.NumberSchema
                        height = schemas.NumberSchema
                        
                        
                        class unit(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "cm": "CM",
                                    "in": "IN",
                                }
                            
                            @schemas.classproperty
                            def CM(cls):
                                return cls("cm")
                            
                            @schemas.classproperty
                            def IN(cls):
                                return cls("in")
                        
                        
                        class orientation(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "portrait": "PORTRAIT",
                                    "landscape": "LANDSCAPE",
                                }
                            
                            @schemas.classproperty
                            def PORTRAIT(cls):
                                return cls("portrait")
                            
                            @schemas.classproperty
                            def LANDSCAPE(cls):
                                return cls("landscape")
                        
                        
                        class rotation(
                            schemas.EnumBase,
                            schemas.IntSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    0: "POSITIVE_0",
                                    90: "POSITIVE_90",
                                    180: "POSITIVE_180",
                                    270: "POSITIVE_270",
                                }
                            
                            @schemas.classproperty
                            def POSITIVE_0(cls):
                                return cls(0)
                            
                            @schemas.classproperty
                            def POSITIVE_90(cls):
                                return cls(90)
                            
                            @schemas.classproperty
                            def POSITIVE_180(cls):
                                return cls(180)
                            
                            @schemas.classproperty
                            def POSITIVE_270(cls):
                                return cls(270)
                        
                        
                        class margins(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    top = schemas.NumberSchema
                                    right = schemas.NumberSchema
                                    bottom = schemas.NumberSchema
                                    left = schemas.NumberSchema
                                    __annotations__ = {
                                        "top": top,
                                        "right": right,
                                        "bottom": bottom,
                                        "left": left,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["top"]) -> MetaOapg.properties.top: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["right"]) -> MetaOapg.properties.right: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["bottom"]) -> MetaOapg.properties.bottom: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["left"]) -> MetaOapg.properties.left: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["top", "right", "bottom", "left", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["top"]) -> typing.Union[MetaOapg.properties.top, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["right"]) -> typing.Union[MetaOapg.properties.right, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["bottom"]) -> typing.Union[MetaOapg.properties.bottom, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["left"]) -> typing.Union[MetaOapg.properties.left, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["top", "right", "bottom", "left", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                top: typing.Union[MetaOapg.properties.top, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                right: typing.Union[MetaOapg.properties.right, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                bottom: typing.Union[MetaOapg.properties.bottom, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                left: typing.Union[MetaOapg.properties.left, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'margins':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    top=top,
                                    right=right,
                                    bottom=bottom,
                                    left=left,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class repeatLayout(
                            schemas.DictBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneFrozenDictMixin
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class format(
                                        schemas.EnumBase,
                                        schemas.StrSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            enum_value_to_name = {
                                                "A4": "A4",
                                                "letter": "LETTER",
                                                "custom": "CUSTOM",
                                            }
                                        
                                        @schemas.classproperty
                                        def A4(cls):
                                            return cls("A4")
                                        
                                        @schemas.classproperty
                                        def LETTER(cls):
                                            return cls("letter")
                                        
                                        @schemas.classproperty
                                        def CUSTOM(cls):
                                            return cls("custom")
                                    width = schemas.NumberSchema
                                    height = schemas.NumberSchema
                                    __annotations__ = {
                                        "format": format,
                                        "width": width,
                                        "height": height,
                                    }
                        
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["format", "width", "height", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["format", "width", "height", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, None, ],
                                format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
                                width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'repeatLayout':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    format=format,
                                    width=width,
                                    height=height,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        emptyLabels = schemas.IntSchema
                        __annotations__ = {
                            "format": format,
                            "width": width,
                            "height": height,
                            "unit": unit,
                            "orientation": orientation,
                            "rotation": rotation,
                            "margins": margins,
                            "repeatLayout": repeatLayout,
                            "emptyLabels": emptyLabels,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["orientation"]) -> MetaOapg.properties.orientation: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["rotation"]) -> MetaOapg.properties.rotation: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["margins"]) -> MetaOapg.properties.margins: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["repeatLayout"]) -> MetaOapg.properties.repeatLayout: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["emptyLabels"]) -> MetaOapg.properties.emptyLabels: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["format", "width", "height", "unit", "orientation", "rotation", "margins", "repeatLayout", "emptyLabels", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> typing.Union[MetaOapg.properties.unit, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["orientation"]) -> typing.Union[MetaOapg.properties.orientation, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["rotation"]) -> typing.Union[MetaOapg.properties.rotation, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["margins"]) -> typing.Union[MetaOapg.properties.margins, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["repeatLayout"]) -> typing.Union[MetaOapg.properties.repeatLayout, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["emptyLabels"]) -> typing.Union[MetaOapg.properties.emptyLabels, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["format", "width", "height", "unit", "orientation", "rotation", "margins", "repeatLayout", "emptyLabels", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
                    width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    unit: typing.Union[MetaOapg.properties.unit, str, schemas.Unset] = schemas.unset,
                    orientation: typing.Union[MetaOapg.properties.orientation, str, schemas.Unset] = schemas.unset,
                    rotation: typing.Union[MetaOapg.properties.rotation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    margins: typing.Union[MetaOapg.properties.margins, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    repeatLayout: typing.Union[MetaOapg.properties.repeatLayout, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
                    emptyLabels: typing.Union[MetaOapg.properties.emptyLabels, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'layout':
                    return super().__new__(
                        cls,
                        *_args,
                        format=format,
                        width=width,
                        height=height,
                        unit=unit,
                        orientation=orientation,
                        rotation=rotation,
                        margins=margins,
                        repeatLayout=repeatLayout,
                        emptyLabels=emptyLabels,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class pages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                width = schemas.NumberSchema
                                height = schemas.NumberSchema
                                
                                
                                class margins(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            right = schemas.NumberSchema
                                            bottom = schemas.NumberSchema
                                            __annotations__ = {
                                                "right": right,
                                                "bottom": bottom,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["right"]) -> MetaOapg.properties.right: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["bottom"]) -> MetaOapg.properties.bottom: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["right", "bottom", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["right"]) -> typing.Union[MetaOapg.properties.right, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["bottom"]) -> typing.Union[MetaOapg.properties.bottom, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["right", "bottom", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        right: typing.Union[MetaOapg.properties.right, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                        bottom: typing.Union[MetaOapg.properties.bottom, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'margins':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            right=right,
                                            bottom=bottom,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                
                                
                                class components(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['Component']:
                                            return Component
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple['Component'], typing.List['Component']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'components':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'Component':
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "width": width,
                                    "height": height,
                                    "margins": margins,
                                    "components": components,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["margins"]) -> MetaOapg.properties.margins: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["components"]) -> MetaOapg.properties.components: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["width", "height", "margins", "components", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["margins"]) -> typing.Union[MetaOapg.properties.margins, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["components"]) -> typing.Union[MetaOapg.properties.components, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["width", "height", "margins", "components", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            margins: typing.Union[MetaOapg.properties.margins, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            components: typing.Union[MetaOapg.properties.components, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                width=width,
                                height=height,
                                margins=margins,
                                components=components,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pages':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class dataSettings(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class sortBy(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.DictSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'sortBy':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        
                        
                        class filterBy(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.DictSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'filterBy':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "sortBy": sortBy,
                            "filterBy": filterBy,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sortBy"]) -> MetaOapg.properties.sortBy: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["filterBy"]) -> MetaOapg.properties.filterBy: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sortBy", "filterBy", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sortBy"]) -> typing.Union[MetaOapg.properties.sortBy, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["filterBy"]) -> typing.Union[MetaOapg.properties.filterBy, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sortBy", "filterBy", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    sortBy: typing.Union[MetaOapg.properties.sortBy, list, tuple, schemas.Unset] = schemas.unset,
                    filterBy: typing.Union[MetaOapg.properties.filterBy, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'dataSettings':
                    return super().__new__(
                        cls,
                        *_args,
                        sortBy=sortBy,
                        filterBy=filterBy,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class editor(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        heightMultiplier = schemas.NumberSchema
                        __annotations__ = {
                            "heightMultiplier": heightMultiplier,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["heightMultiplier"]) -> MetaOapg.properties.heightMultiplier: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["heightMultiplier", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["heightMultiplier"]) -> typing.Union[MetaOapg.properties.heightMultiplier, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["heightMultiplier", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    heightMultiplier: typing.Union[MetaOapg.properties.heightMultiplier, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'editor':
                    return super().__new__(
                        cls,
                        *_args,
                        heightMultiplier=heightMultiplier,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "name": name,
                "tags": tags,
                "isDraft": isDraft,
                "layout": layout,
                "pages": pages,
                "dataSettings": dataSettings,
                "editor": editor,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDraft"]) -> MetaOapg.properties.isDraft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layout"]) -> MetaOapg.properties.layout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSettings"]) -> MetaOapg.properties.dataSettings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editor"]) -> MetaOapg.properties.editor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "tags", "isDraft", "layout", "pages", "dataSettings", "editor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDraft"]) -> typing.Union[MetaOapg.properties.isDraft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layout"]) -> typing.Union[MetaOapg.properties.layout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> typing.Union[MetaOapg.properties.pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSettings"]) -> typing.Union[MetaOapg.properties.dataSettings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editor"]) -> typing.Union[MetaOapg.properties.editor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "tags", "isDraft", "layout", "pages", "dataSettings", "editor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        isDraft: typing.Union[MetaOapg.properties.isDraft, bool, schemas.Unset] = schemas.unset,
        layout: typing.Union[MetaOapg.properties.layout, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        pages: typing.Union[MetaOapg.properties.pages, list, tuple, schemas.Unset] = schemas.unset,
        dataSettings: typing.Union[MetaOapg.properties.dataSettings, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        editor: typing.Union[MetaOapg.properties.editor, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateDefinition':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            tags=tags,
            isDraft=isDraft,
            layout=layout,
            pages=pages,
            dataSettings=dataSettings,
            editor=editor,
            _configuration=_configuration,
            **kwargs,
        )

from pdf_generator_api_client.model.component import Component
