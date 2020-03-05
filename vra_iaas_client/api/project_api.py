# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vra_iaas_client.api_client import ApiClient


class ProjectApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_project(self, body, **kwargs):  # noqa: E501
        """Create project  # noqa: E501

        Create project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectSpecification body: Project Specification instance (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create project  # noqa: E501

        Create project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectSpecification body: Project Specification instance (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_project(self, id, **kwargs):  # noqa: E501
        """Delete project  # noqa: E501

        Delete project with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_project_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_project_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete project  # noqa: E501

        Delete project with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project(self, id, **kwargs):  # noqa: E501
        """Get project  # noqa: E501

        Get project with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_project_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get project  # noqa: E501

        Get project with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_resource_metadata(self, id, **kwargs):  # noqa: E501
        """Get project resource metadata  # noqa: E501

        Get project resource metadata by a given project id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_resource_metadata(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: ProjectResourceMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_resource_metadata_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_resource_metadata_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_project_resource_metadata_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get project resource metadata  # noqa: E501

        Get project resource metadata by a given project id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_resource_metadata_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: ProjectResourceMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_resource_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_project_resource_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects/{id}/resource-metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectResourceMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_projects(self, **kwargs):  # noqa: E501
        """Get projects  # noqa: E501

        Get all projects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: ProjectResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_projects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_projects_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_projects_with_http_info(self, **kwargs):  # noqa: E501
        """Get projects  # noqa: E501

        Get all projects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: ProjectResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_projects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_project(self, id, body, **kwargs):  # noqa: E501
        """Update project  # noqa: E501

        Update project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param ProjectSpecification body: Project specification (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_project_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_project_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def update_project_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update project  # noqa: E501

        Update project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param ProjectSpecification body: Project specification (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_project`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_project_resource_metadata(self, id, body, **kwargs):  # noqa: E501
        """Update project resource metadata  # noqa: E501

        Update project resource metadata by a given project id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_resource_metadata(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param ProjectResourceMetadataSpecification body: Project specification (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_project_resource_metadata_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_project_resource_metadata_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def update_project_resource_metadata_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update project resource metadata  # noqa: E501

        Update project resource metadata by a given project id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_resource_metadata_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the project. (required)
        :param ProjectResourceMetadataSpecification body: Project specification (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project_resource_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_project_resource_metadata`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_project_resource_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'api_version' in params:
            query_params.append(('apiVersion', params['api_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'app/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/projects/{id}/resource-metadata', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
