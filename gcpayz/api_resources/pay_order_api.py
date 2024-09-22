# -*- coding=utf-8 -*-
from gcpayz.api_requestor import ApiRequestor
from gcpayz.app_config import AppConfig


class PayOrderApi(AppConfig, ApiRequestor):

    @classmethod
    def pay_order(cls, data):
        url = AppConfig.get_base() + "/api/pay/unifiedOrder"
        return cls._request_api(url, data)

    @classmethod
    def query_order(cls, data):
        url = AppConfig.get_base() + "/api/pay/query"
        return cls._request_api(url, data)

    @classmethod
    def close_order(cls, data):
        url = AppConfig.get_base() + "/api/pay/close"
        return cls._request_api(url, data)

    @classmethod
    def get_channel_user_id(cls, data):
        url = AppConfig.get_base() + "/api/channelUserId/jump"
        return cls._request_api(url, data)

    @staticmethod
    def _request_api(url, data):
        return ApiRequestor.request("POST", url, data)
