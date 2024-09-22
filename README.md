# Gcpayz Python SDK
---

## 简介

gcpayz 文件夹下是 Python SDK 文件，  
example 文件夹里面是简单的接入示例，该示例仅供参考。

## 接入方法

[示例代码](example/)

### 初始化

设置请求超时时间，默认10秒

```python
gcpayz.request_timeout = 10
```

### 设置重试

设置重试次数，`0` 表示不重试，默认为 `1`。

```python
gcpayz.max_network_retries = 1
```

当服务端返回 `502` 时，是否根据返回内容来判断是否重试。`True` 表示只要是 `502`，全部重试。默认为 `True`。

```python
gcpayz.bad_gateway_match = True
```

设置重试延时时间，默认0.5秒

```python
gcpayz.network_retry_delay = 0.5
```

### 参数配置

配置信息可通过商户平台查看

```python
AppConfig.set_mch_no(mch_no)  # 配置商户号
AppConfig.set_app_id(app_id)  # 配置应用id
AppConfig.set_api_key(api_key)  # 配置api key
AppConfig.set_version(version)  # 配置api版本号，如果不配置，默认配置为1.0
```

## 支付

### 统一下单

```python
gcpayz.Pay.create(
    mchOrderNo="mho{}".format(int(time.time() * 1000)),  # 商户订单号
    wayCode="WX_BAR",  # 支付方式
    amount=1,  # 支付金额（单位分）
    currency="cny",  # 币种（目前只支持cny）
    clientIp="192.168.1.132",  # 发起支付请求客户端的IP地址
    subject="商品标题",  # 商品标题
    body="商品描述",  # 商品描述
    notifyUrl="",  # 异步通知地址
    returnUrl="",  # 前端跳转地址
    channelExtra="{\"auth_code\":\"133884556191863472\"}",  # 渠道扩展参数
    extParam=""  # 商户扩展参数,回调时原样返回
)
```

### 查询订单

```python
gcpayz.Pay.pay_query(
    payOrderId="P1747545303520661506",  # 支付订单号，与mchOrderNo二者传一即可
    # mchOrderNo="mho1705482242572"  # 商户订单号，与payOrderId二者传一即可
)
```

### 关单订单

```python
gcpayz.Pay.pay_close(
    payOrderId="P1747545303520661506",  # 支付订单号，与mchOrderNo二者传一即可
    # mchOrderNo="mho1705482242572"  # 商户订单号，与payOrderId二者传一即可
)
```

### 支付通知

当订单支付成功时，支付网关会向商户系统发起回调通知。如果商户系统没有正确返回，支付网关会延迟再次通知。

```python
"""
该链接是通过统一下单接口提交的参数notifyUrl设置，如果无法访问
链接，商户系统将无法接收到支付中心的通知。
"""
gcpayz.Pay.create(
    mchOrderNo="mho{}".format(int(time.time() * 1000)),  # 商户订单号
    wayCode="WX_BAR",  # 支付方式
    amount=1,  # 支付金额（单位分）
    currency="cny",  # 币种（目前只支持cny）
    clientIp="192.168.1.132",  # 发起支付请求客户端的IP地址
    subject="商品标题",  # 商品标题
    body="商品描述",  # 商品描述
    notifyUrl="https://www.baidu.com",  # 异步通知地址
    returnUrl="",  # 前端跳转地址
    channelExtra="{\"auth_code\":\"133884556191863472\"}",  # 渠道扩展参数
    extParam=""  # 商户扩展参数,回调时原样返回
)
```

### 获取用户渠道id

```python
gcpayz.Pay.channel_user_jump(
    ifCode="AUTO",  # 支付接口，目前只支持传 AUTO
    redirectUrl="https://www.jeequan.com"  # 跳转地址
)
```

### 发起退款

```python
gcpayz.Pay.refund(
    payOrderId="P1747545303520661506",  # 支付订单号，与mchOrderNo二者传一即可
    # mchOrderNo="mho1705482242572",  # 商户订单号，与payOrderId二者传一即可
    mchRefundNo="mho{}".format(int(round(time.time() * 1000))),  # 商户退款单号
    refundAmount=1,  # 退款金额（单位：分）
    currency="cny",  # 币种（目前只支持cny）
    clientIp="192.168.1.132",  # 发起退款请求客户端的IP地址
    refundReason="测试退款",  # 退款原因
    notifyUrl="",  # 异步通知地址
    channelExtra="",  # 渠道扩展参数
    extraParam=""  # 商户扩展参数,回调时原样返回
)
```

