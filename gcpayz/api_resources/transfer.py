# -*- coding=utf-8 -*-
from gcpayz.api_resources.transfer_order_api import TransferOrderApi
from gcpayz.util import analysis_params


class Transfer(TransferOrderApi):

    @staticmethod
    def create(**params):
        data = analysis_params(params)
        return TransferOrderApi.transfer_order(data)

    @staticmethod
    def transfer_query(**params):
        data = analysis_params(params)
        return TransferOrderApi.query_transfer(data)
