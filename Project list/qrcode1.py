import qrcode
from PIL import Image
# qr code data legi or change kare gi 
# QRCode functionality ko change karta hai jase ki color or border ko change karta hai
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=8,)

# website ka qr banana hai to qr code
qr.add_data("https://www/wscubetech.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="green",back_color="yellow")
img.save("wscube_web.png")