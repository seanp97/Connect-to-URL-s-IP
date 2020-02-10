from tkinter import *
import sys
import tkinter
from tkinter import messagebox
import socket

getEnt = ""

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 80
    getEnt = Entry.get(urlEnt)
    print(getEnt)
    hostip = socket.gethostbyname(getEnt)
    s.connect((hostip, port))
    urlEmpty.configure(text="Connected to " + hostip)

app = Tk()
app.title("Connect to URL's IP")
app.geometry("900x450")

urlLabel = Label(app, text="Connect to IP address of URL provided below", padx=20, pady=20, font='Helvetica 14 bold')
urlLabel.grid(column=0, row=0)

urlEnt = Entry(app, bd=5)
urlEnt.grid(column=0, row=1)

urlBtn = Button(app, text="Submit", command=getIP)
urlBtn.grid(column=0, row=2)

urlEmpty = Label(app, text="", padx=10, pady=20, font='Helvetica 10 bold')
urlEmpty.grid(column=0, row=3)

app.mainloop()