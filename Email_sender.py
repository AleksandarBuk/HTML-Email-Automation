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

# uses SMTP server to log into gmail client and send the email

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('INPUT_RECEIVERS_E-MAIL', 'INPUT_YOUR_GOOGLE_SECURITY_PASSWORD') # use google's Securrity app password to allow the app to send the e-mail message
    smtp.send_message(email)
    print('Successfully sent')
