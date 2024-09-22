# -*- coding=utf-8 -*-
import time
import gcpayz
from gcpayz.app_config import AppConfig
from example.notice.notice_service_start import NoticeServiceStart


class CreateTransferNotice(NoticeServiceStart):

    def __init__(self):
        self.service = NoticeServiceStart()
        # 配置信息
        api_key = "YLfBTJQB1rXVNgGk9VuGTwinpYnQWPoAK4EvgUd1DBcMKzzQ3UxpD6tcND7qlUVBjmwJ933U12u0bhPgr3QSxfK4U6zX9RomJlhT9kDooNDaW6hc2jpDnPWTZJGYCyHb"
        AppConfig.set_mch_no("M1679219294")
        AppConfig.set_app_id("6416da5ee4b00bed884be286")
        AppConfig.set_api_key(api_key)
        self.service.start_service()

    def transfer_send_notice(self):
        try:
            charge = gcpayz.Transfer.create(
                mchOrderNo="mho{}".format(int(round(time.time() + 1000))),  # 商户转账单号
                amount=1,  # 转账金额（单位分）
                currency="cny",  # 币种
                ifCode="aliaqfpay",  # 接口代码，wxpay-微信官方接口 ; alipay-支付宝官方接口; aliaqfpay-支付宝安全发接口
                entryType="ALIPAY_CASH",  # 入账方式，WX_CASH-微信零钱; ALIPAY_CASH-支付宝转账; BANK_CARD-银行卡
                accountNo="1552148758",  # 收款账号
                accountName="测试",  # 收款人姓名
                transferDesc="测试转账",  # 转账备注信息
                clientIp="192.168.1.132",  # 发起转账请求客户端的IP地址
                notifyUrl="http://fg4x6u.natappfree.cc/notice/content",  # 异步通知地址
            )
            print(charge)
        except Exception as error:
            print(error)
        time.sleep(5)
        self.service.stop_service()


if __name__ == '__main__':
    C = CreateTransferNotice()
    C.transfer_send_notice()
