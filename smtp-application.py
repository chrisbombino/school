import smtplib
import auth

from_email = 'cjbombino@gmail.com'
to_email = from_email
password = auth.app_password

server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login(from_email, password)

subject = 'Test'
message = 'Hi Mom'

msg = '\r\n'.join([
    'Subject: Test',
    '',
    message
])
print(msg)
server.sendmail(from_email, to_email, message)
server.quit()