# coding=utf-8

import urllib.request
import codecs
import os
from bs4 import BeautifulSoup

def get_update():
    #定义url地址
    url='http://www.zafu.edu.cn/tzgg.htm'
    #定义发送的请求
    req=urllib.request.Request(url)
    #将服务器返回的页面放入rsp变量
    rsp=urllib.request.urlopen(req)
    #读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html=rsp.read().decode('utf-8','ignore')
    #使用BeautifulSoup模块解析变量中的web内容
    html=BeautifulSoup(html,'html.parser')
    # 文件历史
    history = 'history/zafu_tzgg.txt'


    #循环找出所有的a标签，并赋值给变量 link
    for div in html.find_all('div'):    
        div_class = div.get('class')
        if not div_class is None:
            div_class = div_class[0]
        # 通知公告
        if div_class == 'rigthConBox-con':
            record_list = []
            for a in div.find_all('a',limit=10):
                # 把href中的内容赋值给info_link
                info_link=url[0:23] + a.get('href')
                #把a标签中的文字赋值给info_text,并去除空格
                info_text=a.get_text(strip=True)

                record = info_link + ' ' + info_text
                record_list.append(record)
            
            # 若是初次运行次程序，先写入数据
            history_len = len(open(history, encoding='utf8').read())            
            if history_len == 0 or history_len == 1 or history_len == 3:
                history_file = open(history,'w', encoding='utf8')
                for record in record_list:
                    history_file.write(record+'\n')
                history_file.close()
            else:
                history_file = open(history,'r',encoding='utf8')
                old_record_list = history_file.readlines()
                

                
get_update()