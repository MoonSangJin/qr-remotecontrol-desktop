from tkinter import *
import qrcode
from PIL import ImageTk, Image
import socket
import remocon

SOCKET_IP = socket.gethostbyname_ex( socket.gethostname() )[-1][-1]
SOCKET_PORT = 9220

def openServer():
    webClientURL = "http://{}:5500/button.html?ip={}&port={}".format( SOCKET_IP, SOCKET_IP, SOCKET_PORT)
    print("Client: ", webClientURL)
    qrcodeImage = qrcode.make(webClientURL)
    # qrcodeImage.resize(150, 150, Image.ANTIALIAS)
    qrcodePhotoImage = ImageTk.PhotoImage(qrcodeImage)
    qrcodeLabel = Label(root, image=qrcodePhotoImage)
    qrcodeLabel.grid(row=3, column=0, columnspan=2)
    root.update()

    remocon.run( portText.get() )

root = Tk()

ipLabel = Label(root, text="IP : {}".format(SOCKET_IP))
ipLabel.grid(row=0, column=0, columnspan=2, sticky=W)
portLabel = Label(root, text="Port : ")
portLabel.grid(row=1, column=0, sticky=W)
portText = Entry(root)
portText.grid(row=1, column=1, sticky=W)
portText.insert(0, SOCKET_PORT)

openBtn = Button(root, text ="Open server", command=openServer)
openBtn.grid(row=2, column=0, columnspan=2)

root.mainloop()