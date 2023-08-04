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

class TaskBase(object):
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
        'name': 'str',
        'resource_subtype': 'str',
        'created_by': 'AttachmentResponseParentCreatedBy',
        'approval_status': 'str',
        'assignee_status': 'str',
        'completed': 'bool',
        'completed_at': 'datetime',
        'completed_by': 'TaskBaseCompletedBy',
        'created_at': 'datetime',
        'dependencies': 'list[TaskBaseDependencies]',
        'dependents': 'list[TaskBaseDependencies]',
        'due_at': 'datetime',
        'due_on': 'date',
        'external': 'TaskBaseExternal',
        'html_notes': 'str',
        'hearted': 'bool',
        'hearts': 'list[GoalResponseLikes]',
        'is_rendered_as_separator': 'bool',
        'liked': 'bool',
        'likes': 'list[GoalResponseLikes]',
        'memberships': 'list[TaskBaseMemberships]',
        'modified_at': 'datetime',
        'notes': 'str',
        'num_hearts': 'int',
        'num_likes': 'int',
        'num_subtasks': 'int',
        'start_at': 'datetime',
        'start_on': 'date',
        'actual_time_minutes': 'float'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'resource_subtype': 'resource_subtype',
        'created_by': 'created_by',
        'approval_status': 'approval_status',
        'assignee_status': 'assignee_status',
        'completed': 'completed',
        'completed_at': 'completed_at',
        'completed_by': 'completed_by',
        'created_at': 'created_at',
        'dependencies': 'dependencies',
        'dependents': 'dependents',
        'due_at': 'due_at',
        'due_on': 'due_on',
        'external': 'external',
        'html_notes': 'html_notes',
        'hearted': 'hearted',
        'hearts': 'hearts',
        'is_rendered_as_separator': 'is_rendered_as_separator',
        'liked': 'liked',
        'likes': 'likes',
        'memberships': 'memberships',
        'modified_at': 'modified_at',
        'notes': 'notes',
        'num_hearts': 'num_hearts',
        'num_likes': 'num_likes',
        'num_subtasks': 'num_subtasks',
        'start_at': 'start_at',
        'start_on': 'start_on',
        'actual_time_minutes': 'actual_time_minutes'
    }

    def __init__(self, gid=None, resource_type=None, name=None, resource_subtype=None, created_by=None, approval_status=None, assignee_status=None, completed=None, completed_at=None, completed_by=None, created_at=None, dependencies=None, dependents=None, due_at=None, due_on=None, external=None, html_notes=None, hearted=None, hearts=None, is_rendered_as_separator=None, liked=None, likes=None, memberships=None, modified_at=None, notes=None, num_hearts=None, num_likes=None, num_subtasks=None, start_at=None, start_on=None, actual_time_minutes=None):  # noqa: E501
        """TaskBase - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._resource_subtype = None
        self._created_by = None
        self._approval_status = None
        self._assignee_status = None
        self._completed = None
        self._completed_at = None
        self._completed_by = None
        self._created_at = None
        self._dependencies = None
        self._dependents = None
        self._due_at = None
        self._due_on = None
        self._external = None
        self._html_notes = None
        self._hearted = None
        self._hearts = None
        self._is_rendered_as_separator = None
        self._liked = None
        self._likes = None
        self._memberships = None
        self._modified_at = None
        self._notes = None
        self._num_hearts = None
        self._num_likes = None
        self._num_subtasks = None
        self._start_at = None
        self._start_on = None
        self._actual_time_minutes = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype
        if created_by is not None:
            self.created_by = created_by
        if approval_status is not None:
            self.approval_status = approval_status
        if assignee_status is not None:
            self.assignee_status = assignee_status
        if completed is not None:
            self.completed = completed
        if completed_at is not None:
            self.completed_at = completed_at
        if completed_by is not None:
            self.completed_by = completed_by
        if created_at is not None:
            self.created_at = created_at
        if dependencies is not None:
            self.dependencies = dependencies
        if dependents is not None:
            self.dependents = dependents
        if due_at is not None:
            self.due_at = due_at
        if due_on is not None:
            self.due_on = due_on
        if external is not None:
            self.external = external
        if html_notes is not None:
            self.html_notes = html_notes
        if hearted is not None:
            self.hearted = hearted
        if hearts is not None:
            self.hearts = hearts
        if is_rendered_as_separator is not None:
            self.is_rendered_as_separator = is_rendered_as_separator
        if liked is not None:
            self.liked = liked
        if likes is not None:
            self.likes = likes
        if memberships is not None:
            self.memberships = memberships
        if modified_at is not None:
            self.modified_at = modified_at
        if notes is not None:
            self.notes = notes
        if num_hearts is not None:
            self.num_hearts = num_hearts
        if num_likes is not None:
            self.num_likes = num_likes
        if num_subtasks is not None:
            self.num_subtasks = num_subtasks
        if start_at is not None:
            self.start_at = start_at
        if start_on is not None:
            self.start_on = start_on
        if actual_time_minutes is not None:
            self.actual_time_minutes = actual_time_minutes

    @property
    def gid(self):
        """Gets the gid of this TaskBase.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this TaskBase.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this TaskBase.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this TaskBase.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TaskBase.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this TaskBase.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this TaskBase.  # noqa: E501

        Name of the task. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer.  # noqa: E501

        :return: The name of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskBase.

        Name of the task. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer.  # noqa: E501

        :param name: The name of this TaskBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this TaskBase.  # noqa: E501

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The resource_subtype `milestone` represent a single moment in time. This means tasks with this subtype cannot have a start_date.  # noqa: E501

        :return: The resource_subtype of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this TaskBase.

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The resource_subtype `milestone` represent a single moment in time. This means tasks with this subtype cannot have a start_date.  # noqa: E501

        :param resource_subtype: The resource_subtype of this TaskBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["default_task", "milestone", "section", "approval"]  # noqa: E501
        if resource_subtype not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_subtype` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_subtype, allowed_values)
            )

        self._resource_subtype = resource_subtype

    @property
    def created_by(self):
        """Gets the created_by of this TaskBase.  # noqa: E501


        :return: The created_by of this TaskBase.  # noqa: E501
        :rtype: AttachmentResponseParentCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TaskBase.


        :param created_by: The created_by of this TaskBase.  # noqa: E501
        :type: AttachmentResponseParentCreatedBy
        """

        self._created_by = created_by

    @property
    def approval_status(self):
        """Gets the approval_status of this TaskBase.  # noqa: E501

        *Conditional* Reflects the approval status of this task. This field is kept in sync with `completed`, meaning `pending` translates to false while `approved`, `rejected`, and `changes_requested` translate to true. If you set completed to true, this field will be set to `approved`.  # noqa: E501

        :return: The approval_status of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this TaskBase.

        *Conditional* Reflects the approval status of this task. This field is kept in sync with `completed`, meaning `pending` translates to false while `approved`, `rejected`, and `changes_requested` translate to true. If you set completed to true, this field will be set to `approved`.  # noqa: E501

        :param approval_status: The approval_status of this TaskBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "approved", "rejected", "changes_requested"]  # noqa: E501
        if approval_status not in allowed_values:
            raise ValueError(
                "Invalid value for `approval_status` ({0}), must be one of {1}"  # noqa: E501
                .format(approval_status, allowed_values)
            )

        self._approval_status = approval_status

    @property
    def assignee_status(self):
        """Gets the assignee_status of this TaskBase.  # noqa: E501

        *Deprecated* Scheduling status of this task for the user it is assigned to. This field can only be set if the assignee is non-null. Setting this field to \"inbox\" or \"upcoming\" inserts it at the top of the section, while the other options will insert at the bottom.  # noqa: E501

        :return: The assignee_status of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._assignee_status

    @assignee_status.setter
    def assignee_status(self, assignee_status):
        """Sets the assignee_status of this TaskBase.

        *Deprecated* Scheduling status of this task for the user it is assigned to. This field can only be set if the assignee is non-null. Setting this field to \"inbox\" or \"upcoming\" inserts it at the top of the section, while the other options will insert at the bottom.  # noqa: E501

        :param assignee_status: The assignee_status of this TaskBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["today", "upcoming", "later", "new", "inbox"]  # noqa: E501
        if assignee_status not in allowed_values:
            raise ValueError(
                "Invalid value for `assignee_status` ({0}), must be one of {1}"  # noqa: E501
                .format(assignee_status, allowed_values)
            )

        self._assignee_status = assignee_status

    @property
    def completed(self):
        """Gets the completed of this TaskBase.  # noqa: E501

        True if the task is currently marked complete, false if not.  # noqa: E501

        :return: The completed of this TaskBase.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this TaskBase.

        True if the task is currently marked complete, false if not.  # noqa: E501

        :param completed: The completed of this TaskBase.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def completed_at(self):
        """Gets the completed_at of this TaskBase.  # noqa: E501

        The time at which this task was completed, or null if the task is incomplete.  # noqa: E501

        :return: The completed_at of this TaskBase.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this TaskBase.

        The time at which this task was completed, or null if the task is incomplete.  # noqa: E501

        :param completed_at: The completed_at of this TaskBase.  # noqa: E501
        :type: datetime
        """

        self._completed_at = completed_at

    @property
    def completed_by(self):
        """Gets the completed_by of this TaskBase.  # noqa: E501


        :return: The completed_by of this TaskBase.  # noqa: E501
        :rtype: TaskBaseCompletedBy
        """
        return self._completed_by

    @completed_by.setter
    def completed_by(self, completed_by):
        """Sets the completed_by of this TaskBase.


        :param completed_by: The completed_by of this TaskBase.  # noqa: E501
        :type: TaskBaseCompletedBy
        """

        self._completed_by = completed_by

    @property
    def created_at(self):
        """Gets the created_at of this TaskBase.  # noqa: E501

        The time at which this resource was created.  # noqa: E501

        :return: The created_at of this TaskBase.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskBase.

        The time at which this resource was created.  # noqa: E501

        :param created_at: The created_at of this TaskBase.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def dependencies(self):
        """Gets the dependencies of this TaskBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). Array of resources referencing tasks that this task depends on. The objects contain only the gid of the dependency.  # noqa: E501

        :return: The dependencies of this TaskBase.  # noqa: E501
        :rtype: list[TaskBaseDependencies]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this TaskBase.

        [Opt In](/docs/inputoutput-options). Array of resources referencing tasks that this task depends on. The objects contain only the gid of the dependency.  # noqa: E501

        :param dependencies: The dependencies of this TaskBase.  # noqa: E501
        :type: list[TaskBaseDependencies]
        """

        self._dependencies = dependencies

    @property
    def dependents(self):
        """Gets the dependents of this TaskBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). Array of resources referencing tasks that depend on this task. The objects contain only the ID of the dependent.  # noqa: E501

        :return: The dependents of this TaskBase.  # noqa: E501
        :rtype: list[TaskBaseDependencies]
        """
        return self._dependents

    @dependents.setter
    def dependents(self, dependents):
        """Sets the dependents of this TaskBase.

        [Opt In](/docs/inputoutput-options). Array of resources referencing tasks that depend on this task. The objects contain only the ID of the dependent.  # noqa: E501

        :param dependents: The dependents of this TaskBase.  # noqa: E501
        :type: list[TaskBaseDependencies]
        """

        self._dependents = dependents

    @property
    def due_at(self):
        """Gets the due_at of this TaskBase.  # noqa: E501

        The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with `due_on`.  # noqa: E501

        :return: The due_at of this TaskBase.  # noqa: E501
        :rtype: datetime
        """
        return self._due_at

    @due_at.setter
    def due_at(self, due_at):
        """Sets the due_at of this TaskBase.

        The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with `due_on`.  # noqa: E501

        :param due_at: The due_at of this TaskBase.  # noqa: E501
        :type: datetime
        """

        self._due_at = due_at

    @property
    def due_on(self):
        """Gets the due_on of this TaskBase.  # noqa: E501

        The localized date on which this task is due, or null if the task has no due date. This takes a date with `YYYY-MM-DD` format and should not be used together with `due_at`.  # noqa: E501

        :return: The due_on of this TaskBase.  # noqa: E501
        :rtype: date
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this TaskBase.

        The localized date on which this task is due, or null if the task has no due date. This takes a date with `YYYY-MM-DD` format and should not be used together with `due_at`.  # noqa: E501

        :param due_on: The due_on of this TaskBase.  # noqa: E501
        :type: date
        """

        self._due_on = due_on

    @property
    def external(self):
        """Gets the external of this TaskBase.  # noqa: E501


        :return: The external of this TaskBase.  # noqa: E501
        :rtype: TaskBaseExternal
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this TaskBase.


        :param external: The external of this TaskBase.  # noqa: E501
        :type: TaskBaseExternal
        """

        self._external = external

    @property
    def html_notes(self):
        """Gets the html_notes of this TaskBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). The notes of the text with formatting as HTML.  # noqa: E501

        :return: The html_notes of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._html_notes

    @html_notes.setter
    def html_notes(self, html_notes):
        """Sets the html_notes of this TaskBase.

        [Opt In](/docs/inputoutput-options). The notes of the text with formatting as HTML.  # noqa: E501

        :param html_notes: The html_notes of this TaskBase.  # noqa: E501
        :type: str
        """

        self._html_notes = html_notes

    @property
    def hearted(self):
        """Gets the hearted of this TaskBase.  # noqa: E501

        *Deprecated - please use liked instead* True if the task is hearted by the authorized user, false if not.  # noqa: E501

        :return: The hearted of this TaskBase.  # noqa: E501
        :rtype: bool
        """
        return self._hearted

    @hearted.setter
    def hearted(self, hearted):
        """Sets the hearted of this TaskBase.

        *Deprecated - please use liked instead* True if the task is hearted by the authorized user, false if not.  # noqa: E501

        :param hearted: The hearted of this TaskBase.  # noqa: E501
        :type: bool
        """

        self._hearted = hearted

    @property
    def hearts(self):
        """Gets the hearts of this TaskBase.  # noqa: E501

        *Deprecated - please use likes instead* Array of likes for users who have hearted this task.  # noqa: E501

        :return: The hearts of this TaskBase.  # noqa: E501
        :rtype: list[GoalResponseLikes]
        """
        return self._hearts

    @hearts.setter
    def hearts(self, hearts):
        """Sets the hearts of this TaskBase.

        *Deprecated - please use likes instead* Array of likes for users who have hearted this task.  # noqa: E501

        :param hearts: The hearts of this TaskBase.  # noqa: E501
        :type: list[GoalResponseLikes]
        """

        self._hearts = hearts

    @property
    def is_rendered_as_separator(self):
        """Gets the is_rendered_as_separator of this TaskBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). In some contexts tasks can be rendered as a visual separator; for instance, subtasks can appear similar to [sections](/reference/sections) without being true `section` objects. If a `task` object is rendered this way in any context it will have the property `is_rendered_as_separator` set to `true`.  # noqa: E501

        :return: The is_rendered_as_separator of this TaskBase.  # noqa: E501
        :rtype: bool
        """
        return self._is_rendered_as_separator

    @is_rendered_as_separator.setter
    def is_rendered_as_separator(self, is_rendered_as_separator):
        """Sets the is_rendered_as_separator of this TaskBase.

        [Opt In](/docs/inputoutput-options). In some contexts tasks can be rendered as a visual separator; for instance, subtasks can appear similar to [sections](/reference/sections) without being true `section` objects. If a `task` object is rendered this way in any context it will have the property `is_rendered_as_separator` set to `true`.  # noqa: E501

        :param is_rendered_as_separator: The is_rendered_as_separator of this TaskBase.  # noqa: E501
        :type: bool
        """

        self._is_rendered_as_separator = is_rendered_as_separator

    @property
    def liked(self):
        """Gets the liked of this TaskBase.  # noqa: E501

        True if the task is liked by the authorized user, false if not.  # noqa: E501

        :return: The liked of this TaskBase.  # noqa: E501
        :rtype: bool
        """
        return self._liked

    @liked.setter
    def liked(self, liked):
        """Sets the liked of this TaskBase.

        True if the task is liked by the authorized user, false if not.  # noqa: E501

        :param liked: The liked of this TaskBase.  # noqa: E501
        :type: bool
        """

        self._liked = liked

    @property
    def likes(self):
        """Gets the likes of this TaskBase.  # noqa: E501

        Array of likes for users who have liked this task.  # noqa: E501

        :return: The likes of this TaskBase.  # noqa: E501
        :rtype: list[GoalResponseLikes]
        """
        return self._likes

    @likes.setter
    def likes(self, likes):
        """Sets the likes of this TaskBase.

        Array of likes for users who have liked this task.  # noqa: E501

        :param likes: The likes of this TaskBase.  # noqa: E501
        :type: list[GoalResponseLikes]
        """

        self._likes = likes

    @property
    def memberships(self):
        """Gets the memberships of this TaskBase.  # noqa: E501

        *Create-only*. Array of projects this task is associated with and the section it is in. At task creation time, this array can be used to add the task to specific sections. After task creation, these associations can be modified using the `addProject` and `removeProject` endpoints. Note that over time, more types of memberships may be added to this property.  # noqa: E501

        :return: The memberships of this TaskBase.  # noqa: E501
        :rtype: list[TaskBaseMemberships]
        """
        return self._memberships

    @memberships.setter
    def memberships(self, memberships):
        """Sets the memberships of this TaskBase.

        *Create-only*. Array of projects this task is associated with and the section it is in. At task creation time, this array can be used to add the task to specific sections. After task creation, these associations can be modified using the `addProject` and `removeProject` endpoints. Note that over time, more types of memberships may be added to this property.  # noqa: E501

        :param memberships: The memberships of this TaskBase.  # noqa: E501
        :type: list[TaskBaseMemberships]
        """

        self._memberships = memberships

    @property
    def modified_at(self):
        """Gets the modified_at of this TaskBase.  # noqa: E501

        The time at which this task was last modified.  The following conditions will change `modified_at`:  - story is created on a task - story is trashed on a task - attachment is trashed on a task - task is assigned or unassigned - custom field value is changed - the task itself is trashed - Or if any of the following fields are updated:   - completed   - name   - due_date   - description   - attachments   - items   - schedule_status  The following conditions will _not_ change `modified_at`:  - moving to a new container (project, portfolio, etc) - comments being added to the task (but the stories they generate   _will_ affect `modified_at`)  # noqa: E501

        :return: The modified_at of this TaskBase.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this TaskBase.

        The time at which this task was last modified.  The following conditions will change `modified_at`:  - story is created on a task - story is trashed on a task - attachment is trashed on a task - task is assigned or unassigned - custom field value is changed - the task itself is trashed - Or if any of the following fields are updated:   - completed   - name   - due_date   - description   - attachments   - items   - schedule_status  The following conditions will _not_ change `modified_at`:  - moving to a new container (project, portfolio, etc) - comments being added to the task (but the stories they generate   _will_ affect `modified_at`)  # noqa: E501

        :param modified_at: The modified_at of this TaskBase.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def notes(self):
        """Gets the notes of this TaskBase.  # noqa: E501

        Free-form textual information associated with the task (i.e. its description).  # noqa: E501

        :return: The notes of this TaskBase.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this TaskBase.

        Free-form textual information associated with the task (i.e. its description).  # noqa: E501

        :param notes: The notes of this TaskBase.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def num_hearts(self):
        """Gets the num_hearts of this TaskBase.  # noqa: E501

        *Deprecated - please use likes instead* The number of users who have hearted this task.  # noqa: E501

        :return: The num_hearts of this TaskBase.  # noqa: E501
        :rtype: int
        """
        return self._num_hearts

    @num_hearts.setter
    def num_hearts(self, num_hearts):
        """Sets the num_hearts of this TaskBase.

        *Deprecated - please use likes instead* The number of users who have hearted this task.  # noqa: E501

        :param num_hearts: The num_hearts of this TaskBase.  # noqa: E501
        :type: int
        """

        self._num_hearts = num_hearts

    @property
    def num_likes(self):
        """Gets the num_likes of this TaskBase.  # noqa: E501

        The number of users who have liked this task.  # noqa: E501

        :return: The num_likes of this TaskBase.  # noqa: E501
        :rtype: int
        """
        return self._num_likes

    @num_likes.setter
    def num_likes(self, num_likes):
        """Sets the num_likes of this TaskBase.

        The number of users who have liked this task.  # noqa: E501

        :param num_likes: The num_likes of this TaskBase.  # noqa: E501
        :type: int
        """

        self._num_likes = num_likes

    @property
    def num_subtasks(self):
        """Gets the num_subtasks of this TaskBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). The number of subtasks on this task.   # noqa: E501

        :return: The num_subtasks of this TaskBase.  # noqa: E501
        :rtype: int
        """
        return self._num_subtasks

    @num_subtasks.setter
    def num_subtasks(self, num_subtasks):
        """Sets the num_subtasks of this TaskBase.

        [Opt In](/docs/inputoutput-options). The number of subtasks on this task.   # noqa: E501

        :param num_subtasks: The num_subtasks of this TaskBase.  # noqa: E501
        :type: int
        """

        self._num_subtasks = num_subtasks

    @property
    def start_at(self):
        """Gets the start_at of this TaskBase.  # noqa: E501

        Date and time on which work begins for the task, or null if the task has no start time. This takes an ISO 8601 date string in UTC and should not be used together with `start_on`. *Note: `due_at` must be present in the request when setting or unsetting the `start_at` parameter.*  # noqa: E501

        :return: The start_at of this TaskBase.  # noqa: E501
        :rtype: datetime
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this TaskBase.

        Date and time on which work begins for the task, or null if the task has no start time. This takes an ISO 8601 date string in UTC and should not be used together with `start_on`. *Note: `due_at` must be present in the request when setting or unsetting the `start_at` parameter.*  # noqa: E501

        :param start_at: The start_at of this TaskBase.  # noqa: E501
        :type: datetime
        """

        self._start_at = start_at

    @property
    def start_on(self):
        """Gets the start_on of this TaskBase.  # noqa: E501

        The day on which work begins for the task , or null if the task has no start date. This takes a date with `YYYY-MM-DD` format and should not be used together with `start_at`. *Note: `due_on` or `due_at` must be present in the request when setting or unsetting the `start_on` parameter.*  # noqa: E501

        :return: The start_on of this TaskBase.  # noqa: E501
        :rtype: date
        """
        return self._start_on

    @start_on.setter
    def start_on(self, start_on):
        """Sets the start_on of this TaskBase.

        The day on which work begins for the task , or null if the task has no start date. This takes a date with `YYYY-MM-DD` format and should not be used together with `start_at`. *Note: `due_on` or `due_at` must be present in the request when setting or unsetting the `start_on` parameter.*  # noqa: E501

        :param start_on: The start_on of this TaskBase.  # noqa: E501
        :type: date
        """

        self._start_on = start_on

    @property
    def actual_time_minutes(self):
        """Gets the actual_time_minutes of this TaskBase.  # noqa: E501

        This value represents the sum of all the Time Tracking entries in the Actual Time field on a given Task. It is represented as a nullable long value.  # noqa: E501

        :return: The actual_time_minutes of this TaskBase.  # noqa: E501
        :rtype: float
        """
        return self._actual_time_minutes

    @actual_time_minutes.setter
    def actual_time_minutes(self, actual_time_minutes):
        """Sets the actual_time_minutes of this TaskBase.

        This value represents the sum of all the Time Tracking entries in the Actual Time field on a given Task. It is represented as a nullable long value.  # noqa: E501

        :param actual_time_minutes: The actual_time_minutes of this TaskBase.  # noqa: E501
        :type: float
        """

        self._actual_time_minutes = actual_time_minutes

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
        if issubclass(TaskBase, dict):
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
        if not isinstance(other, TaskBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
