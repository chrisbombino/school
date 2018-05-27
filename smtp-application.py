import smtplib
from . import auth

from_email = 'cjbombino@gmail.com'
to_email = from_email
password = auth.password

server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login(from_email, password)