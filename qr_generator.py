import qrcode

qr_text = """Ruwan Wickramanayake
Senior Consultant
Lanka Labs Consultancies"""

img = qrcode.make(qr_text)
img.save("QR.jpg")
