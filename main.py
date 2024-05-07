from fastapi import FastAPI, File, UploadFile
import shutil

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

app = FastAPI()


@app.post("/ocr")
def ocr(image: UploadFile = File(...)):
    filePath = "txtfile"
    with open(filePath, "wb") as file:
        shutil.copyfileobj(image.file, file)
    return pytesseract.image_to_string(filePath, lang="eng")
