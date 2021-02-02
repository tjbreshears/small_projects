import pyqrcode
import png
import os

print("URL/text to make into a QR Code")
text = input(": ")

print("Name your QR Code file")
name = input(": ")
full_name = name + ".png"

# Create QR code
url=pyqrcode.create(text, error = 'M')

#Find current user's desktop and change directory.
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)

#Make QR code png
url.show()
url.png(full_name, scale =6)
