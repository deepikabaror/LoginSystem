# youtube lika -- websites QR code
import qrcode as qr
# wscube search youtube and link
img = qr.make("https://www.youtube.com/c/wscubetechjodhpur")
img.save("wscube_youtube.png")
