import smtplib
import ssl

default_message = """\
Subject: Hi from pyPortfolio project!

This is a test email from python.
"""


def send_email(message):
  host = "smtp.gmail.com"
  port = 465
  context = ssl.create_default_context()

  password = "akkq dmgl ljny gcjb"
  email = "dalesumande@gmail.com"

  with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, email, message)


if __name__ == "__main__":
  send_email(default_message)
