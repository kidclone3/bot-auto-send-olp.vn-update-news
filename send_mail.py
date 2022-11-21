import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
gmail_user = os.getenv('GMAIL_USER')
gmail_app_password = os.getenv('GMAIL_APP_PASSWORD')
sent_from = gmail_user
# sent_to = ['buikhanhduy_t65@hus.edu.vn', 'sao2162002gmail.com']
# print(sent_to)
def send_mail():
    with open('mail_list.txt', 'r') as f:
        sent_to = [line.strip() for line in f.readlines()]
    sent_subject = "[UPDATE] OLP.VN vừa có tin tức mới"
    # with codecs.open('template.html', 'r', encoding='utf-8', errors='ignore') as f:
    sent_body = """\
    OLP.vn vừa cập nhật tin tức mới.
    https://www.olp.vn/tin-tức/olympic-icpc/thông-báo

    From small bot with luv! \u2764\ufe0f
    """

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
    print(sent_to)
    msg = MIMEMultipart()
    msg_text = MIMEText(sent_body)
    msg['Subject'] = sent_subject
    msg['From'] = sent_from
    msg['To'] = ", ".join(sent_to)
    msg.attach(msg_text)
    msg.preamble = sent_body
    # email_text = """\
    # From: %s
    # Subject: %s
    # %s
    # """ % (sent_from, sent_subject, sent_body)

    print(email_text)
    # print(msg.as_string())
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, msg.as_string().encode('utf8'))
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
    
if __name__ == '__main__':
    send_mail()