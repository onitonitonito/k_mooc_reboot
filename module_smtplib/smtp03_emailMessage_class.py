"""
# How To Send Emails Using Python With File Attachments [Scripts]
# https://www.codeitbro.com/send-emails-using-python/
#  - https://bit.ly/2xLw59c
#  - Himanshu Tyagi April 2, 2020
"""
import smtplib
from email.message import EmailMessage
from config import (
                email_sender,
                email_reciever,
                dict_email,     # keys = ['subject', 'body(array)']
                contents,       # body(array) --> string w/ '\n'
                message,        # combined = subject + body
            )

Password = input('Enter your email account password: ')

#creating an object of EmailMessage class
newMessage = EmailMessage()

#Defining email subject
newMessage['Subject'] = dict_email['subject']

#Defining sender email
newMessage['From'] = email_sender

#Defining reciever email
newMessage['To'] = email_reciever

#Defining email body
newMessage.set_content(contents)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    #Login to SMTP server
    smtp.login(email_sender, Password)

    #Sending email using send_message method by passing EmailMessage object
    smtp.send_message(newMessage)
