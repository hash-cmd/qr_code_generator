# TICT Voucher QR Code Generator

A Python-based utility to generate high-resolution QR codes for the TUCEE Institute of Counselling and Technology (TICT) voucher purchase system, featuring centered logo embedding.

## 🚀 Features

- **Branded QR Codes**: Automatically embeds the TICT logo in the center of the QR code.
- **High Error Correction**: Uses `ERROR_CORRECT_H` (High) to ensure the QR remains scannable even with a logo covering part of the data.
- **White "Island" Protection**: Adds a clean white background behind the logo for maximum visibility and better scanning.
- **High Resolution**: Configurable `box_size` for crisp, print-ready images.

## 📋 Prerequisites

- Python 3.x
- [Pillow](https://python-pillow.org/) (Image processing)
- [qrcode](https://pypi.org/project/qrcode/) (QR generation)

## 🛠️ Installation

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install qrcode[pil]
   ```

## 📂 Project Structure

- `qr_generator.py`: The main script with logo embedding and optimized styling.
- `qr_generator_without_logo.py`: A simplified version without branding.
- `images/`: Directory containing the TICT logo (`tict.webp`).
- `tict_voucher_qr.png`: The generated branded QR code.
- `my_qrcode.png`: A copy of the generated QR code.

## 🖥️ Usage

Simply run the main generator script:

```bash
python3 qr_generator.py
```

The script will generate the QR code and save it to the project root. It handles:
- Correcting the URL for voucher purchases.
- Loading the logo from the local `images/` folder.
- Resizing and centering the logo perfectly.

## 📝 Configuration

You can customize the following variables inside `qr_generator.py`:

- `data`: The URL or text to encode.
- `box_size`: Controls the resolution of the QR code (default is 20).
- `logo_size`: Adjusts the size of the center logo.

---
*Created for TUCEE Institute of Counselling and Technology.*
