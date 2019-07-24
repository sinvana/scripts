import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host = "smtp.qq.com"
mail_user = "demo"
mail_pass = "demo"
#msjhwsozljwtfj

sender = "demo@qq.com"
#########################################################
r = ["demo@163.com","demo2@qq.com","demo3@qq.com","demo4@qq.com"]
c = ["1","你是我的眼","年少有为",""]
#########################################################
title = "模拟批量发送"

def sendEmail(receiver,content):
    message = MIMEText(content,"plain","utf-8")
    message['From'] = "{}".format(sender)
    message['To'] = receiver
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender,receiver,message.as_string())
        print("successful!")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == "__main__":
    for i in range(3):
        sendEmail(r[i],c[i])
