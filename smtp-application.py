import smtplib
import auth
from email.mime.text import MIMEText
from tkinter import *

top = Tk()
tk_to = Label(top, text='To:')
tk_to.pack()
E1 = Entry(top, bd=5)
E1.pack()

tk_from = Label(top, text='From:')
tk_from.pack()
E2 = Entry(top, bd=5)
E2.pack()

tk_subject = Label(top, text='Subject:')
tk_subject.pack()
E3 = Entry(top, bd=5)
E3.pack()

tk_body = Label(top, text='Body:')
tk_body.pack()
E4 = Entry(top, bd=5)
E4.pack()

top.mainloop()

pw_window = Tk()
pw_label = Label(pw_window, text='Password:')
E5 = Entry(pw_window)

pw_window.mainloop()
'''
# initialize message info
from_email = 'cjbombino@gmail.com'
to_email = from_email
password = auth.app_password
subject = 'Test'
body = 'Hello World'

# xreate SMTP server and login
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(from_email, password)

# Create MIMEText messsage object
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

# Send mail and quit server
server.sendmail(from_email, to_email, msg.as_string())
server.quit()
'''