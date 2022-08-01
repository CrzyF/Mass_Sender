import os
import smtplib
import imghdr
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


contacts = ['']

msg = EmailMessage()
msg['Subject'] = ''
msg['From'] = ''
msg['To'] = contacts

# msg.set_content('This is a plain text email')

msg.add_alternative("""\

HTML_CODE_HERE

""", subtype='html')


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('email_here', 'app_password_here')
server.send_message(msg)
print('Messages Sent Successfully')
server.quit()
