# -*- coding=utf-8 -*-
import gcpayz
from gcpayz.app_config import AppConfig

# 配置信息
api_key = "YLfBTJQB1rXVNgGk9VuGTwinpYnQWPoAK4EvgUd1DBcMKzzQ3UxpD6tcND7qlUVBjmwJ933U12u0bhPgr3QSxfK4U6zX9RomJlhT9kDooNDaW6hc2jpDnPWTZJGYCyHb"
AppConfig.set_mch_no("M1679219294")
AppConfig.set_app_id("6416da5ee4b00bed884be286")
AppConfig.set_api_key(api_key)


"""
支付 API 文档：https://www.showdoc.com.cn/2581465630175070?page_id=11478149393875123
"""

print("转账查询")
try:
    transfer_query = gcpayz.Transfer.transfer_query(
        transferId="T1743191690773204994",  # 转账订单号，与mchOrderNo二者传一即可
        # mchOrderNo="mho162913762435"  # 商户转账单号，与transferId二者传一即可
    )
    print(transfer_query)
except Exception as e:
    print(e)
