# -*- coding=utf-8 -*-
import time
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

print("退款")
try:
    refund = gcpayz.Pay.refund(
        payOrderId="P1747547821449433089",  # 支付订单号，与mchOrderNo二者传一即可
        # mchOrderNo="mho1705482842905",  # 商户订单号，与payOrderId二者传一即可
        mchRefundNo="mho{}".format(int(round(time.time() * 1000))),  # 商户退款单号
        refundAmount=1,  # 退款金额（单位：分）
        currency="cny",  # 币种（目前只支持cny）
        clientIp="192.168.1.132",  # 发起退款请求客户端的IP地址
        refundReason="测试退款",  # 退款原因
        notifyUrl="",  # 异步通知地址
        channelExtra="",  # 渠道扩展参数
        extraParam=""  # 商户扩展参数,回调时原样返回
    )
    print(refund)
except Exception as e:
    print(e)
