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

print("支付")
try:
    create = gcpayz.Pay.create(
        mchOrderNo="mho{}".format(int(time.time() * 1000)),  # 商户订单号
        wayCode="INDIA_PAY_IN",  # 支付方式
        amount=50000000,  # 支付金额（单位分）
        currency="INR",  # 币种（目前只支持cny）
        clientIp="192.168.1.132",  # 发起支付请求客户端的IP地址
        subject="游戏攻略",  # 商品标题
        body="未知特殊的充值记录",  # 商品描述
        notifyUrl="",  # 异步通知地址
        returnUrl="",  # 前端跳转地址
        channelExtra="{\"name\":\"tom\",\"email\":\"tom@gmail.com\",\"phone\":\"9001941197\"}",  # 渠道扩展参数
        extParam=""  # 商户扩展参数,回调时原样返回
    )
    print(create)
except Exception as e:
    print(e)
