# -*- coding=utf-8 -*-
from gcpayz.api_resources.pay_order_api import PayOrderApi
from gcpayz.api_resources.refund_order_api import RefundOrderApi
from gcpayz.util import analysis_params


class Pay(PayOrderApi, RefundOrderApi):

    @staticmethod
    def create(**params):
        data = analysis_params(params)
        return PayOrderApi.pay_order(data)

    @staticmethod
    def pay_query(**params):
        data = analysis_params(params)
        return PayOrderApi.query_order(data)

    @staticmethod
    def pay_close(**params):
        data = analysis_params(params)
        return PayOrderApi.close_order(data)

    @staticmethod
    def refund(**params):
        data = analysis_params(params)
        return RefundOrderApi.refund_order(data)

    @staticmethod
    def refund_query(**params):
        data = analysis_params(params)
        return RefundOrderApi.query_refund(data)

    @staticmethod
    def channel_user_jump(**params):
        data = analysis_params(params)
        return PayOrderApi.get_channel_user_id(data)
