#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
MUA:
在我们用Outlook或者Foxmail之类的软件写好邮件，填上对方的Email地址，点“发送”，电子邮件就发出去了。
这些电子邮件软件被称为MUA：Mail User Agent——邮件用户代理。

MTA:
Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等。

MDA:
新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理。

所以，一封电子邮件的旅程就是：
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：
1.编写MUA把邮件发到MTA；
2.编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。

收邮件时，MUA和MDA使用的协议有两种：
POP：Post Office Protocol，目前版本是3，俗称POP3；
IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

在使用Python收发邮件前，请先准备好至少两个电子邮箱，如xxx@163.com，xxx@qq.com等，注意两个邮箱不要用同一家邮件服务商。



""")