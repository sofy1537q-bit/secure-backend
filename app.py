# 🔥 FINAL FLASK SERVER (RENDER READY) 🔥

from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)

# 🔐 مفتاح التشفير (ثابت)
key = Fernet.generate_key()
cipher = Fernet(key)

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "mustafa" and password == "1234":
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})

# ---------------- TEXT ----------------
@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    text = data.get("text")

    encrypted = cipher.encrypt(text.encode())

    return jsonify({
        "ciphertext": base64.b64encode(encrypted).decode(),
        "nonce": "none"
    })

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    ciphertext = data.get("ciphertext")

    decrypted = cipher.decrypt(base64.b64decode(ciphertext)).decode()

    return jsonify({
        "plaintext": decrypted
    })

# ---------------- IMAGE ----------------
@app.route("/encrypt_image", methods=["POST"])
def encrypt_image():
    data = request.get_json()
    image_data = base64.b64decode(data.get("image"))

    encrypted = cipher.encrypt(image_data)

    return jsonify({
        "ciphertext": base64.b64encode(encrypted).decode(),
        "nonce": "none"
    })

@app.route("/decrypt_image", methods=["POST"])
def decrypt_image():
    data = request.get_json()
    ciphertext = data.get("ciphertext")

    decrypted = cipher.decrypt(base64.b64decode(ciphertext))

    return jsonify({
        "image": base64.b64encode(decrypted).decode()
    })

# ---------------- TEST ----------------
@app.route("/")
def home():
    return "Server Running 🚀"