#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
def gmailSmtp():
    #smtp邮箱服务器地址
    smtp_host = 'smtp.gmail.com'  
    #密码(部分邮箱为授权码) 
    mail_pass = 'secrtet' 

    sender = 'sendmail@gmail.com'
    receivers = ['receiver@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("Hello", 'utf-8')   # 发送者
    message['To'] =  Header("测试", 'utf-8')        # 接收者
 
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
 
 
    try:
        smtpObj = smtplib.SMTP(smtp_host, 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"
    except smtplib.SMTPException as e:
        print ("Error: 无法发送邮件", e)

if __name__ == "__main__":
    gmailSmtp()