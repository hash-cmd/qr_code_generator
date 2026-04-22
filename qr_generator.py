import qrcode
from PIL import Image

# Data to encode
data = "https://apply.tucee.edu.gh/voucher/purchase"

qr = qrcode.QRCode(
    version=1,  # size of QR Code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=20,  # Increased resolution
    border=2,   # Smaller border
)

qr.add_data(data)
qr.make(fit=True)

# Ensure image is in RGB for saving as PNG/WebP
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load and prepare logo
logo = Image.open("images/tict.webp")
logo = logo.convert("RGBA")  # Ensure we have alpha channel for masking

# Calculate logo size (aim for ~22% of QR code size)
qr_width, qr_height = img.size
logo_size = qr_width // 4  # Roughly 112px for a 450px QR
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Calculate positioning
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Create a white "island" for the logo so it stands out
white_background = Image.new("RGBA", (logo_size, logo_size), "white")
img.paste(white_background, pos)

# Paste logo onto the white island
img.paste(logo, pos, mask=logo)

import os

# Save final QR code
output_file = "tict_voucher_qr.png"
img.save(output_file)

# Also save as my_qrcode.png in case the user is looking for that
img.save("my_qrcode.png")

print(f"✅ Success! QR code saved to: {os.path.abspath(output_file)}")
print(f"✅ Also saved a copy to: {os.path.abspath('my_qrcode.png')}")
