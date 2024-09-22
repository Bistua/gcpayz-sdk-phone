# -*- coding=utf-8 -*-

class ERROR(Exception):
    pass


class RequestError(ERROR):
    pass


class ResponseError(ERROR):
    pass


class APIError(ERROR):
    pass
