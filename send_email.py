import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = 'dimasradityo.b@gmail.com'
password = "poywegrhrholgqzn"

context = ssl.create_default_context()

message = '''\
Subject: Hi!
How are you?
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, username, message)