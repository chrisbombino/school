import smtplib
import auth
from email.mime.text import MIMEText
import tkinter

top = tkinter.Tk()
tk_user = Label(top, text='To Email')
tk_user.pack(side = LEFT)
E1 = Entry(top, bd=5)
E1.pack(side-RIGHT)

top.mainloop()

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