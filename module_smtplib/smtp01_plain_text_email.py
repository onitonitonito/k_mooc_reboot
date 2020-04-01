"""
# How To Send Emails Using Python With File Attachments [Scripts]
# https://www.codeitbro.com/send-emails-using-python/
#  - https://bit.ly/2xLw59c
#  - Himanshu Tyagi April 2, 2020
#
# IF N.G - Login credentials not working with Gmail SMTP - Stack Overflow
# = https://bit.ly/2xHDpCW
"""
# In a nutshell, google is not allowing you to log in via smtplib because
# it has flagged this sort of login as "less secure", so what you have to do
# is go to this link while you're logged in to your google account,
# and allow the access: https://www.google.com/settings/security/lesssecureapps
# Once that is set (see my screenshot below), it should work.

# SMTP server address: smtp.gmail.com.
# Gmail SMTP port (TLS): 587.
# SMTP port (SSL): 465.
# SMTP TLS/SSL required: yes.

print(__doc__)

import smtplib
from config import (
                email_sender,
                email_reciever,
                message,
            )

# print(smtplib.SMTP.login.__doc__);quit()
password = input('Enter your email account password :')
server = 'smtp.gmail.com'
port = 587
print('\n')

print(message)

_answer = "\n\n...Is it OK with you? [Y:Enter]/No=1"
if input(_answer).startswith("1"): quit()
print('\n')


with smtplib.SMTP(server, port) as smtp:
    smtp.ehlo()     # Identify ourselves w/ the mail server we're using.
    smtp.starttls() # Encrypt our connection
    smtp.ehlo()     # Reidentify our connection as encrypted w/ mail server
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciever, message)
