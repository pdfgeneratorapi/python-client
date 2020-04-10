# coding: utf-8

"""
    PDF Generator API

    # Introduction PDF Generator API allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.  The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.  # Authentication The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret. When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.  <SecurityDefinitions />  ## Accessing your API Key and Secret You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).  ## Creating a JWT JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.  The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form: ``` {Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature} ```  We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.  ### Header Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256. Property `typ` defines the type of token and it is always JWT. ``` {   \"alg\": \"HS256\",   \"typ\": \"JWT\" } ```  ### Payload The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required. It is mandatory to specify the following claims: * issuer (`iss`): Your API key * subject (`sub`): Workspace identifier  You can also specify the token expiration time (`exp`) which is timestamp in seconds since Epoch (unix epoch time). It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"exp\": 1586112639 } ```  ### Signature To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is. ``` HMACSHA256(     base64UrlEncode(header) + \".\" +     base64UrlEncode(payload),     API_SECRET) ```  ### Putting all together The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret. ``` eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q  // Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 // Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0 // Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q ```  ## Testing with JWTs You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __5 minutes__. You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications.  # Libraries and SDKs ## Postman Collection We have created a [Postman](https://www.postman.com) Collection so you can easily test all the API endpoints wihtout developing and code. You can download the collection [here](https://app.getpostman.com/run-collection/8f99146f64819f3e6db5) or just click the button below.  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8f99146f64819f3e6db5)  ## Client Libraries All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.  * [PHP Client](https://github.com/pdfgeneratorapi/php-client) * [Java Client](https://github.com/pdfgeneratorapi/java-client) * [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client) * [Python Client](https://github.com/pdfgeneratorapi/python-client) * [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)  We have validated the generated libraries, but let us know if you find any anomalies in the client code.   # noqa: E501

    The version of the OpenAPI document: 3.1.0
    Contact: support@pdfgeneratorapi.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pdf_generator_api_client.configuration import Configuration


class TemplateDefinitionNewLayout(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'format': 'str',
        'width': 'float',
        'height': 'float',
        'unit': 'str',
        'orientation': 'str',
        'roation': 'int',
        'margins': 'TemplateDefinitionNewLayoutMargins',
        'repeat_layout': 'TemplateDefinitionNewLayoutRepeatLayout',
        'empty_labels': 'int'
    }

    attribute_map = {
        'format': 'format',
        'width': 'width',
        'height': 'height',
        'unit': 'unit',
        'orientation': 'orientation',
        'roation': 'roation',
        'margins': 'margins',
        'repeat_layout': 'repeatLayout',
        'empty_labels': 'emptyLabels'
    }

    def __init__(self, format=None, width=None, height=None, unit=None, orientation=None, roation=None, margins=None, repeat_layout=None, empty_labels=None, local_vars_configuration=None):  # noqa: E501
        """TemplateDefinitionNewLayout - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._format = None
        self._width = None
        self._height = None
        self._unit = None
        self._orientation = None
        self._roation = None
        self._margins = None
        self._repeat_layout = None
        self._empty_labels = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if unit is not None:
            self.unit = unit
        if orientation is not None:
            self.orientation = orientation
        if roation is not None:
            self.roation = roation
        if margins is not None:
            self.margins = margins
        self.repeat_layout = repeat_layout
        if empty_labels is not None:
            self.empty_labels = empty_labels

    @property
    def format(self):
        """Gets the format of this TemplateDefinitionNewLayout.  # noqa: E501

        Defines template page size  # noqa: E501

        :return: The format of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TemplateDefinitionNewLayout.

        Defines template page size  # noqa: E501

        :param format: The format of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: str
        """
        allowed_values = ["A4", "letter", "custom"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def width(self):
        """Gets the width of this TemplateDefinitionNewLayout.  # noqa: E501

        Page width in units  # noqa: E501

        :return: The width of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TemplateDefinitionNewLayout.

        Page width in units  # noqa: E501

        :param width: The width of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this TemplateDefinitionNewLayout.  # noqa: E501

        Page height in units  # noqa: E501

        :return: The height of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TemplateDefinitionNewLayout.

        Page height in units  # noqa: E501

        :param height: The height of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def unit(self):
        """Gets the unit of this TemplateDefinitionNewLayout.  # noqa: E501

        Measure unit  # noqa: E501

        :return: The unit of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TemplateDefinitionNewLayout.

        Measure unit  # noqa: E501

        :param unit: The unit of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: str
        """
        allowed_values = ["cm", "in"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def orientation(self):
        """Gets the orientation of this TemplateDefinitionNewLayout.  # noqa: E501

        Page orientation  # noqa: E501

        :return: The orientation of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this TemplateDefinitionNewLayout.

        Page orientation  # noqa: E501

        :param orientation: The orientation of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: str
        """
        allowed_values = ["portrait", "landscape"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and orientation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                .format(orientation, allowed_values)
            )

        self._orientation = orientation

    @property
    def roation(self):
        """Gets the roation of this TemplateDefinitionNewLayout.  # noqa: E501

        Page rotation in degrees  # noqa: E501

        :return: The roation of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: int
        """
        return self._roation

    @roation.setter
    def roation(self, roation):
        """Sets the roation of this TemplateDefinitionNewLayout.

        Page rotation in degrees  # noqa: E501

        :param roation: The roation of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 90, 180, 270]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and roation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `roation` ({0}), must be one of {1}"  # noqa: E501
                .format(roation, allowed_values)
            )

        self._roation = roation

    @property
    def margins(self):
        """Gets the margins of this TemplateDefinitionNewLayout.  # noqa: E501


        :return: The margins of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: TemplateDefinitionNewLayoutMargins
        """
        return self._margins

    @margins.setter
    def margins(self, margins):
        """Sets the margins of this TemplateDefinitionNewLayout.


        :param margins: The margins of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: TemplateDefinitionNewLayoutMargins
        """

        self._margins = margins

    @property
    def repeat_layout(self):
        """Gets the repeat_layout of this TemplateDefinitionNewLayout.  # noqa: E501


        :return: The repeat_layout of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: TemplateDefinitionNewLayoutRepeatLayout
        """
        return self._repeat_layout

    @repeat_layout.setter
    def repeat_layout(self, repeat_layout):
        """Sets the repeat_layout of this TemplateDefinitionNewLayout.


        :param repeat_layout: The repeat_layout of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: TemplateDefinitionNewLayoutRepeatLayout
        """

        self._repeat_layout = repeat_layout

    @property
    def empty_labels(self):
        """Gets the empty_labels of this TemplateDefinitionNewLayout.  # noqa: E501

        Defines how many pages or labels should be empty  # noqa: E501

        :return: The empty_labels of this TemplateDefinitionNewLayout.  # noqa: E501
        :rtype: int
        """
        return self._empty_labels

    @empty_labels.setter
    def empty_labels(self, empty_labels):
        """Sets the empty_labels of this TemplateDefinitionNewLayout.

        Defines how many pages or labels should be empty  # noqa: E501

        :param empty_labels: The empty_labels of this TemplateDefinitionNewLayout.  # noqa: E501
        :type: int
        """

        self._empty_labels = empty_labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateDefinitionNewLayout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateDefinitionNewLayout):
            return True

        return self.to_dict() != other.to_dict()
