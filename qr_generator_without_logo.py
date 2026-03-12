import qrcode

# Data to encode
data = "https://maps.app.goo.gl/4m4bRmM3qjPXaKKC6"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # size of QR Code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Generate QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save final QR code
img.save("my_qrcode.png")