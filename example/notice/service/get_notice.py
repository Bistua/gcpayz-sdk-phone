# -*- coding=utf-8 -*-
from flask import request, Blueprint
from gcpayz.util import signature_rules

notice = Blueprint("notice", __name__)


@notice.route("/content", methods=["POST"])
def notice_content():
    return verify_signature()


def verify_signature():
    try:
        get_params, get_sign = analysis_get_params()
    except TypeError:
        return "fail"
    else:
        signature = signature_rules(get_params)
        if signature == get_sign:
            print(
                "验签成功\n"
                "获取sign-{}\n"
                "生成sign-{}".format(get_sign, signature)
            )
            return "success"
        else:
            print(
                "验签失败\n"
                "获取sign-{}\n"
                "生成sign-{}".format(get_sign, signature)
            )
            return "fail"


def analysis_get_params():
    new_params = {}
    get_params = request.form.to_dict()
    print("通知接收到的参数-{}".format(get_params))
    if get_params:
        get_sign = get_params["sign"]
        for key, value in get_params.items():
            if key != "sign" and value or value == 0:
                new_params[key] = value
        return new_params, get_sign
    else:
        return None
