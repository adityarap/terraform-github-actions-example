# import boto3
# from botocore.exceptions import ClientError

# SENDER = "testfor276@gmail.com" # must be verified in AWS SES Email
# RECIPIENT = "testfor276@gmail.com" # must be verified in AWS SES Email

# # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
# AWS_REGION = "us-east-1"

# # The subject line for the email.
# SUBJECT = "This is test email for testing purpose..!!"

# # The email body for recipients with non-HTML email clients.
# BODY_TEXT = ("Hey Hi...\r\n"
#              "This email was sent with Amazon SES using the "
#              "AWS SDK for Python (Boto)."
#             )
            
# # The HTML body of the email.
# BODY_HTML = """<html>
# <head></head>
# <body>
#   <h1>Hey Hi...</h1>
#   <p>This email was sent with
#     <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
#     <a href='https://aws.amazon.com/sdk-for-python/'>
#       AWS SDK for Python (Boto)</a>.</p>
# </body>
# </html>
#             """            

# # The character encoding for the email.
# CHARSET = "UTF-8"

# # Create a new SES resource and specify a region.
# client = boto3.client('ses',region_name=AWS_REGION)

# # Try to send the email.
# try:
#     #Provide the contents of the email.
#     response = client.send_email(
#         Destination={
#             'ToAddresses': [
#                 RECIPIENT,
#             ],
#         },
#         Message={
#             'Body': {
#                 'Html': {
    
#                     'Data': BODY_HTML
#                 },
#                 'Text': {
    
#                     'Data': BODY_TEXT
#                 },
#             },
#             'Subject': {

#                 'Data': SUBJECT
#             },
#         },
#         Source=SENDER
#     )
# # Display an error if something goes wrong.	
# except ClientError as e:
#     print(e.response['Error']['Message'])
# else:
#     print("Email sent! Message ID:"),
#     print(response['MessageId'])

            
# import smtplib, ssl
# import os


# port = 465
# smtp_server = "smtp.gmail.com"
# USERNAME = os.environ.get('USER_EMAIL')
# PASSWORD = os.environ.get('USER_PASSWORD')
# # connection_url: ${{secrets.MAIL_CONNECTION}}

# message = """\
# Subject: ${{ github.job }} job of ${{ github.repository }} has ${{ job.status }}
# to: aditya.raparthi13@gmail.com

# This is your daily email report.
# """

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(USERNAME,PASSWORD)
#     server.sendmail(USERNAME,USERNAME,message)


import smtplib, ssl
import os

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.environ['USERNAME'] #"prudhvinaagch@gmail.com"  # Enter your address
receiver_email = "adityaraparthi1305@gmail.com"  # Enter receiver address
password = os.environ['PASSWORD'] #"odptefjhmqeziubd"
message = """\
Subject: ${{ github.job }} job of ${{ github.repository }} has ${{ job.status }}

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
