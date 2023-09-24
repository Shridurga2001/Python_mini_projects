# pip3 install qrcode Image 
import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 9,
        border =5,   
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="pink", back_color = "white")
    img.save("qrcode1.png")

print("QRCODE GENERATOR")
print("")
link = input("Enter any Link: ")
generate_qrcode(link)