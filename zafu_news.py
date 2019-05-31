# coding=utf-8
import time
from web_utility import get_update 
from mail_utility import send_mail 

# 接受信息的邮箱
receiver = 'xixiangshu704@qq.com'
# 扫描网站的周期 单位 秒
scan_time = 10

while True:
    time.sleep(scan_time)
    result = get_update()
    title = result[0]
    article = result[1]
    print(title)
    print(article)
    print()
    # send_mail(title,article,receiver)
