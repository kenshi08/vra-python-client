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


class AwsStorageProfile(object):
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
        'owner': 'str',
        'device_type': 'str',
        'volume_type': 'str',
        'links': 'dict(str, Href)',
        'supports_encryption': 'bool',
        'external_region_id': 'str',
        'description': 'str',
        'org_id': 'str',
        'tags': 'list[Tag]',
        'organization_id': 'str',
        'created_at': 'str',
        'name': 'str',
        'iops': 'str',
        'id': 'str',
        'default_item': 'bool',
        'updated_at': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'device_type': 'deviceType',
        'volume_type': 'volumeType',
        'links': '_links',
        'supports_encryption': 'supportsEncryption',
        'external_region_id': 'externalRegionId',
        'description': 'description',
        'org_id': 'orgId',
        'tags': 'tags',
        'organization_id': 'organizationId',
        'created_at': 'createdAt',
        'name': 'name',
        'iops': 'iops',
        'id': 'id',
        'default_item': 'defaultItem',
        'updated_at': 'updatedAt'
    }

    def __init__(self, owner=None, device_type=None, volume_type=None, links=None, supports_encryption=None, external_region_id=None, description=None, org_id=None, tags=None, organization_id=None, created_at=None, name=None, iops=None, id=None, default_item=None, updated_at=None):  # noqa: E501
        """AwsStorageProfile - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._device_type = None
        self._volume_type = None
        self._links = None
        self._supports_encryption = None
        self._external_region_id = None
        self._description = None
        self._org_id = None
        self._tags = None
        self._organization_id = None
        self._created_at = None
        self._name = None
        self._iops = None
        self._id = None
        self._default_item = None
        self._updated_at = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if device_type is not None:
            self.device_type = device_type
        if volume_type is not None:
            self.volume_type = volume_type
        self.links = links
        if supports_encryption is not None:
            self.supports_encryption = supports_encryption
        if external_region_id is not None:
            self.external_region_id = external_region_id
        if description is not None:
            self.description = description
        if org_id is not None:
            self.org_id = org_id
        if tags is not None:
            self.tags = tags
        if organization_id is not None:
            self.organization_id = organization_id
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if iops is not None:
            self.iops = iops
        self.id = id
        self.default_item = default_item
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this AwsStorageProfile.  # noqa: E501

        Email of the user that owns the entity.  # noqa: E501

        :return: The owner of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AwsStorageProfile.

        Email of the user that owns the entity.  # noqa: E501

        :param owner: The owner of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def device_type(self):
        """Gets the device_type of this AwsStorageProfile.  # noqa: E501

        Indicates the type of storage device.  # noqa: E501

        :return: The device_type of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this AwsStorageProfile.

        Indicates the type of storage device.  # noqa: E501

        :param device_type: The device_type of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def volume_type(self):
        """Gets the volume_type of this AwsStorageProfile.  # noqa: E501

        Indicates the type of volume associated with type of storage device.  # noqa: E501

        :return: The volume_type of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this AwsStorageProfile.

        Indicates the type of volume associated with type of storage device.  # noqa: E501

        :param volume_type: The volume_type of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

    @property
    def links(self):
        """Gets the links of this AwsStorageProfile.  # noqa: E501

        HATEOAS of the entity  # noqa: E501

        :return: The links of this AwsStorageProfile.  # noqa: E501
        :rtype: dict(str, Href)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AwsStorageProfile.

        HATEOAS of the entity  # noqa: E501

        :param links: The links of this AwsStorageProfile.  # noqa: E501
        :type: dict(str, Href)
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def supports_encryption(self):
        """Gets the supports_encryption of this AwsStorageProfile.  # noqa: E501

        Indicates whether this storage profile supports encryption or not.  # noqa: E501

        :return: The supports_encryption of this AwsStorageProfile.  # noqa: E501
        :rtype: bool
        """
        return self._supports_encryption

    @supports_encryption.setter
    def supports_encryption(self, supports_encryption):
        """Sets the supports_encryption of this AwsStorageProfile.

        Indicates whether this storage profile supports encryption or not.  # noqa: E501

        :param supports_encryption: The supports_encryption of this AwsStorageProfile.  # noqa: E501
        :type: bool
        """

        self._supports_encryption = supports_encryption

    @property
    def external_region_id(self):
        """Gets the external_region_id of this AwsStorageProfile.  # noqa: E501

        The id of the region for which this profile is defined  # noqa: E501

        :return: The external_region_id of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._external_region_id

    @external_region_id.setter
    def external_region_id(self, external_region_id):
        """Sets the external_region_id of this AwsStorageProfile.

        The id of the region for which this profile is defined  # noqa: E501

        :param external_region_id: The external_region_id of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._external_region_id = external_region_id

    @property
    def description(self):
        """Gets the description of this AwsStorageProfile.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwsStorageProfile.

        A human-friendly description.  # noqa: E501

        :param description: The description of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def org_id(self):
        """Gets the org_id of this AwsStorageProfile.  # noqa: E501

        The id of the organization this entity belongs to.  # noqa: E501

        :return: The org_id of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this AwsStorageProfile.

        The id of the organization this entity belongs to.  # noqa: E501

        :param org_id: The org_id of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def tags(self):
        """Gets the tags of this AwsStorageProfile.  # noqa: E501

        A list of tags that represent the capabilities of this storage profile  # noqa: E501

        :return: The tags of this AwsStorageProfile.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsStorageProfile.

        A list of tags that represent the capabilities of this storage profile  # noqa: E501

        :param tags: The tags of this AwsStorageProfile.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def organization_id(self):
        """Gets the organization_id of this AwsStorageProfile.  # noqa: E501

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :return: The organization_id of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this AwsStorageProfile.

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :param organization_id: The organization_id of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def created_at(self):
        """Gets the created_at of this AwsStorageProfile.  # noqa: E501

        Date when the entity was created. The date is in ISO 8601 and UTC.  # noqa: E501

        :return: The created_at of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AwsStorageProfile.

        Date when the entity was created. The date is in ISO 8601 and UTC.  # noqa: E501

        :param created_at: The created_at of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this AwsStorageProfile.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwsStorageProfile.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def iops(self):
        """Gets the iops of this AwsStorageProfile.  # noqa: E501

        Indicates maximum I/O operations per second in range(1-20,000).  # noqa: E501

        :return: The iops of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this AwsStorageProfile.

        Indicates maximum I/O operations per second in range(1-20,000).  # noqa: E501

        :param iops: The iops of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._iops = iops

    @property
    def id(self):
        """Gets the id of this AwsStorageProfile.  # noqa: E501

        The id of this resource instance  # noqa: E501

        :return: The id of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsStorageProfile.

        The id of this resource instance  # noqa: E501

        :param id: The id of this AwsStorageProfile.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def default_item(self):
        """Gets the default_item of this AwsStorageProfile.  # noqa: E501

        Indicates whether this storage profile is default or not..  # noqa: E501

        :return: The default_item of this AwsStorageProfile.  # noqa: E501
        :rtype: bool
        """
        return self._default_item

    @default_item.setter
    def default_item(self, default_item):
        """Sets the default_item of this AwsStorageProfile.

        Indicates whether this storage profile is default or not..  # noqa: E501

        :param default_item: The default_item of this AwsStorageProfile.  # noqa: E501
        :type: bool
        """
        if default_item is None:
            raise ValueError("Invalid value for `default_item`, must not be `None`")  # noqa: E501

        self._default_item = default_item

    @property
    def updated_at(self):
        """Gets the updated_at of this AwsStorageProfile.  # noqa: E501

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :return: The updated_at of this AwsStorageProfile.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AwsStorageProfile.

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :param updated_at: The updated_at of this AwsStorageProfile.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(AwsStorageProfile, dict):
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
        if not isinstance(other, AwsStorageProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
