# -*- coding=utf-8 -*-
import time
import hashlib
from gcpayz.app_config import AppConfig
from gcpayz import error


def analysis_params(params):
    """
    解析请求参数
    :param params: 请求参数
    :return: 返回解析后的参数
    """
    new_dict = {}
    sign_type = "MD5"
    time_stamp = int(round(time.time() * 1000))
    for key, value in params.items():
        if value or value == 0:
            new_dict[key] = value
    params["mchNo"] = new_dict["mchNo"] = AppConfig.get_mch_no()
    params["appId"] = new_dict["appId"] = AppConfig.get_app_id()
    params["reqTime"] = new_dict["reqTime"] = time_stamp
    params["version"] = new_dict["version"] = AppConfig.get_version()
    params["signType"] = new_dict["signType"] = sign_type
    params["sign"] = signature_rules(new_dict)
    return params


def signature_rules(dict_data):
    """
    签名规则
    :param dict_data: 签名的数据
    :return: 返回加密后的签名
    """
    try:
        temp_data = sorted(dict_data.items(), key=lambda x: x[0], reverse=False)
        text = ""
        for key, value in dict(temp_data).items():
            text += "{}={}&".format(key, value)
        text += "key={}".format(AppConfig.get_api_key())
        return md5_encrypt(text)
    except Exception as e:
        raise error.RequestError(e)


def md5_encrypt(text):
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest().upper()
