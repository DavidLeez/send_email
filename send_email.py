import smtplib
import ssl
import os

host = "smtp.gmail.com"
port = 465


def send_email(message):
    username = 'davidleez.vn@gmail.com'
    # password = os.getenv('PASSWORD')
    password = 'fkhqeovktkvhmzhc'

    receiver = 'dailv.cntt@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
