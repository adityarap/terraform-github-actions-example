import smtplib, ssl
import os


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
connection_url: ${{secrets.MAIL_CONNECTION}}
message = """\
Subject: ${{ github.job }} job of ${{ github.repository }} has ${{ job.status }}
to: aditya.raparthi13@gmail.com

This is your daily email report.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,USERNAME,message)
