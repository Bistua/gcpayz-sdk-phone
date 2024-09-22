# -*- coding=utf-8 -*-
import time
import gcpayz
from gcpayz.app_config import AppConfig
from example.notice.notice_service_start import NoticeServiceStart


class CreateRefundPayNotice(NoticeServiceStart):

    def __init__(self):
        self.service = NoticeServiceStart
        # 配置信息
        api_key = "YLfBTJQB1rXVNgGk9VuGTwinpYnQWPoAK4EvgUd1DBcMKzzQ3UxpD6tcND7qlUVBjmwJ933U12u0bhPgr3QSxfK4U6zX9RomJlhT9kDooNDaW6hc2jpDnPWTZJGYCyHb"
        AppConfig.set_mch_no("M1679219294")
        AppConfig.set_app_id("6416da5ee4b00bed884be286")
        AppConfig.set_api_key(api_key)
        self.service.start_service()

    def refund_send_notice(self):
        try:
            refund = gcpayz.Pay.refund(
                payOrderId="P1744272867860877313",  # 支付订单号，与mchOrderNo二者传一即可
                # mchOrderNo="",  # 商户订单号，与payOrderId二者传一即可
                mchRefundNo="mho{}".format(int(round(time.time() * 1000))),  # 商户退款单号
                refundAmount=1,  # 退款金额（单位：分）
                currency="cny",  # 币种（目前只支持cny）
                clientIp="192.168.1.132",  # 发起退款请求客户端的IP地址
                refundReason="测试退款",  # 退款原因
                notifyUrl="http://fg4x6u.natappfree.cc/notice/content",  # 异步通知地址
                channelExtra="",  # 渠道扩展参数
                extraParam=""  # 商户扩展参数,回调时原样返回
            )
            print(refund)
        except Exception as error:
            print(error)
        time.sleep(5)
        self.service.stop_service()


if __name__ == '__main__':
    C = CreateRefundPayNotice()
    C.refund_send_notice()
