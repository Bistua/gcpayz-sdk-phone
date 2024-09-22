# -*- coding=utf-8 -*-
import gcpayz
from gcpayz.app_config import AppConfig
# 配置信息
api_key = "hKqPeLLWL2Y2PmpJvnY51u2SK8pDZAHboc3aICDZyeMScGMNBVbvJFCrRcsMhMIwoO4iQ2kzf8LYfjoTnyrff0f677zR26czH3PlNlB1FR48O2KQMNKFzBua3LMYDzcc"
AppConfig.set_mch_no("M1726854270")
AppConfig.set_app_id("66edb483212c0083a0ee25b3")
AppConfig.set_api_key(api_key)


"""
支付 API 文档：https://www.showdoc.com.cn/2581465630175070?page_id=11478149393875123
"""

print("发起订单分账")
try:
    exec = gcpayz.Division.exec(
        payOrderId="P1721732006052859906",  # 支付订单号，与mchOrderNo二者传一即可
        # mchOrderNo="",  # 商户订单号，与payOrderId二者传一即可
        useSysAutoDivisionReceivers=1  # 是否使用系统配置的自动分账组，0-否 1-是
    )
    print(exec)
except Exception as e:
    print(e)
