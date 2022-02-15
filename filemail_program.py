import re
import smtplib
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import askopenfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

roat = Tk()
roat.title("Email Address")
roat.geometry("1050x660")
roat.maxsize(1050, 660)
roat.minsize(1050, 660)

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.pdf')])
   if file:
      filepath = os.path.abspath(file.name)
      global f
      f = filepath
      filepaths.insert(END, str(f))
      

def fetched():
    add = text1.get("1.0", "end-1c")
    global a
    a = re.findall("([\w.-]+@[\w.-]+)", add)
    text2.insert(END, a)

def send():
    emai = emails.get()
    pasw = passw.get()
    subj = sub.get()
    msgss = msgs.get("1.0", "end-1c")
    messagebox.showinfo("Information", "Sending Email Please Wait \n Press Ok To Continue")
    subject= subj
    Lists = a
    msg = MIMEMultipart()
    msg['Subject'] = subject
    body = msgss
    msg.attach(MIMEText(body, 'plain'))
    filename = "Attachment_File.pdf"
    attachment = open(f, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(emai, pasw)
    text = msg.as_string()
    s.sendmail(emai, Lists, text)
    s.quit()
    messagebox.showinfo("Information", "All Email Send Successfully")

    
label = Label(roat, text = "Email Sender", font= "time 25 bold",
              bg = "blue",
              padx = 420,pady = 10 ,fg = "white")
label.place(x = 0, y = 0)

label1 = Label(roat, text = "Enter Your Text :", font= "time 18 bold")
label1.place(x = 22, y = 160)

text1 = Text(roat, width = 50, height = 12, bd = 3)
text1.place(x = 270, y = 80)

label2 = Label(roat, text = "Enter Your Email Address :", font= "time 18 bold")
label2.place(x = 720, y = 80)

emails = Entry(roat, width = 25, bd = 3, font= "time 16 bold")
emails.place(x = 720, y = 125)

label3 = Label(roat, text = "Enter Your Password :", font= "time 18 bold")
label3.place(x = 720, y = 170)

passw = Entry(roat, width = 25, bd = 3, font= "time 16 bold", show = "*")
passw.place(x = 720, y = 215)

label4 = Label(roat, text = "Enter Subject :", font= "time 18 bold")
label4.place(x = 720, y = 260)

sub = Entry(roat, width = 25, bd = 3, font= "time 16 bold")
sub.place(x = 720, y = 300)

label5 = Label(roat, text = "Enter Message :", font= "time 18 bold")
label5.place(x = 720, y = 340)

msgs = Text(roat, width = 38, height = 9, bd = 3)
msgs.place(x = 720, y = 380)

Att = Button(roat, text="Attachment", font = "time 13 bold",
                bg = "#af063f", fg = "white", padx = 30, pady = 5, command=open_file)
Att.place(x = 720, y = 538)

filepaths = Entry(roat, width = 11, bd = 6, font= "time 14")
filepaths.place(x = 890, y = 540)

send = Button(roat, text = "Send Email", font = "time 13 bold",
                bg = "#af063f", fg = "white", padx = 102, pady = 5, command = send)
send.place(x = 720, y = 585)

submit = Button(roat, text = "Submit", font = "time 13 bold",
                bg = "#af063f", fg = "white", padx = 295, pady = 5, command = fetched)
submit.place(x = 20, y = 293)

label2 = Label(roat, text = "Fetched Email addresses :", font= "time 18 bold")
label2.place(x = 22, y = 350)

text2 = Text(roat, width = 72, height = 12, bd = 3, font= "time 12 bold")
text2.place(x = 20, y = 380)

label = Label(roat, text = "", font= "time 25 bold",
              bg = "blue",
              padx = 550,pady = 1,fg = "white")
label.place(x = 0, y = 634)

roat.mainloop()
