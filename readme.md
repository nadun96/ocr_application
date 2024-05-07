# OCR Service

This is a simple OCR (Optical Character Recognition) service built with FastAPI and PyTesseract.

## Installation

1. Clone the repository
2. Install the dependencies using pip:
    ```
    pip install fastapi uvicorn pytesseract
    ```
3. Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki). After installation, update the `tesseract_cmd` path in `main.py` to your own Tesseract path.

## Usage

1. Run the server:
    ```
    uvicorn main:app --reload
    ```
2. Send a POST request to `http://localhost:8000/ocr` with an image file. The service will return the recognized text from the image.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)