import smtplib
import auth
from email.mime.text import MIMEText

from_email = 'cjbombino@gmail.com'
to_email = from_email
password = auth.app_password
subject = 'Test'
body = 'Hello World'

server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login(from_email, password)



msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

server.sendmail(from_email, to_email, msg.as_string())
server.quit()