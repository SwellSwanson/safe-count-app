from flask import Flask, render_template_string, request
from PIL import Image
import pytesseract


app = Flask(__name__)

@app.route('/')
def index():
    # Serve the HTML form
    return render_template_string(open('index.html').read())

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['slip_image']
    if not file:
        return "No file uploaded", 400

    # Open the image and run OCR
    image = Image.open(file)
    text = pytesseract.image_to_string(image)

    # Here you would parse numbers and calculate totals
    # For now, just return the raw text
    return f"<h2>OCR Result:</h2><pre>{text}</pre>"


if __name__ == '__main__':
    app.run(debug=True)
