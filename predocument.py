from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import pytesseract
from PIL import Image
import base64
import io
import numpy as np

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Atur PATH ke Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def perform_ocr(image_data):
    image = cv2.imdecode(np.frombuffer(base64.b64decode(image_data), np.uint8), cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(threshold_image)
    return text

@app.route("/", methods=["GET", "POST"])
def ismpredocument():
    if request.method == "GET":
        return jsonify({"error": "Metode GET tidak diizinkan. Harap gunakan metode POST."})

    try:
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "Tidak ada file"})

        # Baca dan proses gambar menggunakan PIL.Image
        pillow_img = Image.open(file)

        # Konversi gambar menjadi base64
        buffered = io.BytesIO()
        # Simpan gambar dalam format PNG
        pillow_img.save(buffered, format="PNG")
        image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Lakukan OCR pada gambar
        ocr_result = perform_ocr(image_data)

        # Buat kamus untuk output
        output_dict = {
            "fitur": "Konversi Gambar ke Teks",
            "gambar": file.filename,
            "hasil_teks": ocr_result
        }

        respons = jsonify(output_dict)
        # Tambahkan header CORS
        respons.headers.add("Access-Control-Allow-Origin", "*")
        respons.headers.add("Access-Control-Allow-Methods", "GET, POST")

        return respons

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)