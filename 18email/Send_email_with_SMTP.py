#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
""")


from email.mime.text import MIMEText
import smtplib


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = 'zb-zhoufengen@kingmed.com.cn'
password = 'xxxxx'
# 输入收件人地址:
to_addr = 'phean@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.exmail.qq.com'

#server = smtplib.SMTP(smtp_server, 465) # SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()