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


class StorageProfileVsphereSpecification(object):
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
        'supports_encryption': 'bool',
        'shares_level': 'str',
        'description': 'str',
        'disk_mode': 'str',
        'storage_policy_id': 'str',
        'tags': 'list[Tag]',
        'shares': 'str',
        'provisioning_type': 'str',
        'region_id': 'str',
        'limit_iops': 'str',
        'name': 'str',
        'default_item': 'bool',
        'datastore_id': 'str'
    }

    attribute_map = {
        'supports_encryption': 'supportsEncryption',
        'shares_level': 'sharesLevel',
        'description': 'description',
        'disk_mode': 'diskMode',
        'storage_policy_id': 'storagePolicyId',
        'tags': 'tags',
        'shares': 'shares',
        'provisioning_type': 'provisioningType',
        'region_id': 'regionId',
        'limit_iops': 'limitIops',
        'name': 'name',
        'default_item': 'defaultItem',
        'datastore_id': 'datastoreId'
    }

    def __init__(self, supports_encryption=None, shares_level=None, description=None, disk_mode=None, storage_policy_id=None, tags=None, shares=None, provisioning_type=None, region_id=None, limit_iops=None, name=None, default_item=None, datastore_id=None):  # noqa: E501
        """StorageProfileVsphereSpecification - a model defined in Swagger"""  # noqa: E501

        self._supports_encryption = None
        self._shares_level = None
        self._description = None
        self._disk_mode = None
        self._storage_policy_id = None
        self._tags = None
        self._shares = None
        self._provisioning_type = None
        self._region_id = None
        self._limit_iops = None
        self._name = None
        self._default_item = None
        self._datastore_id = None
        self.discriminator = None

        if supports_encryption is not None:
            self.supports_encryption = supports_encryption
        if shares_level is not None:
            self.shares_level = shares_level
        if description is not None:
            self.description = description
        if disk_mode is not None:
            self.disk_mode = disk_mode
        if storage_policy_id is not None:
            self.storage_policy_id = storage_policy_id
        if tags is not None:
            self.tags = tags
        if shares is not None:
            self.shares = shares
        if provisioning_type is not None:
            self.provisioning_type = provisioning_type
        self.region_id = region_id
        if limit_iops is not None:
            self.limit_iops = limit_iops
        self.name = name
        self.default_item = default_item
        if datastore_id is not None:
            self.datastore_id = datastore_id

    @property
    def supports_encryption(self):
        """Gets the supports_encryption of this StorageProfileVsphereSpecification.  # noqa: E501

        Indicates whether this storage profile supports encryption or not.  # noqa: E501

        :return: The supports_encryption of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._supports_encryption

    @supports_encryption.setter
    def supports_encryption(self, supports_encryption):
        """Sets the supports_encryption of this StorageProfileVsphereSpecification.

        Indicates whether this storage profile supports encryption or not.  # noqa: E501

        :param supports_encryption: The supports_encryption of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: bool
        """

        self._supports_encryption = supports_encryption

    @property
    def shares_level(self):
        """Gets the shares_level of this StorageProfileVsphereSpecification.  # noqa: E501

        Shares are specified as High, Normal, Low or Custom and these values specify share values with a 4:2:1 ratio, respectively.   # noqa: E501

        :return: The shares_level of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._shares_level

    @shares_level.setter
    def shares_level(self, shares_level):
        """Sets the shares_level of this StorageProfileVsphereSpecification.

        Shares are specified as High, Normal, Low or Custom and these values specify share values with a 4:2:1 ratio, respectively.   # noqa: E501

        :param shares_level: The shares_level of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._shares_level = shares_level

    @property
    def description(self):
        """Gets the description of this StorageProfileVsphereSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StorageProfileVsphereSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disk_mode(self):
        """Gets the disk_mode of this StorageProfileVsphereSpecification.  # noqa: E501

        Type of mode for the disk  # noqa: E501

        :return: The disk_mode of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._disk_mode

    @disk_mode.setter
    def disk_mode(self, disk_mode):
        """Sets the disk_mode of this StorageProfileVsphereSpecification.

        Type of mode for the disk  # noqa: E501

        :param disk_mode: The disk_mode of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._disk_mode = disk_mode

    @property
    def storage_policy_id(self):
        """Gets the storage_policy_id of this StorageProfileVsphereSpecification.  # noqa: E501

        Id of the vSphere Storage Policy to be applied.  # noqa: E501

        :return: The storage_policy_id of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._storage_policy_id

    @storage_policy_id.setter
    def storage_policy_id(self, storage_policy_id):
        """Sets the storage_policy_id of this StorageProfileVsphereSpecification.

        Id of the vSphere Storage Policy to be applied.  # noqa: E501

        :param storage_policy_id: The storage_policy_id of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._storage_policy_id = storage_policy_id

    @property
    def tags(self):
        """Gets the tags of this StorageProfileVsphereSpecification.  # noqa: E501

        A list of tags that represent the capabilities of this storage profile.  # noqa: E501

        :return: The tags of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StorageProfileVsphereSpecification.

        A list of tags that represent the capabilities of this storage profile.  # noqa: E501

        :param tags: The tags of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def shares(self):
        """Gets the shares of this StorageProfileVsphereSpecification.  # noqa: E501

        A specific number of shares assigned to each virtual machine.  # noqa: E501

        :return: The shares of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this StorageProfileVsphereSpecification.

        A specific number of shares assigned to each virtual machine.  # noqa: E501

        :param shares: The shares of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._shares = shares

    @property
    def provisioning_type(self):
        """Gets the provisioning_type of this StorageProfileVsphereSpecification.  # noqa: E501

        Type of provisioning policy for the disk.  # noqa: E501

        :return: The provisioning_type of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._provisioning_type

    @provisioning_type.setter
    def provisioning_type(self, provisioning_type):
        """Sets the provisioning_type of this StorageProfileVsphereSpecification.

        Type of provisioning policy for the disk.  # noqa: E501

        :param provisioning_type: The provisioning_type of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._provisioning_type = provisioning_type

    @property
    def region_id(self):
        """Gets the region_id of this StorageProfileVsphereSpecification.  # noqa: E501

        The Id of the region that is associated with the storage profile.  # noqa: E501

        :return: The region_id of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this StorageProfileVsphereSpecification.

        The Id of the region that is associated with the storage profile.  # noqa: E501

        :param region_id: The region_id of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def limit_iops(self):
        """Gets the limit_iops of this StorageProfileVsphereSpecification.  # noqa: E501

        The upper bound for the I/O operations per second allocated for each virtual disk.  # noqa: E501

        :return: The limit_iops of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._limit_iops

    @limit_iops.setter
    def limit_iops(self, limit_iops):
        """Sets the limit_iops of this StorageProfileVsphereSpecification.

        The upper bound for the I/O operations per second allocated for each virtual disk.  # noqa: E501

        :param limit_iops: The limit_iops of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._limit_iops = limit_iops

    @property
    def name(self):
        """Gets the name of this StorageProfileVsphereSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageProfileVsphereSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def default_item(self):
        """Gets the default_item of this StorageProfileVsphereSpecification.  # noqa: E501

        Indicates if a storage profile acts as a default storage profile for a disk.  # noqa: E501

        :return: The default_item of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._default_item

    @default_item.setter
    def default_item(self, default_item):
        """Sets the default_item of this StorageProfileVsphereSpecification.

        Indicates if a storage profile acts as a default storage profile for a disk.  # noqa: E501

        :param default_item: The default_item of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: bool
        """
        if default_item is None:
            raise ValueError("Invalid value for `default_item`, must not be `None`")  # noqa: E501

        self._default_item = default_item

    @property
    def datastore_id(self):
        """Gets the datastore_id of this StorageProfileVsphereSpecification.  # noqa: E501

        Id of the vSphere Datastore for placing disk and VM.  # noqa: E501

        :return: The datastore_id of this StorageProfileVsphereSpecification.  # noqa: E501
        :rtype: str
        """
        return self._datastore_id

    @datastore_id.setter
    def datastore_id(self, datastore_id):
        """Sets the datastore_id of this StorageProfileVsphereSpecification.

        Id of the vSphere Datastore for placing disk and VM.  # noqa: E501

        :param datastore_id: The datastore_id of this StorageProfileVsphereSpecification.  # noqa: E501
        :type: str
        """

        self._datastore_id = datastore_id

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
        if issubclass(StorageProfileVsphereSpecification, dict):
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
        if not isinstance(other, StorageProfileVsphereSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other