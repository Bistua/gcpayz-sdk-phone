# -*- coding=utf-8 -*-
from gcpayz.api_resources.division_order_api import DivisionOrderApi
from gcpayz.util import analysis_params


class Division(DivisionOrderApi):

    @staticmethod
    def bind_user(**params):
        data = analysis_params(params)
        return DivisionOrderApi.bind_share_user(data)

    @staticmethod
    def exec(**params):
        data = analysis_params(params)
        return DivisionOrderApi.order_share(data)
