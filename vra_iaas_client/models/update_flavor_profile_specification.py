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


class UpdateFlavorProfileSpecification(object):
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
        'name': 'str',
        'description': 'str',
        'flavor_mapping': 'dict(str, FabricFlavorDescription)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'flavor_mapping': 'flavorMapping'
    }

    def __init__(self, name=None, description=None, flavor_mapping=None):  # noqa: E501
        """UpdateFlavorProfileSpecification - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._flavor_mapping = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.flavor_mapping = flavor_mapping

    @property
    def name(self):
        """Gets the name of this UpdateFlavorProfileSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this UpdateFlavorProfileSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateFlavorProfileSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this UpdateFlavorProfileSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateFlavorProfileSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this UpdateFlavorProfileSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFlavorProfileSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this UpdateFlavorProfileSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def flavor_mapping(self):
        """Gets the flavor_mapping of this UpdateFlavorProfileSpecification.  # noqa: E501

        Map between global fabric flavor keys <String> and fabric flavor descriptions <FabricFlavorDescription>   # noqa: E501

        :return: The flavor_mapping of this UpdateFlavorProfileSpecification.  # noqa: E501
        :rtype: dict(str, FabricFlavorDescription)
        """
        return self._flavor_mapping

    @flavor_mapping.setter
    def flavor_mapping(self, flavor_mapping):
        """Sets the flavor_mapping of this UpdateFlavorProfileSpecification.

        Map between global fabric flavor keys <String> and fabric flavor descriptions <FabricFlavorDescription>   # noqa: E501

        :param flavor_mapping: The flavor_mapping of this UpdateFlavorProfileSpecification.  # noqa: E501
        :type: dict(str, FabricFlavorDescription)
        """
        if flavor_mapping is None:
            raise ValueError("Invalid value for `flavor_mapping`, must not be `None`")  # noqa: E501

        self._flavor_mapping = flavor_mapping

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
        if issubclass(UpdateFlavorProfileSpecification, dict):
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
        if not isinstance(other, UpdateFlavorProfileSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other