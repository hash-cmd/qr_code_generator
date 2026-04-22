# 📱 QR Code Generator with Logo Embedding

A high-performance Python utility for generating professional QR codes. This tool features a smart "island" background for centered logos, ensuring maximum visibility and scannability even with complex branding.

## ✨ Features

- **Optional Logo Embedding**: Smoothly generates plain QR codes if no logo is found, or beautifully embeds a logo if provided.
- **"White Island" Protection**: Automatically draws a clean white background behind the logo to prevent QR modules from interfering with your branding.
- **Smart Detection**: Automatically searches for `logo.png` in the root directory or falls back to an existing asset in the `images/` folder.
- **High Error Correction**: Uses `ERROR_CORRECT_H` (High) as the default, allowing up to 30% of the code to be obscured while remaining fully functional.
- **Premium Resolution**: Configurable `box_size` (default is 20) for crisp, professional images suitable for print and digital use.

## 📋 Prerequisites

- **Python 3.x**
- **Libraries**:
    - [qrcode[pil]](https://pypi.org/project/qrcode/) - For core generation.
    - [Pillow](https://python-pillow.org/) - For advanced image processing.

## 🛠️ Installation

1. **Activate your environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install requirements**:
   ```bash
   pip install qrcode[pil]
   ```

## 📂 Project Structure

- `qr_generator.py`: The single main script containing all generation logic.
- `images/`: Directory for default or fallback logo assets.
- `qrcode_with_logo.png`: Output generated when a logo is detected.
- `qrcode_plain.png`: Output generated when running without a logo.

## 🖥️ Usage

Simply run the main script:

```bash
python3 qr_generator.py
```

### How to use a Custom Logo:
Place your logo image in the project root and name it **`logo.png`**. The script will automatically detect it, resize it, and center it with the protective white background.

If no logo is found, the script will gracefully generate a plain QR code named `qrcode_plain.png`.

## 📝 Configuration

Open `qr_generator.py` to easily customize:

- `data`: The URL, text, or data you want to encode.
- `box_size`: The resolution of the QR (higher = larger file).
- `logo_size`: The relative size of the center logo.

---
*Maintained for Public and Professional Use.*
