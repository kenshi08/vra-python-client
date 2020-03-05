# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CloudAccountAwsResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'number_of_elements': 'int',
        'content': 'list[CloudAccountAws]',
        'total_elements': 'int'
    }

    attribute_map = {
        'number_of_elements': 'numberOfElements',
        'content': 'content',
        'total_elements': 'totalElements'
    }

    def __init__(self, number_of_elements=None, content=None, total_elements=None):  # noqa: E501
        """CloudAccountAwsResult - a model defined in Swagger"""  # noqa: E501

        self._number_of_elements = None
        self._content = None
        self._total_elements = None
        self.discriminator = None

        if number_of_elements is not None:
            self.number_of_elements = number_of_elements
        if content is not None:
            self.content = content
        if total_elements is not None:
            self.total_elements = total_elements

    @property
    def number_of_elements(self):
        """Gets the number_of_elements of this CloudAccountAwsResult.  # noqa: E501

        Number of elements in the current page  # noqa: E501

        :return: The number_of_elements of this CloudAccountAwsResult.  # noqa: E501
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """Sets the number_of_elements of this CloudAccountAwsResult.

        Number of elements in the current page  # noqa: E501

        :param number_of_elements: The number_of_elements of this CloudAccountAwsResult.  # noqa: E501
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def content(self):
        """Gets the content of this CloudAccountAwsResult.  # noqa: E501

        List of content items  # noqa: E501

        :return: The content of this CloudAccountAwsResult.  # noqa: E501
        :rtype: list[CloudAccountAws]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CloudAccountAwsResult.

        List of content items  # noqa: E501

        :param content: The content of this CloudAccountAwsResult.  # noqa: E501
        :type: list[CloudAccountAws]
        """

        self._content = content

    @property
    def total_elements(self):
        """Gets the total_elements of this CloudAccountAwsResult.  # noqa: E501

        Total number of elements. In some cases the field may not be populated  # noqa: E501

        :return: The total_elements of this CloudAccountAwsResult.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this CloudAccountAwsResult.

        Total number of elements. In some cases the field may not be populated  # noqa: E501

        :param total_elements: The total_elements of this CloudAccountAwsResult.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CloudAccountAwsResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudAccountAwsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
