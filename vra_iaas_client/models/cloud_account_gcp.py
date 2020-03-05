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


class CloudAccountGcp(object):
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
        'enabled_region_ids': 'list[str]',
        'links': 'dict(str, Href)',
        'client_email': 'str',
        'description': 'str',
        'org_id': 'str',
        'tags': 'list[Tag]',
        'organization_id': 'str',
        'created_at': 'str',
        'custom_properties': 'dict(str, str)',
        'name': 'str',
        'id': 'str',
        'project_id': 'str',
        'private_key_id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'enabled_region_ids': 'enabledRegionIds',
        'links': '_links',
        'client_email': 'clientEmail',
        'description': 'description',
        'org_id': 'orgId',
        'tags': 'tags',
        'organization_id': 'organizationId',
        'created_at': 'createdAt',
        'custom_properties': 'customProperties',
        'name': 'name',
        'id': 'id',
        'project_id': 'projectId',
        'private_key_id': 'privateKeyId',
        'updated_at': 'updatedAt'
    }

    def __init__(self, owner=None, enabled_region_ids=None, links=None, client_email=None, description=None, org_id=None, tags=None, organization_id=None, created_at=None, custom_properties=None, name=None, id=None, project_id=None, private_key_id=None, updated_at=None):  # noqa: E501
        """CloudAccountGcp - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._enabled_region_ids = None
        self._links = None
        self._client_email = None
        self._description = None
        self._org_id = None
        self._tags = None
        self._organization_id = None
        self._created_at = None
        self._custom_properties = None
        self._name = None
        self._id = None
        self._project_id = None
        self._private_key_id = None
        self._updated_at = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if enabled_region_ids is not None:
            self.enabled_region_ids = enabled_region_ids
        self.links = links
        self.client_email = client_email
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
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if name is not None:
            self.name = name
        self.id = id
        self.project_id = project_id
        self.private_key_id = private_key_id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this CloudAccountGcp.  # noqa: E501

        Email of the user that owns the entity.  # noqa: E501

        :return: The owner of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CloudAccountGcp.

        Email of the user that owns the entity.  # noqa: E501

        :param owner: The owner of this CloudAccountGcp.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def enabled_region_ids(self):
        """Gets the enabled_region_ids of this CloudAccountGcp.  # noqa: E501

        A set of region names that are enabled for this   # noqa: E501

        :return: The enabled_region_ids of this CloudAccountGcp.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabled_region_ids

    @enabled_region_ids.setter
    def enabled_region_ids(self, enabled_region_ids):
        """Sets the enabled_region_ids of this CloudAccountGcp.

        A set of region names that are enabled for this   # noqa: E501

        :param enabled_region_ids: The enabled_region_ids of this CloudAccountGcp.  # noqa: E501
        :type: list[str]
        """

        self._enabled_region_ids = enabled_region_ids

    @property
    def links(self):
        """Gets the links of this CloudAccountGcp.  # noqa: E501

        HATEOAS of the entity  # noqa: E501

        :return: The links of this CloudAccountGcp.  # noqa: E501
        :rtype: dict(str, Href)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CloudAccountGcp.

        HATEOAS of the entity  # noqa: E501

        :param links: The links of this CloudAccountGcp.  # noqa: E501
        :type: dict(str, Href)
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def client_email(self):
        """Gets the client_email of this CloudAccountGcp.  # noqa: E501

        GCP Client email  # noqa: E501

        :return: The client_email of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._client_email

    @client_email.setter
    def client_email(self, client_email):
        """Sets the client_email of this CloudAccountGcp.

        GCP Client email  # noqa: E501

        :param client_email: The client_email of this CloudAccountGcp.  # noqa: E501
        :type: str
        """
        if client_email is None:
            raise ValueError("Invalid value for `client_email`, must not be `None`")  # noqa: E501

        self._client_email = client_email

    @property
    def description(self):
        """Gets the description of this CloudAccountGcp.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudAccountGcp.

        A human-friendly description.  # noqa: E501

        :param description: The description of this CloudAccountGcp.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def org_id(self):
        """Gets the org_id of this CloudAccountGcp.  # noqa: E501

        The id of the organization this entity belongs to.  # noqa: E501

        :return: The org_id of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CloudAccountGcp.

        The id of the organization this entity belongs to.  # noqa: E501

        :param org_id: The org_id of this CloudAccountGcp.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def tags(self):
        """Gets the tags of this CloudAccountGcp.  # noqa: E501

        A set of tag keys and optional values that were set on on the Cloud Account  # noqa: E501

        :return: The tags of this CloudAccountGcp.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudAccountGcp.

        A set of tag keys and optional values that were set on on the Cloud Account  # noqa: E501

        :param tags: The tags of this CloudAccountGcp.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def organization_id(self):
        """Gets the organization_id of this CloudAccountGcp.  # noqa: E501

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :return: The organization_id of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this CloudAccountGcp.

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :param organization_id: The organization_id of this CloudAccountGcp.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def created_at(self):
        """Gets the created_at of this CloudAccountGcp.  # noqa: E501

        Date when the entity was created. The date is in ISO 8601 and UTC.  # noqa: E501

        :return: The created_at of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CloudAccountGcp.

        Date when the entity was created. The date is in ISO 8601 and UTC.  # noqa: E501

        :param created_at: The created_at of this CloudAccountGcp.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def custom_properties(self):
        """Gets the custom_properties of this CloudAccountGcp.  # noqa: E501

        Additional properties that may be used to extend the base type.  # noqa: E501

        :return: The custom_properties of this CloudAccountGcp.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this CloudAccountGcp.

        Additional properties that may be used to extend the base type.  # noqa: E501

        :param custom_properties: The custom_properties of this CloudAccountGcp.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def name(self):
        """Gets the name of this CloudAccountGcp.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountGcp.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this CloudAccountGcp.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this CloudAccountGcp.  # noqa: E501

        The id of this resource instance  # noqa: E501

        :return: The id of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudAccountGcp.

        The id of this resource instance  # noqa: E501

        :param id: The id of this CloudAccountGcp.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this CloudAccountGcp.  # noqa: E501

        GCP Project ID  # noqa: E501

        :return: The project_id of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CloudAccountGcp.

        GCP Project ID  # noqa: E501

        :param project_id: The project_id of this CloudAccountGcp.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def private_key_id(self):
        """Gets the private_key_id of this CloudAccountGcp.  # noqa: E501

        GCP Private key ID  # noqa: E501

        :return: The private_key_id of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._private_key_id

    @private_key_id.setter
    def private_key_id(self, private_key_id):
        """Sets the private_key_id of this CloudAccountGcp.

        GCP Private key ID  # noqa: E501

        :param private_key_id: The private_key_id of this CloudAccountGcp.  # noqa: E501
        :type: str
        """
        if private_key_id is None:
            raise ValueError("Invalid value for `private_key_id`, must not be `None`")  # noqa: E501

        self._private_key_id = private_key_id

    @property
    def updated_at(self):
        """Gets the updated_at of this CloudAccountGcp.  # noqa: E501

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :return: The updated_at of this CloudAccountGcp.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CloudAccountGcp.

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :param updated_at: The updated_at of this CloudAccountGcp.  # noqa: E501
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
        if issubclass(CloudAccountGcp, dict):
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
        if not isinstance(other, CloudAccountGcp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other