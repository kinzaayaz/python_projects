import qrcode
data = input("Enter the text or URL to generate a QR Code: ")
filename = input("Enter a filename to save (without extension): ") + ".png"
qr=qrcode.make(data)
qr.save(filename)
print(f"QR Code saved as {filename}")