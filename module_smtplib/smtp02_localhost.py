""" N.G
# How To Send Emails Using Python With File Attachments [Scripts]
# https://www.codeitbro.com/send-emails-using-python/
#  - https://bit.ly/2xLw59c
#  - Himanshu Tyagi April 2, 2020

# README : start server First!
python -m smtpd -c DebuggingServer -n localhost:1025
"""

# Sender_Email = "emailpythontest12345@gmail.com"
# Subject = "Test Email from CodeItBro"
# Body = "Hi, hope you are doing fine! Stay Home! Stay Safe!"
# Message = f'Subject: {Subject}\n\n{Body}'

print(__doc__)

import smtplib
from config import (
                email_sender,
                email_reciever,
                message,
            )

server='localhost'
port = 1025

with smtplib.SMTP(server, port) as smtp:
    smtp.sendmail(email_sender, email_reciever, message)
