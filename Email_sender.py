import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'INPUT_SENDERS_NAME'
email['to'] = 'INPUT_RECEIVERS_E-MAIL'
email['subject'] = 'Summer is here!'

email.set_content(html.substitute('Crash news'), 'html')

#Define class user for registration
class User:

    def __init__(self, name, signature):
        self.name = name
        self.signature = signature

#basic function
    def Greeting(self):
        print(self.name)

    def Yell(self):
        print(f'{self.name} has logged in. {self.signature}')

# uses SMTP server to log into gmail client and send the email

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('INPUT_RECEIVERS_E-MAIL',
               'INPUT_YOUR_GOOGLE_SECURITY_PASSWORD')  # use google's Securrity app password to allow the app to send the e-mail message
    smtp.send_message(email)
    print('Successfully sent')

# sending to e-mail lists functionality
