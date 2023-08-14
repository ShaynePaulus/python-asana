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


class UserTaskListsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user_task_list(self, user_task_list_gid, **kwargs):  # noqa: E501
        """Get a user task list  # noqa: E501

        Returns the full record for a user task list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_task_list(user_task_list_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_task_list_gid: Globally unique identifier for the user task list. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: UserTaskListResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_user_task_list_with_http_info(user_task_list_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_task_list_with_http_info(user_task_list_gid, **kwargs)  # noqa: E501
            return data

    def get_user_task_list_with_http_info(self, user_task_list_gid, **kwargs):  # noqa: E501
        """Get a user task list  # noqa: E501

        Returns the full record for a user task list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_task_list_with_http_info(user_task_list_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_task_list_gid: Globally unique identifier for the user task list. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: UserTaskListResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_task_list_gid', 'opt_fields']  # noqa: E501
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
                    " to method get_user_task_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_task_list_gid' is set
        if ('user_task_list_gid' not in params or
                params['user_task_list_gid'] is None):
            raise ValueError("Missing the required parameter `user_task_list_gid` when calling `get_user_task_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_task_list_gid' in params:
            path_params['user_task_list_gid'] = params['user_task_list_gid']  # noqa: E501

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
            '/user_task_lists/{user_task_list_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserTaskListResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_task_list_for_user(self, user_gid, workspace, **kwargs):  # noqa: E501
        """Get a user's task list  # noqa: E501

        Returns the full record for a user's task list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_task_list_for_user(user_gid, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
        :param str workspace: The workspace in which to get the user task list. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: UserTaskListResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_user_task_list_for_user_with_http_info(user_gid, workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_task_list_for_user_with_http_info(user_gid, workspace, **kwargs)  # noqa: E501
            return data

    def get_user_task_list_for_user_with_http_info(self, user_gid, workspace, **kwargs):  # noqa: E501
        """Get a user's task list  # noqa: E501

        Returns the full record for a user's task list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_task_list_for_user_with_http_info(user_gid, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
        :param str workspace: The workspace in which to get the user task list. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: UserTaskListResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_gid', 'workspace', 'opt_fields']  # noqa: E501
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
                    " to method get_user_task_list_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_gid' is set
        if ('user_gid' not in params or
                params['user_gid'] is None):
            raise ValueError("Missing the required parameter `user_gid` when calling `get_user_task_list_for_user`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `get_user_task_list_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_gid' in params:
            path_params['user_gid'] = params['user_gid']  # noqa: E501

        query_params = []
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
            '/users/{user_gid}/user_task_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserTaskListResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
