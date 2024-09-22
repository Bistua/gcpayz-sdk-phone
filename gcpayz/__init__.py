# -*- coding=utf-8 -*-
from gcpayz.api_resources import *

max_network_retries = 1  # 重试次数
bad_gateway_match = True  # 是否开启重试
network_retry_delay = 0.5  # 重试间隔
request_timeout = 10  # 请求超时时间,单位，秒
