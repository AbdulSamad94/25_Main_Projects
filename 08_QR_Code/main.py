import qrcode
import cv2

# Generate QR Code

data = "https://github.com/AbdulSamad94"  
qr = qrcode.make(data)
qr.save("./08_QR_Code/qr_code.png") 
qr.show()

# Decode QR Code

img = cv2.imread("./08_QR_Code/qr_code.png")

detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

print("Decoded data:", data)