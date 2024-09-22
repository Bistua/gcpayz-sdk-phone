# -*- coding=utf-8 -*-
import time
import gcpayz
from gcpayz.app_config import AppConfig
from example.notice.notice_service_start import NoticeServiceStart


class CreatePayNotice(NoticeServiceStart):

    def __init__(self):
        self.service = NoticeServiceStart
        # 配置信息
        api_key = "YLfBTJQB1rXVNgGk9VuGTwinpYnQWPoAK4EvgUd1DBcMKzzQ3UxpD6tcND7qlUVBjmwJ933U12u0bhPgr3QSxfK4U6zX9RomJlhT9kDooNDaW6hc2jpDnPWTZJGYCyHb"
        AppConfig.set_mch_no("M1679219294")
        AppConfig.set_app_id("6416da5ee4b00bed884be286")
        AppConfig.set_api_key(api_key)
        self.service.start_service()

    def pay_send_notice(self):
        try:
            charge = gcpayz.Pay.create(
                mchOrderNo="mho{}".format(int(round(time.time() * 1000))),  # 商户订单号
                wayCode="ALI_BAR",  # 支付方式
                amount=1,  # 支付金额（单位分）
                currency="cny",  # 币种（目前只支持cny）
                clientIp="192.168.1.132",  # 发起支付请求客户端的IP地址
                subject="商品标题",  # 商品标题
                body="商品描述",  # 商品描述
                notifyUrl="http://fg4x6u.natappfree.cc/notice/content",  # 异步通知地址
                returnUrl="",  # 前端跳转地址
                channelExtra="{\"authCode\":\"286922355302598616\"}",  # 渠道扩展参数
                extParam=""  # 商户扩展参数,回调时原样返回
            )
            print(charge)
        except Exception as error:
            print(error)
        time.sleep(5)
        self.service.stop_service()


if __name__ == '__main__':
    C = CreatePayNotice()
    C.pay_send_notice()
