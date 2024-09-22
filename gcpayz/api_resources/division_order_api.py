# -*- coding=utf-8 -*-
from gcpayz.api_requestor import ApiRequestor
from gcpayz.app_config import AppConfig


class DivisionOrderApi(AppConfig, ApiRequestor):

    @classmethod
    def bind_share_user(cls, data):
        url = AppConfig.get_base() + "/api/division/receiver/bind"
        return cls._request_api(url, data)

    @classmethod
    def order_share(cls, data):
        url = AppConfig.get_base() + "/api/division/exec"
        return cls._request_api(url, data)

    @staticmethod
    def _request_api(url, data):
        return ApiRequestor.request("POST", url, data)
