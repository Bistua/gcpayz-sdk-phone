# -*- coding=utf-8 -*-
import os
import re
import sys
import time
from flask import Flask
from threading import Thread
from example.notice.service.get_notice import notice


class NoticeServiceStart(object):

    @staticmethod
    def start_service():
        print("启动服务")
        app = Flask(__name__)
        app.register_blueprint(notice, url_prefix='/notice')
        Thread(target=app.run, args=("localhost", 5001,)).start()
        time.sleep(1)

    @staticmethod
    def stop_service():
        print("关闭服务")
        if sys.platform.startswith("win"):
            pid_cmd = 'netstat -ano | findstr "5001"'
            cmd_data = os.popen(pid_cmd).read()
            pid = re.findall("LISTENING(.*)\n", cmd_data)[0].strip()
            kill_service = 'taskkill /F /PID "{}"'.format(pid)
        else:
            pid_cmd = 'netstat -tlnp | grep 5001'
            cmd_data = os.popen(pid_cmd).read()
            pid = re.findall("LISTEN(.*)/", cmd_data)[0].strip()
            kill_service = 'kill -9 {}'.format(pid)
        os.system(kill_service)

if __name__ == '__main__':
    N = NoticeServiceStart()
    N.start_service()