### 退款查询

```python
gcpayz.Pay.refund_query(
    refundOrderId="R1747547915020161025",  # 退款订单号，与mchRefundNo二者传一即可
    # mchRefundNo="mho1705482865233"  # 商户退款单号，与refundOrderId二者传一即可
)
```

### 退款通知

当退款完成时(成功或失败)，支付网关会向商户系统发起回调通知。如果商户系统没有正确返回，支付网关会延迟再次通知。

```python
"""
该链接是通过统一下单接口提交的参数notifyUrl设置，如果无法访问
链接，商户系统将无法接收到支付中心的通知。

"""
gcpayz.Pay.refund(
    payOrderId="P1747545303520661506",  # 支付订单号，与mchOrderNo二者传一即可
    # mchOrderNo="mho1705482242572",  # 商户订单号，与payOrderId二者传一即可
    mchRefundNo="mho{}".format(int(round(time.time() * 1000))),  # 商户退款单号
    refundAmount=1,  # 退款金额（单位：分）
    currency="cny",  # 币种（目前只支持cny）
    clientIp="192.168.1.132",  # 发起退款请求客户端的IP地址
    refundReason="测试退款",  # 退款原因
    notifyUrl="https://www.baidu.com",  # 异步通知地址
    channelExtra="",  # 渠道扩展参数
    extraParam=""  # 商户扩展参数,回调时原样返回
)
```

## 转账

### 发起转账

```python
gcpayz.Transfer.create(
    mchOrderNo="mho{}".format(int(round(time.time() * 1000))),  # 商户转账单号
    amount=1,  # 转账金额（单位分）
    currency="cny",  # 币种
    ifCode="aliaqfpay",  # 接口代码，wxpay-微信官方接口 ; alipay-支付宝官方接口; aliaqfpay-支付宝安全发接口
    entryType="ALIPAY_CASH",  # 入账方式，WX_CASH-微信零钱; ALIPAY_CASH-支付宝转账; BANK_CARD-银行卡
    accountNo="15521548748",  # 收款账号
    accountName="测试",  # 收款人姓名
    transferDesc="测试转账",  # 转账备注信息
    clientIp="192.168.1.132"  # 发起转账请求客户端的IP地址
)
```

### 转账查询

```python
gcpayz.Transfer.transfer_query(
    transferId="T1743191690773204994",  # 转账订单号，与mchOrderNo二者传一即可
    # mchOrderNo="mho162913762435"  # 商户转账单号，与transferId二者传一即可
)
```

### 转账通知

当转账完成时(成功或失败)，支付网关会向商户系统发起回调通知。如果商户系统没有正确返回，支付网关会延迟再次通知。

```python
"""
该链接是通过转账申请接口提交的参数notifyUrl设置，如果无法访问
链接，商户系统将无法接收到支付中心的通知。
"""
gcpayz.Transfer.create(
    mchOrderNo="mho{}".format(int(round(time.time() * 1000))),  # 商户转账单号
    amount=1,  # 转账金额（单位分）
    currency="cny",  # 币种
    ifCode="aliaqfpay",  # 接口代码，wxpay-微信官方接口 ; alipay-支付宝官方接口; aliaqfpay-支付宝安全发接口
    entryType="ALIPAY_CASH",  # 入账方式，WX_CASH-微信零钱; ALIPAY_CASH-支付宝转账; BANK_CARD-银行卡
    accountNo="15521548748",  # 收款账号
    accountName="测试",  # 收款人姓名
    transferDesc="测试转账",  # 转账备注信息
    clientIp="192.168.1.132",  # 发起转账请求客户端的IP地址
    notifyUrl="https://www.baidu.com"  # 异步通知地址
)
```

## 分账

### 绑定分账用户

```python
gcpayz.Division.bind_user(
    ifCode="zftpay",  # 接口代码
    receiverAlias="15521254124",  # 接收者账号别名
    receiverGroupId=100048,  # 组ID
    accType=0,  # 分账接收账号类型
    accNo="15521254124",  # 分账接收账号
    relationType="PARTNER",  # 分账关系类型
    divisionProfit=0.3  # 默认分账比例(若分账30% 则填入 0.3)
)
```

### 发起订单分账

```python
gcpayz.Division.exec(
    payOrderId="P1721732006052859906",  # 支付订单号，与mchOrderNo二者传一即可
    # mchOrderNo="",  # 商户订单号，与payOrderId二者传一即可
    useSysAutoDivisionReceivers=1  # 是否使用系统配置的自动分账组，0-否 1-是
)
```

