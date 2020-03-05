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


class NetworkSpecification(object):
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
        'custom_properties': 'dict(str, str)',
        'deployment_id': 'str',
        'outbound_access': 'bool',
        'name': 'str',
        'description': 'str',
        'project_id': 'str',
        'constraints': 'list[Constraint]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'custom_properties': 'customProperties',
        'deployment_id': 'deploymentId',
        'outbound_access': 'outboundAccess',
        'name': 'name',
        'description': 'description',
        'project_id': 'projectId',
        'constraints': 'constraints',
        'tags': 'tags'
    }

    def __init__(self, custom_properties=None, deployment_id=None, outbound_access=None, name=None, description=None, project_id=None, constraints=None, tags=None):  # noqa: E501
        """NetworkSpecification - a model defined in Swagger"""  # noqa: E501

        self._custom_properties = None
        self._deployment_id = None
        self._outbound_access = None
        self._name = None
        self._description = None
        self._project_id = None
        self._constraints = None
        self._tags = None
        self.discriminator = None

        if custom_properties is not None:
            self.custom_properties = custom_properties
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if outbound_access is not None:
            self.outbound_access = outbound_access
        self.name = name
        if description is not None:
            self.description = description
        self.project_id = project_id
        if constraints is not None:
            self.constraints = constraints
        if tags is not None:
            self.tags = tags

    @property
    def custom_properties(self):
        """Gets the custom_properties of this NetworkSpecification.  # noqa: E501

        Additional custom properties that may be used to extend the network.  # noqa: E501

        :return: The custom_properties of this NetworkSpecification.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this NetworkSpecification.

        Additional custom properties that may be used to extend the network.  # noqa: E501

        :param custom_properties: The custom_properties of this NetworkSpecification.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def deployment_id(self):
        """Gets the deployment_id of this NetworkSpecification.  # noqa: E501

        The id of the deployment that is associated with this resource  # noqa: E501

        :return: The deployment_id of this NetworkSpecification.  # noqa: E501
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this NetworkSpecification.

        The id of the deployment that is associated with this resource  # noqa: E501

        :param deployment_id: The deployment_id of this NetworkSpecification.  # noqa: E501
        :type: str
        """

        self._deployment_id = deployment_id

    @property
    def outbound_access(self):
        """Gets the outbound_access of this NetworkSpecification.  # noqa: E501

        Flag to indicate if the network needs to have outbound access or not. Default is true. This field will be ignored if there is proper input for networkType customProperty  # noqa: E501

        :return: The outbound_access of this NetworkSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._outbound_access

    @outbound_access.setter
    def outbound_access(self, outbound_access):
        """Sets the outbound_access of this NetworkSpecification.

        Flag to indicate if the network needs to have outbound access or not. Default is true. This field will be ignored if there is proper input for networkType customProperty  # noqa: E501

        :param outbound_access: The outbound_access of this NetworkSpecification.  # noqa: E501
        :type: bool
        """

        self._outbound_access = outbound_access

    @property
    def name(self):
        """Gets the name of this NetworkSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this NetworkSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this NetworkSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this NetworkSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this NetworkSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetworkSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this NetworkSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this NetworkSpecification.  # noqa: E501

        The id of the project the current user belongs to.  # noqa: E501

        :return: The project_id of this NetworkSpecification.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NetworkSpecification.

        The id of the project the current user belongs to.  # noqa: E501

        :param project_id: The project_id of this NetworkSpecification.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def constraints(self):
        """Gets the constraints of this NetworkSpecification.  # noqa: E501

        Constraints that are used to drive placement policies for the network that is produced from this specification, related with the network profile. Constraint expressions are matched against tags on existing placement targets.  # noqa: E501

        :return: The constraints of this NetworkSpecification.  # noqa: E501
        :rtype: list[Constraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this NetworkSpecification.

        Constraints that are used to drive placement policies for the network that is produced from this specification, related with the network profile. Constraint expressions are matched against tags on existing placement targets.  # noqa: E501

        :param constraints: The constraints of this NetworkSpecification.  # noqa: E501
        :type: list[Constraint]
        """

        self._constraints = constraints

    @property
    def tags(self):
        """Gets the tags of this NetworkSpecification.  # noqa: E501

        A set of tag keys and optional values that should be set on any resource that is produced from this specification.  # noqa: E501

        :return: The tags of this NetworkSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NetworkSpecification.

        A set of tag keys and optional values that should be set on any resource that is produced from this specification.  # noqa: E501

        :param tags: The tags of this NetworkSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

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
        if issubclass(NetworkSpecification, dict):
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
        if not isinstance(other, NetworkSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
