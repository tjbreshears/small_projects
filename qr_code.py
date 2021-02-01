import pyqrcode
import png


print("URL/text to make into a QR Code")
text = input(": ")

print("Name your QR Code file")
name = input(": ")
full_name = name + ".png"

# Creating QR code
url=pyqrcode.create(text)

url.show()
url.png(full_name, scale =6)
