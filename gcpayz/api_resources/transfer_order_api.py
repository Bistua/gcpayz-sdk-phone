# -*- coding=utf-8 -*-
from gcpayz.api_requestor import ApiRequestor
from gcpayz.app_config import AppConfig


class TransferOrderApi(AppConfig, ApiRequestor):

    @classmethod
    def transfer_order(cls, data):
        url = AppConfig.get_base() + "/api/transferOrder"
        return cls._request_api(url, data)

    @classmethod
    def query_transfer(cls, data):
        url = AppConfig.get_base() + "/api/transfer/query"
        return cls._request_api(url, data)

    @staticmethod
    def _request_api(url, data):
        return ApiRequestor.request("POST", url, data)
