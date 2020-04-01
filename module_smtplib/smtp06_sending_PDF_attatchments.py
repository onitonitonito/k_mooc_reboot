"""
# Sending PDFs As Email Attachments
#
# IF N.G - Login credentials not working with Gmail SMTP - Stack Overflow
# = https://bit.ly/2xHDpCW
"""
# In a nutshell, google is not allowing you to log in via smtplib because
# it has flagged this sort of login as "less secure", so what you have to do
# is go to this link while you're logged in to your google account,
# and allow the access: https://www.google.com/settings/security/lesssecureapps
# Once that is set (see my screenshot below), it should work.

print(__doc__)
import sys
import getpass

import smtplib
import imghdr
from email.message import EmailMessage

from _add_syspath_root import root
from config import (
                email_sender,
                email_reciever,
                dict_email,         # keys = ['subject', 'body(array)']
                contents,           # body(array) --> string w/ '\n'
                message,            # combined = subject + body
            )

dir_data = root + '_statics/data/'

# password = input('Enter your email account password: ')
password = getpass.getpass(
                    prompt='Enter your email account password:',
                    stream=sys.stderr,
                )

newMessage = EmailMessage()
newMessage['Subject'] = "Check out the new program PDF"
newMessage['From'] = email_sender
newMessage['To'] = email_reciever
contents += 'Let me know what you think. PDF attached!'

newMessage.set_content(contents)

files = ['sample.pdf']

for file in files:
    with open(dir_data + file, 'rb') as f:
        file_data = f.read()
        file_name = file
        # file_name = f.name   # [WARN] : contains full path of project!
        print(file_name)       # FOR TEST!
    newMessage.add_attachment(
                        file_data,
                        maintype='application',
                        subtype='octet-stream',
                        filename=file_name
                    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_sender, password)
    smtp.send_message(newMessage)
