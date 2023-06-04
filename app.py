import os
from datetime import datetime
from flask import Flask, send_file, request
from model import detect_pothole
from werkzeug.exceptions import BadRequest, InternalServerError

UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.errorhandler(BadRequest)
def bad_request_handler(error):
    return {
        "error": error.description
    }, 400


@app.errorhandler(InternalServerError)
def internal_server_error_handler(error):
    return {
        "error": error.description
    }, 500


@app.route("/predict", methods=['POST'])
def predict():
    file = request.files.get('image')
    if not file:
        return {
            "error": "Image is required"
        }, 400

    supported_mimetypes = ["image/jpeg", "image/png"]
    mimetype = file.content_type
    if mimetype not in supported_mimetypes:
        return {
            "error": "Unsupported image type"
        }, 415

    current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    filename = current_time + '-' + file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    detect_pothole(file_path)
    os.remove(file_path)
    return send_file('darknet/predictions.jpg', mimetype=mimetype)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")