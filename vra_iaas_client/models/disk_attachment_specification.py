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


class DiskAttachmentSpecification(object):
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
        'block_device_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'block_device_id': 'blockDeviceId',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, block_device_id=None, name=None, description=None):  # noqa: E501
        """DiskAttachmentSpecification - a model defined in Swagger"""  # noqa: E501

        self._block_device_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.block_device_id = block_device_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def block_device_id(self):
        """Gets the block_device_id of this DiskAttachmentSpecification.  # noqa: E501

        The id of the existing block device  # noqa: E501

        :return: The block_device_id of this DiskAttachmentSpecification.  # noqa: E501
        :rtype: str
        """
        return self._block_device_id

    @block_device_id.setter
    def block_device_id(self, block_device_id):
        """Sets the block_device_id of this DiskAttachmentSpecification.

        The id of the existing block device  # noqa: E501

        :param block_device_id: The block_device_id of this DiskAttachmentSpecification.  # noqa: E501
        :type: str
        """
        if block_device_id is None:
            raise ValueError("Invalid value for `block_device_id`, must not be `None`")  # noqa: E501

        self._block_device_id = block_device_id

    @property
    def name(self):
        """Gets the name of this DiskAttachmentSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this DiskAttachmentSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiskAttachmentSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this DiskAttachmentSpecification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DiskAttachmentSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this DiskAttachmentSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DiskAttachmentSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this DiskAttachmentSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(DiskAttachmentSpecification, dict):
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
        if not isinstance(other, DiskAttachmentSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
