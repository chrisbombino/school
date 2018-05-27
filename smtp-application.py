import smtplib

from_email = 'cjbombino@gmail.com'
to_email = from_email

server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login(u, p)