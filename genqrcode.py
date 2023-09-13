import qrcode
from datetime import datetime

print("QR Code Generator Program")
print("Please type 'exit' to exit program.")

while True:
    data = input("Please Enter your qrcode data : ")
    if data == "exit":
        break
    else:
        img = qrcode.make(f'{data}')
        type(img)  # qrcode.image.pil.PilImage
        img.save(
            f"QRcodeimg/{datetime.today().strftime('%Y-%m-%d-%H-%M-%S')}.png")
        print("QR Code Image Saved")
