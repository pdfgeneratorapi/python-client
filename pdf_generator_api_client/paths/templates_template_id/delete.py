# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from pdf_generator_api_client import api_client, exceptions
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

from . import path

# Path params
TemplateIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'templateId': typing.Union[TemplateIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_template_id = api_client.PathParameter(
    name="templateId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TemplateIdSchema,
    required=True,
)
_auth = [
    'JSONWebTokenAuth',
]


class SchemaFor204ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class response(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        success = schemas.BoolSchema
                        __annotations__ = {
                            "success": success,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["success", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["success", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'response':
                    return super().__new__(
                        cls,
                        *args,
                        success=success,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "response": response,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response"]) -> MetaOapg.properties.response: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["response", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response"]) -> typing.Union[MetaOapg.properties.response, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["response", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        response: typing.Union[MetaOapg.properties.response, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor204ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            response=response,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor204ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor204ResponseBodyApplicationJson),
    },
)


class SchemaFor401ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class message(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Authentication failed: request expired": "FAILED_REQUEST_EXPIRED",
                        "Authentication failed: signature or secret missing": "FAILED_SIGNATURE_OR_SECRET_MISSING",
                        "Authentication failed: workspace missing": "FAILED_WORKSPACE_MISSING",
                        "Authentication failed: key missing": "FAILED_KEY_MISSING",
                        "Authentication failed: property iss (issuer) missing in JWT": "FAILED_PROPERTY_ISS_ISSUER_MISSING_IN_JWT",
                        "Authentication failed: property sub (subject) missing in JWT": "FAILED_PROPERTY_SUB_SUBJECT_MISSING_IN_JWT",
                        "Authentication failed: property exp (expiration time) missing in JWT": "FAILED_PROPERTY_EXP_EXPIRATION_TIME_MISSING_IN_JWT",
                        "Authentication failed: invalid iss (issuer)": "FAILED_INVALID_ISS_ISSUER",
                        "Authentication failed: incorrect signature": "FAILED_INCORRECT_SIGNATURE",
                        "Authentication failed": "FAILED",
                    }
                
                @schemas.classproperty
                def FAILED_REQUEST_EXPIRED(cls):
                    return cls("Authentication failed: request expired")
                
                @schemas.classproperty
                def FAILED_SIGNATURE_OR_SECRET_MISSING(cls):
                    return cls("Authentication failed: signature or secret missing")
                
                @schemas.classproperty
                def FAILED_WORKSPACE_MISSING(cls):
                    return cls("Authentication failed: workspace missing")
                
                @schemas.classproperty
                def FAILED_KEY_MISSING(cls):
                    return cls("Authentication failed: key missing")
                
                @schemas.classproperty
                def FAILED_PROPERTY_ISS_ISSUER_MISSING_IN_JWT(cls):
                    return cls("Authentication failed: property iss (issuer) missing in JWT")
                
                @schemas.classproperty
                def FAILED_PROPERTY_SUB_SUBJECT_MISSING_IN_JWT(cls):
                    return cls("Authentication failed: property sub (subject) missing in JWT")
                
                @schemas.classproperty
                def FAILED_PROPERTY_EXP_EXPIRATION_TIME_MISSING_IN_JWT(cls):
                    return cls("Authentication failed: property exp (expiration time) missing in JWT")
                
                @schemas.classproperty
                def FAILED_INVALID_ISS_ISSUER(cls):
                    return cls("Authentication failed: invalid iss (issuer)")
                
                @schemas.classproperty
                def FAILED_INCORRECT_SIGNATURE(cls):
                    return cls("Authentication failed: incorrect signature")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("Authentication failed")
            __annotations__ = {
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor401ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)


class SchemaFor402ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class message(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Your account is suspended, please upgrade your account or contact support@pdfgeneratorapi.com": "YOUR_ACCOUNT_IS_SUSPENDED_PLEASE_UPGRADE_YOUR_ACCOUNT_OR_CONTACT_SUPPORTPDFGENERATORAPI_COM",
                    }
                
                @schemas.classproperty
                def YOUR_ACCOUNT_IS_SUSPENDED_PLEASE_UPGRADE_YOUR_ACCOUNT_OR_CONTACT_SUPPORTPDFGENERATORAPI_COM(cls):
                    return cls("Your account is suspended, please upgrade your account or contact support@pdfgeneratorapi.com")
            __annotations__ = {
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor402ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor402ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor402ResponseBodyApplicationJson),
    },
)


class SchemaFor403ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class message(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Your account has exceeded the monthly document generation limit.": "YOUR_ACCOUNT_HAS_EXCEEDED_THE_MONTHLY_DOCUMENT_GENERATION_LIMIT_",
                    }
                
                @schemas.classproperty
                def YOUR_ACCOUNT_HAS_EXCEEDED_THE_MONTHLY_DOCUMENT_GENERATION_LIMIT_(cls):
                    return cls("Your account has exceeded the monthly document generation limit.")
            __annotations__ = {
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor403ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)


class SchemaFor404ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class message(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Entity not found": "ENTITY_NOT_FOUND",
                        "Template not found": "TEMPLATE_NOT_FOUND",
                        "Resource not found": "RESOURCE_NOT_FOUND",
                        "None of the templates is available for the workspace.": "NONE_OF_THE_TEMPLATES_IS_AVAILABLE_FOR_THE_WORKSPACE_",
                    }
                
                @schemas.classproperty
                def ENTITY_NOT_FOUND(cls):
                    return cls("Entity not found")
                
                @schemas.classproperty
                def TEMPLATE_NOT_FOUND(cls):
                    return cls("Template not found")
                
                @schemas.classproperty
                def RESOURCE_NOT_FOUND(cls):
                    return cls("Resource not found")
                
                @schemas.classproperty
                def NONE_OF_THE_TEMPLATES_IS_AVAILABLE_FOR_THE_WORKSPACE_(cls):
                    return cls("None of the templates is available for the workspace.")
            __annotations__ = {
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor404ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)


class SchemaFor422ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            message = schemas.StrSchema
            errors = schemas.DictSchema
            __annotations__ = {
                "message": message,
                "errors": errors,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union[MetaOapg.properties.errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        errors: typing.Union[MetaOapg.properties.errors, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor422ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor422ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)


class SchemaFor429ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            message = schemas.StrSchema
            __annotations__ = {
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor429ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor429ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)


class SchemaFor500ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            message = schemas.StrSchema
            __annotations__ = {
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor500ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '204': _response_for_204,
    '401': _response_for_401,
    '402': _response_for_402,
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _delete_template_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor204,
    ]: ...

    @typing.overload
    def _delete_template_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _delete_template_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _delete_template_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Delete template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_template_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='delete'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class DeleteTemplate(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def delete_template(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor204,
    ]: ...

    @typing.overload
    def delete_template(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete_template(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete_template(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._delete_template_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def delete(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor204,
    ]: ...

    @typing.overload
    def delete(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._delete_template_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

