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


class RequestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_request(self, id, **kwargs):  # noqa: E501
        """Delete Request  # noqa: E501

        Delete a single Request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_request(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the request. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_request_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_request_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_request_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Request  # noqa: E501

        Delete a single Request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_request_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the request. (required)
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
                    " to method delete_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_request`")  # noqa: E501

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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/iaas/api/request-tracker/{id}', 'DELETE',
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

    def get_request_tracker(self, id, **kwargs):  # noqa: E501
        """Get request tracker  # noqa: E501

        Get request tracker with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_request_tracker(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the request. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: RequestTracker
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_request_tracker_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_request_tracker_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_request_tracker_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get request tracker  # noqa: E501

        Get request tracker with a given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_request_tracker_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the request. (required)
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: RequestTracker
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
                    " to method get_request_tracker" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_request_tracker`")  # noqa: E501

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
            '/iaas/api/request-tracker/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RequestTracker',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_request_trackers(self, **kwargs):  # noqa: E501
        """Get request tracker  # noqa: E501

        Get all request trackers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_request_trackers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: RequestTrackerResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_request_trackers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_request_trackers_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_request_trackers_with_http_info(self, **kwargs):  # noqa: E501
        """Get request tracker  # noqa: E501

        Get all request trackers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_request_trackers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the API in yyyy-MM-dd format (UTC). For versioning information refer to /iaas/api/about
        :return: RequestTrackerResult
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
                    " to method get_request_trackers" % key
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
            '/iaas/api/request-tracker', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RequestTrackerResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
