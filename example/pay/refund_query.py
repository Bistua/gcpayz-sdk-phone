# -*- coding=utf-8 -*-
import gcpayz
from gcpayz.app_config import AppConfig

# 配置信息
# 配置信息
api_key = "hKqPeLLWL2Y2PmpJvnY51u2SK8pDZAHboc3aICDZyeMScGMNBVbvJFCrRcsMhMIwoO4iQ2kzf8LYfjoTnyrff0f677zR26czH3PlNlB1FR48O2KQMNKFzBua3LMYDzcc"
AppConfig.set_mch_no("M1726854270")
AppConfig.set_app_id("66edb483212c0083a0ee25b3")
AppConfig.set_api_key(api_key)

"""
支付 API 文档：https://www.showdoc.com.cn/2581465630175070?page_id=11478149393875123
"""

print("退款查询")
try:
    refund_query = gcpayz.Pay.refund_query(
        refundOrderId="R1747547915020161025",  # 退款订单号，与mchRefundNo二者传一即可
        # mchRefundNo="mho1705482865233"  # 商户退款单号，与refundOrderId二者传一即可
    )
    print(refund_query)
except Exception as e:
    print(e)
