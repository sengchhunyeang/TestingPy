import qrcode

qr = qrcode.QRCode(
    version=1,          # Size (1 is smallest, 40 is largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error tolerance
    box_size=1,        # Size of each square
    border=4,           # Size of border
)
enter = input("Enter text or URL for QR code: ")
img = qrcode.make(enter)
img.save("qrcodegen.png") 