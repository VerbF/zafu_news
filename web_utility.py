# coding=utf-8

import urllib
import codecs
import os
import file_utility
from bs4 import BeautifulSoup

# 获取网页内容
def get_web_content(url):
    #定义发送的请求
    req=urllib.request.Request(url)
    #将服务器返回的页面放入rsp变量
    rsp=urllib.request.urlopen(req)
    #读取这个页面，并解码成utf-8格式，忽略错误,放入变量html中
    html=rsp.read().decode('utf-8','ignore')
    #使用BeautifulSoup模块解析变量中的web内容
    html=BeautifulSoup(html,'html.parser')
    return html

# 获取新旧信息的不同
def get_different(record_list,old_record_list):
    result = []
    for record in record_list:
        # 获取历史记录中最新的一条数据，需要去掉末尾的换行符
        old_first_record = old_record_list[0][0:len(old_record_list[0])-1]
        if record != old_first_record:
            result.append(record)
        else:
            break
    return result

# 获得 zafu 官网通知公告的更新
def get_update_zafu_tzgg():
    
    url='http://www.zafu.edu.cn/tzgg.htm'
    history_file_path = 'history/zafu_tzgg.txt'

    html = get_web_content(url)
    result = []
    #循环找出所有的a标签，并赋值给变量 link
    for div in html.find_all('div'):    
        div_class = div.get('class')
        if not div_class is None:
            div_class = div_class[0]
        # 通知公告
        if div_class == 'rigthConBox-con':
            record_list = []
            for a in div.find_all('a',limit=10):
                info_link=url[0:23] + a.get('href')
                #把a标签中的文字赋值给info_text,并去除空格
                info_text=a.get_text(strip=True)

                record = info_text  + ' ' + info_link
                record_list.append(record)
            
            # 若是初次运行次程序，将数据写入历史文件中          
            if file_utility.is_empty(history_file_path):
                file_utility.write_history_file(history_file_path,record_list)
                return None
            # 若不是初次运行，与历史文件比较，判断是否有新的新闻
            else:
                old_record_list = file_utility.read_history_file(history_file_path)
                result = get_different(record_list,old_record_list)
                # 将最新的新闻写入历史文件中
                file_utility.write_history_file(history_file_path,record_list)
    return result


# 获得 zafu jwc 通知公告的更新
def get_update_zafu_jwc_tzgg():
    
    url='http://jwc.zafu.edu.cn/tzgg.htm'
    history_file_path = 'history/zafu_jwc_tzgg.txt'

    html = get_web_content(url)
    result = []
    #循环找出所有的a标签，并赋值给变量 link
    for div in html.find_all('div'):    
        div_class = div.get('class')
        if (not div_class is None) and len(div_class) == 1:
            div_class = div_class[0]
        # 通知公告
        if div_class == 'ny_news_lb':
            record_list = []
            for a in div.find_all('a',limit=10):
                info_link=url[0:23] + a.get('href')
                #把a标签中的文字赋值给info_text,并去除空格
                info_text=a.get_text(strip=True)

                record = info_text  + ' ' + info_link
                record_list.append(record)
            
            # 若是初次运行次程序，将数据写入历史文件中          
            if file_utility.is_empty(history_file_path):
                file_utility.write_history_file(history_file_path,record_list)
                return None
            # 若不是初次运行，与历史文件比较，判断是否有新的新闻
            else:
                old_record_list = file_utility.read_history_file(history_file_path)
                result = get_different(record_list,old_record_list)
                # 将最新的新闻写入历史文件中
                file_utility.write_history_file(history_file_path,record_list)
    return result

# 获得 zafu ie 通知公告的更新
def get_update_zafu_ie_tzgg():
    
    url='http://ie.zafu.edu.cn/xwxx/tzgg.htm'
    history_file_path = 'history/zafu_ie_tzgg.txt'

    html = get_web_content(url)
    result = []
    #循环找出所有的a标签，并赋值给变量 link
    for div in html.find_all('div'):    
        div_id = div.get('id')
        if (not div_id is None) and len(div_id) == 1:
            div_id = div_id[0]
        # 通知公告
        if div_id == 'LB-nodate':
            record_list = []
            for a in div.find_all('a',limit=10):

                temp_link = a.get('href')
                temp_link = temp_link[3:len(temp_link)]
                info_link=url[0:22] + temp_link

                #把a标签中的文字赋值给info_text,并去除空格
                info_text=a.get_text(strip=True)

                record = info_text  + ' ' + info_link
                record_list.append(record)
            
            # 若是初次运行次程序，将数据写入历史文件中          
            if file_utility.is_empty(history_file_path):
                file_utility.write_history_file(history_file_path,record_list)
                return None
            # 若不是初次运行，与历史文件比较，判断是否有新的新闻
            else:
                old_record_list = file_utility.read_history_file(history_file_path)
                result = get_different(record_list,old_record_list)
                # 将最新的新闻写入历史文件中
                file_utility.write_history_file(history_file_path,record_list)
    return result

# 获得 zafu yjsb 最新信息的更新
def get_update_zafu_yjsb_zxxx():
    
    url='http://yjsb.zafu.edu.cn/index.htm'
    history_dictory_path = 'history/zafu_yjsb/'
    history_file_path = ''

    html = get_web_content(url)
    test_file = open('test.txt','w', encoding='utf8')
    test_file.write(str(html))
    result = []
    #循环找出所有的a标签，并赋值给变量 link
    for div in html.find_all('div'):    
        div_class = div.get('class')
        if (not div_class is None) and len(div_class) == 1:
            div_class = div_class[0]
        # 通知公告
        if div_class == 'itemBox':
            record_list = []
            news_type = ''
            # 获取新闻的类型
            for span in div.find_all('span'):
                span_class = span.get('class')
                if (not span_class is None) and len(span_class) == 1:
                     span_class = span_class[0]
                if span_class == 'pointer':
                    span_text = span.get_text()
                    news_type = span_text
            # 目前只监控这两个类型的新闻
            if news_type == '培养工作':
                history_file_path = history_dictory_path + 'pygz.txt'
            elif news_type == '学位工作':
                history_file_path = history_dictory_path + 'xwgz.txt'
            else:
                continue

            for a in div.find_all('a',limit=7,recursive=True):

                temp_link = a.get('href')
                # temp_link = temp_link[3:len(temp_link)]
                info_link=url[0:24] + temp_link
                #把a标签中的文字赋值给info_text,并去除空格
                info_text=a.get_text(strip=True)
                record = info_text  + ' ' + info_link
                record_list.append(record)
            # 需要删除第一行
            record_list.pop(0)
            # 若是初次运行次程序，将数据写入历史文件中          
            if file_utility.is_empty(history_file_path):
                file_utility.write_history_file(history_file_path,record_list)
                return None
            # 若不是初次运行，与历史文件比较，判断是否有新的新闻
            else:
                old_record_list = file_utility.read_history_file(history_file_path)
                different_record_list = get_different(record_list,old_record_list)
                if len(different_record_list) != 0:
                    result = result + different_record_list
                # 将最新的新闻写入历史文件中
                file_utility.write_history_file(history_file_path,record_list)
    return result