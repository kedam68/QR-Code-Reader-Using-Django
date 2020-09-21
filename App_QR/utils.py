from pyzbar import pyzbar
import cv2


def convert(qr_image):
    image = cv2.cvtColor(qr_image, cv2.COLOR_BGR2RGB)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        barcodeData = barcode.data.decode("utf-8")
        return barcodeData