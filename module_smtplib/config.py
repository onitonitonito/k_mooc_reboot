"""
# IMPORT BEFORE SENDING EMAIL w/ smtplib
"""
# compare to ConfigParser() + *.ini
# module_smtplib\smtp_plain_text_email.py

print(__doc__)

email_sender = 'nitt0x0@gmail.com'
email_reciever = 'nitt0@hanmail.net'

dict_email = {
        'subject'   : "This Is a Test Email from CodeItBro!",
        'body'      : [
                    "Hi, hope you're going fine! ",
                    "Please, Stay home! Stay safe!",
                    "Next time, I'll drop by.",
                    "",
                    "When you are creating a plain text email from scratch,",
                    "then you need to add the subject as header and then ",
                    "have a couple of blank lines. After that, you can put",
                    "the body of the email.",
                    "",
                    "Sincerely, Kay."
            ],
        }

contents = "\n".join(dict_email['body'])
message = f"Subject: {dict_email['subject']}\n\n{contents}"






if __name__ == '__main__':
    print(message)
