# -*- coding=utf-8 -*-
import urllib3
import requests
import gcpayz
from urllib3.exceptions import InsecureRequestWarning
from gcpayz import error


class HttpClient(object):

    @staticmethod
    def request(method, url, params):
        try:
            urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.request(method=method, url=url, params=params, timeout=gcpayz.request_timeout)
            response.close()
            return response
        except Exception as e:
            raise error.APIError("Invalid API Request {}".format(e))
