# coding=utf-8
import time
import config as cfg
import web_utility
from mail_utility import send_mail 

# 接受信息的邮箱
receiver = cfg.receiver
# 扫描网站的周期 单位 秒
scan_time = cfg.scan_time

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

def zafu_yjsb_zxxx():
    result = web_utility.get_update_zafu_yjsb_zxxx()
    for record in result:
        send_mail(zafu_yjsb_zxxx_title,record,receiver)

while True:
    
    zafu_tzgg() # zafu 官网通知公告
    
    zafu_jwc_tzgg() # zafu jwc 通知公告
    
    zafu_ie_tzgg() # zafu ie 通知公告
    
    zafu_yjsb_zxxx() # zafu yjsb 最新消息

    # 扫描间隔时间
    time.sleep(scan_time )
 
