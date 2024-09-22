# -*- coding=utf-8 -*-
import time
import gcpayz
from gcpayz import error
from gcpayz.http_client import HttpClient

class ApiRequestor(object):
    @classmethod
    def request(cls, method, url, params):
        """
        执行请求
        :param method: 请求方式
        :param url: 请求地址
        :param params: 请求参数
        :return: 返回响应结果
        """
        retry_count = 0
        while True:
            retry_count += 1
            response = cls.request_raw(method, url, params)
            result = cls.interpret_response(response)
            if result:
                return result
            elif retry_count == gcpayz.max_network_retries:
                raise error.APIError(
                    "HTTP response code was {}".format(response.status_code)
                )
            else:
                print("第{}次执行".format(retry_count))
                time.sleep(gcpayz.network_retry_delay)

    @staticmethod
    def request_raw(method, url, params):
        """
        处理请求信息
        :param method: 请求方式
        :param url: 请求地址
        :param params: 请求参数
        :return: 返回响应信息
        """
        if method == 'GET' or method == 'DELETE' or method == 'POST' or method == 'PUT':
            try:
                return HttpClient.request(method, url, params)
            except Exception as e:
                raise error.RequestError("Invalid Request {}".format(e))
        else:
            raise error.RequestError("Invalid request method {}".format(method))

    @staticmethod
    def interpret_response(response):
        """
        处理响应信息
        :param response: 响应
        :return: 返回响应结果
        """
        r_code = response.status_code
        if r_code == 502 and gcpayz.bad_gateway_match:
            return None
        elif r_code == 200:
            try:
                r_result = response.json()
                if r_result["code"] == 0 and r_result["msg"] == "SUCCESS":
                    return r_result
                else:
                    raise error.APIError(
                        "Invalid response body from API:{} "
                        "(HTTP response code was {})".format(r_result["msg"], r_result["code"])
                    )
            except Exception as e:
                raise error.ResponseError(
                    "Invalid response body from API:{} ".format(e)
                )
        else:
            raise error.APIError(
                "HTTP response code was {}".format(r_code)
            )
