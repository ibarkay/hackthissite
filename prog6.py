from PIL import Image
import pytesseract

def ocr_core(filename):

    text = pytesseract.image_to_data(filename)
    return text

print(ocr_core('7.png')) #pics gos here
