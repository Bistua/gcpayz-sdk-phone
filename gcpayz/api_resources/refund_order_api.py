# -*- coding=utf-8 -*-
from gcpayz.api_requestor import ApiRequestor
from gcpayz.app_config import AppConfig


class RefundOrderApi(AppConfig, ApiRequestor):

    @classmethod
    def refund_order(cls, data):
        url = AppConfig.get_base() + "/api/refund/refundOrder"
        return cls._request_api(url, data)

    @classmethod
    def query_refund(cls, data):
        url = AppConfig.get_base() + "/api/refund/query"
        return cls._request_api(url, data)

    @staticmethod
    def _request_api(url, data):
        return ApiRequestor.request("POST", url, data)
