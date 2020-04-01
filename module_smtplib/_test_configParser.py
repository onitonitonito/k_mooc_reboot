import configparser
from _add_syspath_root import root

dir_home = root + 'module_smtplib/'

# to load the information from config_invisible.ini(*hidden)
config = configparser.ConfigParser()
config.read(dir_home + 'config.ini')


email_parse = lambda item : config.get('email', item )
subject = email_parse('subject')
body = email_parse('body')
sign = email_parse('sign')

user_parse = lambda item : config.get('user', item )
username = user_parse('name')
userpass = user_parse('pass')


print(f"{subject}\n\n{body}\n\n{sign}")
print(f"\n\nNAME: {username}\nPASS: {userpass}")
