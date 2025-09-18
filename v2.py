from flask import Flask, request, render_template
from PIL import Image
import pytesseract

app = Flask(__name__)

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

# Handle manual input
@app.route("/calculate", methods=["POST"])
def calculate():
    # Bills
    hundreds = int(request.form.get("hundreds", 0))
    fifties = int(request.form.get("fifties", 0))
    twenties = int(request.form.get("twenties", 0))
    tens = int(request.form.get("tens", 0))
    fives = int(request.form.get("fives", 0))
    ones = int(request.form.get("ones", 0))

    # Coin rolls
    pennies = int(request.form.get("pennies", 0))
    nickels = int(request.form.get("nickels", 0))
    dimes = int(request.form.get("dimes", 0))
    quarters = int(request.form.get("quarters", 0))

    total = (
        hundreds*100 + fifties*50 + twenties*20 + tens*10 + fives*5 + ones*1 +
        pennies*0.50 + nickels*2 + dimes*5 + quarters*10
    )

    return f"<h2>Total: ${total:.2f}</h2>"

# Handle file upload
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("slip_image")
    if not file:
        return "No file uploaded", 400

    image = Image.open(file)
    text = pytesseract.image_to_string(image)

    # Optional: parse numbers from text here
    return f"<h2>OCR Result:</h2><pre>{text}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
