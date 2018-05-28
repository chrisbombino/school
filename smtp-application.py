import smtplib
import auth
from email.mime.text import MIMEText
from tkinter import *
import re


class emailWindow:
    # initialize window with labels, text fields and buttons
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()

        self.tk_to = Label(frame, text='To:')
        self.tk_to.pack()
        self.E1 = Entry(frame, bd=5, width=40)
        self.E1.pack()

        self.tk_from = Label(frame, text='From:')
        self.tk_from.pack()
        self.E2 = Entry(frame, bd=5, width=40)
        self.E2.pack()

        self.tk_subject = Label(frame, text='Subject:')
        self.tk_subject.pack()
        self.E3 = Entry(frame, bd=5, width=60)
        self.E3.pack()

        self.tk_body = Label(frame, text='Body:')
        self.tk_body.pack()
        self.E4 = Text(frame, bd=5, height=10)
        self.E4.pack()

        self.send_button = Button(frame, text='Send', command=self.validate, height=2, padx=50)
        self.send_button.pack()

    # function for validating user input
    def validate(self):
        # regex to check email format,
        if re.match(r'\w+@\w+\.com', self.E1.get()) and re.match(r'\w+@gmail\.com', self.E2.get()) and re.match(r'\w+', self.E3.get()) and re.match(r'\w+', self.E4.get('1.0', END)):
            self.open_pw()
        else:
            fails = []
            if re.match(r'^\w+@\w+\.\w{1,4}$', self.E1.get()):
                pass
            else:
                fails.append('To Email')
            if re.match(r'^\w+@gmail\.com$', self.E2.get()):
                pass
            else:
                fails.append('From Email')
            if re.match(r'\w+', self.E3.get()):
                pass
            else:
                fails.append('Subject')
            if re.match(r'\w+', self.E4.get('1.0', END)):
                pass
            else:
                fails.append('Body')
            self.fail_window(fails)
    # if validation fails, this window opens
    def fail_window(self, fail_arr):
        window =Tk()
        print(fail_arr)
        str = ' ,'.join(fail_arr)
        label1 = Label(window, text='Please correct the following information: ' + str)
        label1.pack()

        b = Button(window, text='Close', command=window.quit())
        b.pack()

        window.mainloop()

    # open the password window with text field and buttons
    def open_pw(self):
        abc = Tk()

        pw_label = Label(abc, text='Password:', height=2)
        pw_label.pack()

        self.E5 = Entry(abc, bd=5, show='*', width=30)
        self.E5.pack()

        pw_submit = Button(abc, text='Submit', command=self.submit, height=2, width=10)
        pw_submit.pack()

        pw_cancel = Button(abc, text='Cancel', command=quit, height=2, width=10)
        pw_cancel.pack()

        abc.mainloop()
        #self.newWindow = Toplevel(self.master)
        #w = pw_window(self.newWindow)

    # submit the data to be processed by the server
    def submit(self):
        # initialize message info
        to_email = self.E1.get()
        from_email = self.E2.get()
        subject = self.E3.get()
        body = self.E4.get('1.0', END)
        password = self.E5.get()

        # create SMTP server and login
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
        #server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        frame.quit()

    # close the password window
    def quit(self):
        self.destroy()

# create initial window with emailWindow class properties
root = Tk()
w = emailWindow(root)
root.mainloop()
