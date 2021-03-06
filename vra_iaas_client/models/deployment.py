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


class Deployment(object):
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
        'organization_id': 'str',
        'created_at': 'str',
        'links': 'dict(str, Href)',
        'name': 'str',
        'description': 'str',
        'id': 'str',
        'project_id': 'str',
        'org_id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'organization_id': 'organizationId',
        'created_at': 'createdAt',
        'links': '_links',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'project_id': 'projectId',
        'org_id': 'orgId',
        'updated_at': 'updatedAt'
    }

    def __init__(self, owner=None, organization_id=None, created_at=None, links=None, name=None, description=None, id=None, project_id=None, org_id=None, updated_at=None):  # noqa: E501
        """Deployment - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._organization_id = None
        self._created_at = None
        self._links = None
        self._name = None
        self._description = None
        self._id = None
        self._project_id = None
        self._org_id = None
        self._updated_at = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if organization_id is not None:
            self.organization_id = organization_id
        if created_at is not None:
            self.created_at = created_at
        self.links = links
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.id = id
        if project_id is not None:
            self.project_id = project_id
        if org_id is not None:
            self.org_id = org_id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this Deployment.  # noqa: E501

        Email of the user that owns the entity.  # noqa: E501

        :return: The owner of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Deployment.

        Email of the user that owns the entity.  # noqa: E501

        :param owner: The owner of this Deployment.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def organization_id(self):
        """Gets the organization_id of this Deployment.  # noqa: E501

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :return: The organization_id of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Deployment.

        This field is deprecated. Use orgId instead. The id of the organization this entity belongs to.  # noqa: E501

        :param organization_id: The organization_id of this Deployment.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def created_at(self):
        """Gets the created_at of this Deployment.  # noqa: E501

        Date when the entity was created. The date is in ISO 8601 and UTC.  # noqa: E501

        :return: The created_at of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Deployment.

        Date when the entity was created. The date is in ISO 8601 and UTC.  # noqa: E501

        :param created_at: The created_at of this Deployment.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def links(self):
        """Gets the links of this Deployment.  # noqa: E501

        HATEOAS of the entity  # noqa: E501

        :return: The links of this Deployment.  # noqa: E501
        :rtype: dict(str, Href)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Deployment.

        HATEOAS of the entity  # noqa: E501

        :param links: The links of this Deployment.  # noqa: E501
        :type: dict(str, Href)
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def name(self):
        """Gets the name of this Deployment.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Deployment.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this Deployment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Deployment.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Deployment.

        A human-friendly description.  # noqa: E501

        :param description: The description of this Deployment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Deployment.  # noqa: E501

        The id of this resource instance  # noqa: E501

        :return: The id of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Deployment.

        The id of this resource instance  # noqa: E501

        :param id: The id of this Deployment.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Deployment.  # noqa: E501


        :return: The project_id of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Deployment.


        :param project_id: The project_id of this Deployment.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def org_id(self):
        """Gets the org_id of this Deployment.  # noqa: E501

        The id of the organization this entity belongs to.  # noqa: E501

        :return: The org_id of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Deployment.

        The id of the organization this entity belongs to.  # noqa: E501

        :param org_id: The org_id of this Deployment.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def updated_at(self):
        """Gets the updated_at of this Deployment.  # noqa: E501

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :return: The updated_at of this Deployment.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Deployment.

        Date when the entity was last updated. The date is ISO 8601 and UTC.  # noqa: E501

        :param updated_at: The updated_at of this Deployment.  # noqa: E501
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
        if issubclass(Deployment, dict):
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
        if not isinstance(other, Deployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
