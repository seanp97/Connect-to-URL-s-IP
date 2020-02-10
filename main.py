from tkinter import *
import sys
import tkinter
from tkinter import messagebox
import socket

getEnt = ""
port = 0

def getIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = Entry.get(urlPortEnt)
        port = int(port)
        getEnt = Entry.get(urlEnt)
        hostip = socket.gethostbyname(getEnt)
        s.connect((hostip, port))
        urlEmpty.configure(text="Connected to " + hostip)
    except:
        urlEmpty.configure(text="An error occured")

app = Tk()
app.title("Connect to URL's IP")
app.geometry("900x450")

urlPortLabel = Label(app, text="Enter port number", padx=20, pady=20, font='Helvetica 14 bold')
urlPortLabel.grid(column=0, row=0)
urlPortEnt = Entry(app, bd=5)
urlPortEnt.grid(column=0, row=1)

urlLabel = Label(app, text="Connect to IP address of URL provided below", padx=20, pady=20, font='Helvetica 14 bold')
urlLabel.grid(column=0, row=2)

urlEnt = Entry(app, bd=5)
urlEnt.grid(column=0, row=3)

urlBtn = Button(app, text="Submit", command=getIP)
urlBtn.grid(column=0, row=4)

urlEmpty = Label(app, text="", padx=10, pady=20, font='Helvetica 10 bold')
urlEmpty.grid(column=0, row=5)

app.mainloop()
