"""
# Sending Multiple Images As Attachments
# https://www.codeitbro.com/send-emails-using-python/
# ?fbclid=IwAR3nNfw5L72cKt72ZZF8cyRZo8ckf36K6ComP5dOcv8hBfX-0_bM2EtgqKY
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
                dict_email,     # keys = ['subject', 'body(array)']
                contents,       # body(array) --> string w/ '\n'
                message,        # combined = subject + body
            )

dir_img = root + '_statics/data/'
file_one = 'Felix_munch.png'
file_two = 'Felix_dizzy.png'

# password = input('Enter your email account password: ')
password = getpass.getpass(
                    prompt='Enter your email account password:',
                    stream=sys.stderr,
                )

newMessage = EmailMessage()
newMessage['Subject'] = "Check out the new logo"
newMessage['From'] = email_sender
newMessage['To'] = email_reciever
contents += '\n\nLet me know what you think. Image attached!'

newMessage.set_content(contents)


for file in [file_one, file_two]:
    with open(dir_img + file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = file
        # image_name = f.name   # [WARN] : contains full path of project!
        print(image_name)       # FOR TEST!

    newMessage.add_attachment(
                        image_data,
                        maintype='image',
                        subtype=image_type,
                        filename=image_name
                    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_sender, password)
    smtp.send_message(newMessage)
