import easyocr
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import io

# Initialize reader globally or on first call
# For efficiency in a real dev server, we'll initialize it here.
reader = None

def get_reader():
    global reader
    if reader is None:
        reader = easyocr.Reader(['en'])
    return reader

def extract_text_from_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert('L') # Grayscale
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.filter(ImageFilter.MedianFilter())
    
    ocr_reader = get_reader()
    results = ocr_reader.readtext(np.array(img), detail=0)
    return " ".join(results)
