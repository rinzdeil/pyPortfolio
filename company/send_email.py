import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

password = "akkq dmgl ljny gcjb"
email = "dalesumande@gmail.com"

receiver = "dalesumande@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi from replit!
This is a test email from python.
"""

with smtplib.SMTP_SSL(host, port, context = context) as server:
  server.login(email, password)
  server.sendmail(email, receiver, message)

