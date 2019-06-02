
# zafu_news

获取浙江农林大学新闻，并发送至邮箱

## 网站列表

可获取以下几个网站的最新新闻

- 浙江农林大学**官网**的通知公告  
  [http://www.zafu.edu.cn/tzgg.htm](http://www.zafu.edu.cn/tzgg.htm)
- 浙江农林大学**教务处**通知公告  
  [http://jwc.zafu.edu.cn/tzgg.htm](http://jwc.zafu.edu.cn/tzgg.htm)  
- 浙江农林大学**信息工程学院**通知公告  
  [http://ie.zafu.edu.cn/xwxx/tzgg.htm](http://ie.zafu.edu.cn/xwxx/tzgg.htm)
- 浙江农林大学**研究生部**培养工作和学位工作的最新消息  
  [http://yjsb.zafu.edu.cn/index.htm](http://yjsb.zafu.edu.cn/index.htm)  

## 使用方法

### 1. 修改 zafu_news.py 文件内接受邮件的邮箱  

```python
# 接受信息的邮箱
receiver = 'xixiangshu704@qq.com'
```

### 2. 修改 mail_utility.py 文件内发送邮件的邮箱及密码

若用qq邮箱作为发送邮箱，密码须填写授权码，可参考此[链接](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)

```python
#定义邮件地址、账号密码等变量
host = 'smtp.qq.com'
user = 'xixiangshu704@foxmail.com'
passwd = 'kkknehvraimhbfie'
```

### 3. 运行程序

```python
python zafu_news.py
```

若希望在后台运行可使用下面的命令  

```python
nohup python zafu_news.py &
```

## 备注

可以自定义扫描网站的时间，在 zafu_news.py 文件中修改  

```python
# 扫描网站的周期 单位 秒
scan_time = 5 * 60
```
