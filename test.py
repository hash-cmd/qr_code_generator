import qrcode
from PIL import Image

# Data to encode
data = "https://icounselgh.tuceewellness.com/psychometric/generate"

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
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Open your logo image
logo = Image.open("logo.png")  # Replace with your logo file path

# Resize logo (optional: adjust depending on QR size)
logo_size = 60
logo = logo.resize((logo_size, logo_size))

# Calculate positioning for logo at center
pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

# Paste logo onto QR code
img.paste(logo, pos, mask=logo if logo.mode=='RGBA' else None)

# Save final QR code
img.save("my_qrcode_with_logo.png")
