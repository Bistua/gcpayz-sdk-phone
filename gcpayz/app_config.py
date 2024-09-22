# -*- coding=utf-8 -*-

_values = {
    "api_base": "http://127.0.0.1:9216",
    "version": "1.0"
}


class AppConfig(object):

    @staticmethod
    def get_base():
        return _values.get("api_base")

    @staticmethod
    def set_mch_no(mch_no):
        _values["mch_no"] = mch_no

    @staticmethod
    def get_mch_no():
        return _values.get("mch_no")

    @staticmethod
    def set_app_id(app_id):
        _values["app_id"] = app_id

    @staticmethod
    def get_app_id():
        return _values.get("app_id")

    @staticmethod
    def set_api_key(api_key):
        _values["api_key"] = api_key

    @staticmethod
    def get_api_key():
        return _values.get("api_key")

    @staticmethod
    def set_version(version):
        _values["version"] = version

    @staticmethod
    def get_version():
        return _values.get("version")
