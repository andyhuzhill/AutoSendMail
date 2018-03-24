#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-24 20:47:04
# @Author  : andyhuzhill (andyhuzhill@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

server_addr = "smtp.qq.com"

def send_mail(subject, server_addr, from_addr, passwd, to_addr, msg_text, file_list):
    msg = MIMEMultipart()

    msg["From"] = _format_addr(" <{0}>".format(from_addr))
    msg["To"] = _format_addr(",".join(to_addr))
    msg["Subject"] = Header(subject, 'utf-8').encode()

    msg.attach(MIMEText(msg_text, 'plain', 'utf-8'))

    for file_name in file_list:
        with open(file_name, 'rb') as f:
            mime = MIMEApplication(f.read())
            mime.add_header("Content-Disposition", "attachment", filename=file_name)
            msg.attach(mime)

    server = smtplib.SMTP(server_addr, 587)
    server.starttls()

    server.login(from_addr, passwd)

    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


if __name__ == "__main__":
    send_mail("Test", server_addr, from_addr, password, [], "Message Send By Python", [""])