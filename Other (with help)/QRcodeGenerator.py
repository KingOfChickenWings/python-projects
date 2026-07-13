import qrcode

# img = qrcode.make('youtube.com')
# img.save('QRcodeTest.png')

image_link = input("Enter the text or URL: ").strip()
file_name = input(
    "Enter the filename (with extension like .jpg or .png): ").strip()

QR_code = qrcode.make(image_link)
QR_code.save(file_name)

print(f'QR code saved as {file_name}')
