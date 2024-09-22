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

try:
    pay_query = gcpayz.Pay.pay_query(
        payOrderId="P1747545303520661506",  # 支付订单号，与mchOrderNo二者传一即可
        # mchOrderNo="mho1705482242572"  # 商户订单号，与payOrderId二者传一即可
    )
    print(pay_query)
except Exception as e:
    print(e)
