import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config.conf_mail

def send_Mail(file_new,result):
    f = open(file_new, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    try:
        smtp = smtplib.SMTP(config.conf_mail.Smtp_Server,25)
        sender = config.conf_mail.Smtp_Sender
        password = config.conf_mail.Smtp_Sender_Password
        receiver = config.conf_mail.Smtp_Receiver
        smtp.login(sender, password)
        msg = MIMEMultipart()
        # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
        # 发送正文
        text = MIMEText(mail_body, 'html', 'utf-8')
        # 定义邮件正文标题
        text['Subject'] = Header('自动化测试报告', 'utf-8')
        msg.attach(text)
        # 发送附件
        # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        msg['Subject'] = Header('[执行结果：' + result + ']'+ '自动化测试报告' + now, 'utf-8')
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_file)
        # 定义发件人，如果不写，发件人为空
        msg['From'] = sender
        # 定义收件人，如果不写，收件人为空
        msg['To'] = ",".join(receiver)
        tmp = smtp.sendmail(sender, receiver, msg.as_string())
        print (tmp)
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False

