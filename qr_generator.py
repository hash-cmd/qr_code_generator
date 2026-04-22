import qrcode
import os
from PIL import Image

# Data to encode
data = "https://example.com"

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

# Load and prepare logo (Optional)
# Change "logo.png" to your actual logo file path
logo_path = "logo.png" 

# Dynamic check for logo folder fallback
if not os.path.exists(logo_path) and os.path.exists("images/tict.webp"):
    logo_path = "images/tict.webp"

# Only attempt to embed the logo if it exists
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    logo = logo.convert("RGBA")  # Ensure we have alpha channel for masking

    # Calculate logo size (aim for ~22% of QR code size)
    qr_width, qr_height = img.size
    logo_size = qr_width // 4  
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    # Calculate positioning
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Create a white "island" for the logo so it stands out
    white_background = Image.new("RGBA", (logo_size, logo_size), "white")
    img.paste(white_background, pos)

    # Paste logo onto the white island
    img.paste(logo, pos, mask=logo)
    print(f"🎨 Logo embedded: {logo_path}")
else:
    print("ℹ️ No logo found. Generating a plain QR code.")

# Save final QR code
output_file = "qrcode_with_logo.png"
if not os.path.exists(logo_path):
    output_file = "qrcode_plain.png"

img.save(output_file)

print(f"✅ Success! QR code saved to: {os.path.abspath(output_file)}")
