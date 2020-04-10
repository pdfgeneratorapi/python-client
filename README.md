# pdf-generator-api
# Introduction
PDF Generator API allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.

The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.

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

You can also specify the token expiration time (`exp`) which is timestamp in seconds since Epoch (unix epoch time). It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.

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

## Testing with JWTs
You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __5 minutes__.
You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications.

# Libraries and SDKs
## Postman Collection
We have created a [Postman](https://www.postman.com) Collection so you can easily test all the API endpoints wihtout developing and code. You can download the collection [here](https://app.getpostman.com/run-collection/8f99146f64819f3e6db5) or just click the button below.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8f99146f64819f3e6db5)

## Client Libraries
All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.

* [PHP Client](https://github.com/pdfgeneratorapi/php-client)
* [Java Client](https://github.com/pdfgeneratorapi/java-client)
* [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client)
* [Python Client](https://github.com/pdfgeneratorapi/python-client)
* [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)

We have validated the generated libraries, but let us know if you find any anomalies in the client code.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.pdfgeneratorapi.com](https://support.pdfgeneratorapi.com)

## Requirements.

Python 2.7 and 3.4+

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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pdf_generator_api_client
from pdf_generator_api_client.rest import ApiException
from pprint import pprint

configuration = pdf_generator_api_client.Configuration()
# Configure Bearer authorization (JWT): JSONWebTokenAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"

# Defining host is optional and default to https://us1.pdfgeneratorapi.com/api/v3
configuration.host = "https://us1.pdfgeneratorapi.com/api/v3"
# Enter a context with an instance of the API client
with pdf_generator_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdf_generator_api_client.TemplatesApi(api_client)
    template_id = 19375 # int | Template unique identifier
name = 'My copied template' # str | Name for the copied template. If name is not specified then the original name is used. (optional)

    try:
        # Copy template
        api_response = api_instance.copy_template(template_id, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TemplatesApi->copy_template: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TemplatesApi* | [**copy_template**](docs/TemplatesApi.md#copy_template) | **POST** /templates/{templateId}/copy | Copy template
*TemplatesApi* | [**create_template**](docs/TemplatesApi.md#create_template) | **POST** /templates | Create template
*TemplatesApi* | [**delete_template**](docs/TemplatesApi.md#delete_template) | **DELETE** /templates/{templateId} | Delete template
*TemplatesApi* | [**get_editor_url**](docs/TemplatesApi.md#get_editor_url) | **POST** /templates/{templateId}/editor | Open editor
*TemplatesApi* | [**get_template**](docs/TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Get template
*TemplatesApi* | [**get_templates**](docs/TemplatesApi.md#get_templates) | **GET** /templates | Get templates
*TemplatesApi* | [**merge_template**](docs/TemplatesApi.md#merge_template) | **POST** /templates/{templateId}/output | Merge template
*TemplatesApi* | [**merge_templates**](docs/TemplatesApi.md#merge_templates) | **POST** /templates/output | Merge multiple templates
*TemplatesApi* | [**update_template**](docs/TemplatesApi.md#update_template) | **PUT** /templates/{templateId} | Update template
*WorkspacesApi* | [**delete_workspace**](docs/WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspaceId} | Delete workspace
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspaceId} | Get workspace


## Documentation For Models

 - [Component](docs/Component.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2002Response](docs/InlineResponse2002Response.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2004Meta](docs/InlineResponse2004Meta.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse401](docs/InlineResponse401.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [InlineResponse422](docs/InlineResponse422.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [Template](docs/Template.md)
 - [TemplateDefinition](docs/TemplateDefinition.md)
 - [TemplateDefinitionDataSettings](docs/TemplateDefinitionDataSettings.md)
 - [TemplateDefinitionEditor](docs/TemplateDefinitionEditor.md)
 - [TemplateDefinitionNew](docs/TemplateDefinitionNew.md)
 - [TemplateDefinitionNewLayout](docs/TemplateDefinitionNewLayout.md)
 - [TemplateDefinitionNewLayoutMargins](docs/TemplateDefinitionNewLayoutMargins.md)
 - [TemplateDefinitionNewLayoutRepeatLayout](docs/TemplateDefinitionNewLayoutRepeatLayout.md)
 - [TemplateDefinitionNewMargins](docs/TemplateDefinitionNewMargins.md)
 - [TemplateDefinitionNewPages](docs/TemplateDefinitionNewPages.md)
 - [Workspace](docs/Workspace.md)


## Documentation For Authorization


## JSONWebTokenAuth

- **Type**: Bearer authentication (JWT)


## Author

support@pdfgeneratorapi.com


