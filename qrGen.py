import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def createQR(text):
    originalQR = qrcode.make(text)
    type(originalQR)
    resizedQR = originalQR.resize((290, 290))
    resizedQR.save("qr.png")

def decodeQR(path):
    qr = decode(Image.open(path))
    return qr[0].data.decode('ascii')

