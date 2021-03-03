import os,sys
import tkinter as ui
from tkinter import messagebox as mb
import subprocess as sp
import http.server
import socketserver
import socket
alive="Server is running..."
dead="Server is stopped..."
chk="Type port number and click start."
server=dead
runOnce=False
CREATE_NO_WINDOW = 0x08000000
handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
def donate():
    newWindow = ui.Toplevel(window)
    newWindow.geometry("525x275")
    newWindow.resizable(0,0)
    labelExample = ui.Label(newWindow, text = "Any amount is appreciated.")
    donatee = ui.Text(newWindow)
    labelExample.pack()
    donatee.pack()
    donatee.insert(ui.END,"BTC: 3NhGAPpkLas1pDdPp7tSeP5ba1gHapq7kb")
    donatee.configure(state='disabled')
def start():
    global server,poll,runOnce
    if runOnce==False:
        try:
            PORT= int(giris_port.get())
            server=sp.Popen(args=[f"python","-m","http.server",f"{PORT}"],creationflags=CREATE_NO_WINDOW, stdout=sp.PIPE,stderr=sp.STDOUT)
            poll=server.poll()
            runOnce=True
        except:
            mb.showerror(title="ERROR", message="Port should be number between 1024-65535")
def terminate():
    global runOnce
    if runOnce==True:
        runOnce=False
        server.terminate()
        stat.configure(text=dead,bg="black",fg="white")
def status():
    global runOnce
    if runOnce==True:
        if poll is None:#proc alive
            stat.configure(text=alive,bg="black",fg="white")
    window.after(3000,status)
if __name__ == '__main__':
    window=ui.Tk()
    window.title("HTTPD Server")
    window.geometry("500x200")
    window.resizable(0,0)
    window.configure(bg="black")
    ui.Label(window,text="IP : ",bg="black",fg="white").grid(row=0,column=0)
    ui.Label(window,text=str(local_ip),bg="black",fg="white").grid(row=0,column=1)
    ui.Label(window,text="Port : ",bg="black",fg="white").grid(row=1,column=0)
    giris_port = ui.Entry(window)
    giris_port.grid(row=1, column=1)
    stat=ui.Label(window,text=chk,bg="black",fg="white")
    stat.grid(row=2,column=0)
    stat.place(x=250,y=150,anchor="center")
    button1=ui.Button(text="Start",width=20,height=1,bg="green",fg="white",command=start)
    button1.grid(row=3,column=1)
    button2=ui.Button(text="Stop",width=20,height=1,bg="red",fg="white",command=terminate)
    button2.grid(row=3,column=0)
    button3=ui.Button(text="Donate",width=7,height=1,bg="orange",fg="white",command=donate)
    button3.grid(row=4,column=1)
    button3.place(x=455,y=175,anchor="center")
    window.after(3000,status)
    window.mainloop()
