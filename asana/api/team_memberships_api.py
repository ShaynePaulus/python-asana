# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from asana.api_client import ApiClient


class TeamMembershipsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_team_membership(self, team_membership_gid, **kwargs):  # noqa: E501
        """Get a team membership  # noqa: E501

        Returns the complete team membership record for a single team membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_membership(team_membership_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_membership_gid: (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_team_membership_with_http_info(team_membership_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_membership_with_http_info(team_membership_gid, **kwargs)  # noqa: E501
            return data

    def get_team_membership_with_http_info(self, team_membership_gid, **kwargs):  # noqa: E501
        """Get a team membership  # noqa: E501

        Returns the complete team membership record for a single team membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_membership_with_http_info(team_membership_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_membership_gid: (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_membership_gid', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_membership_gid' is set
        if ('team_membership_gid' not in params or
                params['team_membership_gid'] is None):
            raise ValueError("Missing the required parameter `team_membership_gid` when calling `get_team_membership`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_membership_gid' in params:
            path_params['team_membership_gid'] = params['team_membership_gid']  # noqa: E501

        query_params = []
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/team_memberships/{team_membership_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamMembershipResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_memberships(self, **kwargs):  # noqa: E501
        """Get team memberships  # noqa: E501

        Returns compact team membership records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_memberships(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param str team: Globally unique identifier for the team.
        :param str user: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. This parameter must be used with the workspace parameter.
        :param str workspace: Globally unique identifier for the workspace. This parameter must be used with the user parameter.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_team_memberships_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_team_memberships_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_team_memberships_with_http_info(self, **kwargs):  # noqa: E501
        """Get team memberships  # noqa: E501

        Returns compact team membership records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_memberships_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param str team: Globally unique identifier for the team.
        :param str user: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. This parameter must be used with the workspace parameter.
        :param str workspace: Globally unique identifier for the workspace. This parameter must be used with the user parameter.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'team', 'user', 'workspace', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_memberships" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501
        if 'workspace' in params:
            query_params.append(('workspace', params['workspace']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/team_memberships', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamMembershipResponseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_memberships_for_team(self, team_gid, **kwargs):  # noqa: E501
        """Get memberships from a team  # noqa: E501

        Returns the compact team memberships for the team.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_memberships_for_team(team_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_gid: Globally unique identifier for the team. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_team_memberships_for_team_with_http_info(team_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_memberships_for_team_with_http_info(team_gid, **kwargs)  # noqa: E501
            return data

    def get_team_memberships_for_team_with_http_info(self, team_gid, **kwargs):  # noqa: E501
        """Get memberships from a team  # noqa: E501

        Returns the compact team memberships for the team.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_memberships_for_team_with_http_info(team_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_gid: Globally unique identifier for the team. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_gid', 'limit', 'offset', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_memberships_for_team" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_gid' is set
        if ('team_gid' not in params or
                params['team_gid'] is None):
            raise ValueError("Missing the required parameter `team_gid` when calling `get_team_memberships_for_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_gid' in params:
            path_params['team_gid'] = params['team_gid']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/teams/{team_gid}/team_memberships', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamMembershipResponseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_memberships_for_user(self, user_gid, workspace, **kwargs):  # noqa: E501
        """Get memberships from a user  # noqa: E501

        Returns the compact team membership records for the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_memberships_for_user(user_gid, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
        :param str workspace: Globally unique identifier for the workspace. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_team_memberships_for_user_with_http_info(user_gid, workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_memberships_for_user_with_http_info(user_gid, workspace, **kwargs)  # noqa: E501
            return data

    def get_team_memberships_for_user_with_http_info(self, user_gid, workspace, **kwargs):  # noqa: E501
        """Get memberships from a user  # noqa: E501

        Returns the compact team membership records for the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_memberships_for_user_with_http_info(user_gid, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
        :param str workspace: Globally unique identifier for the workspace. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TeamMembershipResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_gid', 'workspace', 'limit', 'offset', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_memberships_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_gid' is set
        if ('user_gid' not in params or
                params['user_gid'] is None):
            raise ValueError("Missing the required parameter `user_gid` when calling `get_team_memberships_for_user`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `get_team_memberships_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_gid' in params:
            path_params['user_gid'] = params['user_gid']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'workspace' in params:
            query_params.append(('workspace', params['workspace']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/users/{user_gid}/team_memberships', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamMembershipResponseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
