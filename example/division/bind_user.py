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

print("分账绑定用户")
try:
    bind_user = gcpayz.Division.bind_user(
        ifCode="zftpay",  # 接口代码
        receiverAlias="15521254124",  # 接收者账号别名
        receiverGroupId=100048,  # 组ID
        accType=0,  # 分账接收账号类型
        accNo="15521254124",  # 分账接收账号
        relationType="PARTNER",  # 分账关系类型
        divisionProfit=0.3  # 默认分账比例(若分账30% 则填入 0.3)
    )
    print(bind_user)
except Exception as e:
    print(e)
