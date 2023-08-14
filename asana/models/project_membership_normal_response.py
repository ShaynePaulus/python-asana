# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectMembershipNormalResponse(object):
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
        'gid': 'str',
        'resource_type': 'str',
        'parent': 'JobBaseNewProject',
        'member': 'MembershipCompactMember',
        'access_level': 'str',
        'user': 'CustomFieldResponsePeopleValue',
        'project': 'JobBaseNewProject',
        'write_access': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'parent': 'parent',
        'member': 'member',
        'access_level': 'access_level',
        'user': 'user',
        'project': 'project',
        'write_access': 'write_access'
    }

    def __init__(self, gid=None, resource_type=None, parent=None, member=None, access_level=None, user=None, project=None, write_access=None):  # noqa: E501
        """ProjectMembershipNormalResponse - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._parent = None
        self._member = None
        self._access_level = None
        self._user = None
        self._project = None
        self._write_access = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if parent is not None:
            self.parent = parent
        if member is not None:
            self.member = member
        if access_level is not None:
            self.access_level = access_level
        if user is not None:
            self.user = user
        if project is not None:
            self.project = project
        if write_access is not None:
            self.write_access = write_access

    @property
    def gid(self):
        """Gets the gid of this ProjectMembershipNormalResponse.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProjectMembershipNormalResponse.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this ProjectMembershipNormalResponse.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProjectMembershipNormalResponse.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def parent(self):
        """Gets the parent of this ProjectMembershipNormalResponse.  # noqa: E501


        :return: The parent of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: JobBaseNewProject
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ProjectMembershipNormalResponse.


        :param parent: The parent of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: JobBaseNewProject
        """

        self._parent = parent

    @property
    def member(self):
        """Gets the member of this ProjectMembershipNormalResponse.  # noqa: E501


        :return: The member of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: MembershipCompactMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this ProjectMembershipNormalResponse.


        :param member: The member of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: MembershipCompactMember
        """

        self._member = member

    @property
    def access_level(self):
        """Gets the access_level of this ProjectMembershipNormalResponse.  # noqa: E501

        Whether the member has admin, editor, commenter, or viewer access to the project.  # noqa: E501

        :return: The access_level of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this ProjectMembershipNormalResponse.

        Whether the member has admin, editor, commenter, or viewer access to the project.  # noqa: E501

        :param access_level: The access_level of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin", "editor", "commenter", "viewer"]  # noqa: E501
        if access_level not in allowed_values:
            raise ValueError(
                "Invalid value for `access_level` ({0}), must be one of {1}"  # noqa: E501
                .format(access_level, allowed_values)
            )

        self._access_level = access_level

    @property
    def user(self):
        """Gets the user of this ProjectMembershipNormalResponse.  # noqa: E501


        :return: The user of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: CustomFieldResponsePeopleValue
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ProjectMembershipNormalResponse.


        :param user: The user of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: CustomFieldResponsePeopleValue
        """

        self._user = user

    @property
    def project(self):
        """Gets the project of this ProjectMembershipNormalResponse.  # noqa: E501


        :return: The project of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: JobBaseNewProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectMembershipNormalResponse.


        :param project: The project of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: JobBaseNewProject
        """

        self._project = project

    @property
    def write_access(self):
        """Gets the write_access of this ProjectMembershipNormalResponse.  # noqa: E501

        Whether the member has full access or comment-only access to the project.  # noqa: E501

        :return: The write_access of this ProjectMembershipNormalResponse.  # noqa: E501
        :rtype: str
        """
        return self._write_access

    @write_access.setter
    def write_access(self, write_access):
        """Sets the write_access of this ProjectMembershipNormalResponse.

        Whether the member has full access or comment-only access to the project.  # noqa: E501

        :param write_access: The write_access of this ProjectMembershipNormalResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["full_write", "comment_only"]  # noqa: E501
        if write_access not in allowed_values:
            raise ValueError(
                "Invalid value for `write_access` ({0}), must be one of {1}"  # noqa: E501
                .format(write_access, allowed_values)
            )

        self._write_access = write_access

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
        if issubclass(ProjectMembershipNormalResponse, dict):
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
        if not isinstance(other, ProjectMembershipNormalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
