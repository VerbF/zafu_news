# coding=utf-8

#导入需要使用的模块
import smtplib
from email.header import Header
from email.mime.text import MIMEText

#定义发送邮件的函数，传入title,article,receiver参数
def send_mail(title,article,receiver):
    #定义邮件地址、账号密码等变量
    host = 'smtp.qq.com'
    user = 'xixiangshu704@foxmail.com'
    passwd = 'your_password' 
    sender = user
    coding = 'utf8'
    #定义message变量，写邮件内容、邮件头
    message = MIMEText (article,'plain',coding)
    message ['From'] = Header(sender,coding)
    message ['To'] = Header(receiver,coding)
    message ['subject'] = Header(title,coding)
    
    #错误处理
    try:
        #定义mail_client变量，开启SSL邮件，传入邮件服务器地址和端口
        mail_client = smtplib.SMTP_SSL(host,465)
        #连接smtp服务器
        mail_client.connect(host)
        #登录smtp服务器
        mail_client.login(user,passwd)
        #发送邮件
        mail_client.sendmail(sender,receiver,message.as_string())
        #发送完成关闭连接
        mail_client.close()
        print('邮件已成功发送给:'+receiver)
    except:
        #如果过程中抛出异常则提示用户
        print('发送失败!')