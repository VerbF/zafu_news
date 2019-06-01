# coding=utf-8
import time
import web_utility
from mail_utility import send_mail 

# 接受信息的邮箱
receiver = 'xixiangshu704@qq.com'
# 扫描网站的周期 单位 分钟
scan_time = 5

zafu_tzgg_title = 'zafu_news-通知公告'
zafu_jwc_tzgg_title = 'zafu_news-教务处-通知公告'
zafu_yjsb_zxxx_title = 'zafu_news-研究生部-最新消息'
zafu_ie_tzgg_title = 'zafu_news-信工学院-通知公告'


def zafu_tzgg():
    result = web_utility.get_update_zafu_tzgg()
    for record in result:
        send_mail(zafu_tzgg_title,record,receiver)

def zafu_ie_tzgg():
    result = web_utility.get_update_zafu_ie_tzgg()
    for record in result:
        send_mail(zafu_ie_tzgg_title,record,receiver)

def zafu_jwc_tzgg():
    result = web_utility.get_update_zafu_jwc_tzgg()
    for record in result:
        send_mail(zafu_jwc_tzgg_title,record,receiver)


while True:
    time.sleep(scan_time * 60)
    # zafu 官网通知公告
    zafu_tzgg()
    # zafu jwc 通知公告
    zafu_jwc_tzgg()
    # zafu ie 通知公告
    zafu_ie_tzgg()
 
 
