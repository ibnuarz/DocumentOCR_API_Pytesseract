# OCR Project convert image to text (document) API with Flask, Google Cloud and Pytesseract

This repository contains OCR project convert from image to text using Pytesseract and flask. And deploy to google cloud

## Getting Started

### Prerequisites
- Flask
- gunicorn
- pillow
- flask_cors
- pytesseract

### Installation
1. Clone the repository: `https://github.com/ibnuarz/DocumentOCR_API_Pytesseract.git`
2. Install dependencies: `pip install -r requirements.txt`

### Usage
1. Run the Flask application: `python precolor.py`
2. Upload an image file using the provided HTML form or make POST requests to the `/` endpoint.
3. Receive JSON responses.
4. If you want to run on local, you can use local server default flask example `http://127.0.0.1:5000/` but in this case i use my endpoint that i already deploy from my google cloud.
5. If you want to deploy and make endpoint in cloud use Google Cloud SDK Shell and don't include testing folder.

## License
This project is licensed under the MIT License
