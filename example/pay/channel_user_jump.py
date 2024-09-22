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

print("获取用户渠道id")
try:
    channel_user_jump = gcpayz.Pay.channel_user_jump(
        ifCode="AUTO",  # 支付接口，目前只支持传 AUTO
        redirectUrl="https://www.gcpayz.com"   # 跳转地址
    )
    print(channel_user_jump)
except Exception as e:
    print(e)
