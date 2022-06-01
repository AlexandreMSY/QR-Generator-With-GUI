from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import qrGen
import os

def submitFunction():
    url = userLink.get()
    qrGen.createQR(url)

    qr.config(file="qr.png")
    display.config(image=qr)

def decodeFunction():
    try:
        image = filedialog.askopenfilename(filetypes=[("PNG", ".png"), ("GIF", ".gif"), ("JPG", ".jpg")])
        decodedQR = str(qrGen.decodeQR(image))
        userLink.insert(0, decodedQR)

    except IndexError:
        messagebox.showwarning(title="Error!", message="Invalid Picture")

def saveFunction():
    qr = Image.open("qr.png")
    path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", ".png"), ("GIF", ".gif"), ("JPG", ".jpg")])

    qr.save(path)
        
#window configs
window = Tk()
window.config(bg="lightgrey")
window.geometry("1000x400")
window.resizable(width=False, height=False)

placeHolder = PhotoImage(file='bground.png')
qr = PhotoImage(file='bground.png')

#left frame
frame = Frame(window, borderwidth=1, bg="lightgrey")

linkText = Label(frame,text="URL: ", font=("Arial", 13), bg="lightgrey").grid(row=0, column=0)
userLink = Entry(frame,font=("Arial", 10), width=55)
userLink.grid(row=0, column=1)

submit = Button(frame, text="Submit", font=("Arial", 13), borderwidth=2, relief=SOLID, width=20, bg="lightgrey", command=submitFunction).grid(row=2, column=1, pady=3)
loadImage = Button(frame, text="Load Image", font=("Arial", 13), borderwidth=2, relief=SOLID, width=20, bg="lightgrey", command=decodeFunction).grid(row=3, column=1, pady=3)
saveImage = Button(frame, text="Save Image", font=("Arial", 13), borderwidth=2, relief=SOLID, width=20, bg="lightgrey", command=saveFunction).grid(row=4, column=1, pady= 3)

frame.pack(side=LEFT)

#display image frame
imageFrame = Frame(window)

display = Label(imageFrame, image=placeHolder)
display.pack()

imageFrame.pack(side=RIGHT, padx=80)

window.mainloop()

os.remove("qr.png")

#test