from flask import Flask, request, send_file
from ping3 import ping
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def ping():
    return 'Pong', 200

# Handles Download
@app.route('/download')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def download_file():
    return send_file('testfile.txt', as_attachment=True)  # Downloads 20MB file


# Handle file upload
@app.route('/upload', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def upload_file():
    if 'file' not in request.files:  # Checks if file was sent
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    file.save('uploaded_file.txt')  # Save the file
    return "File uploaded successfully", 200


if __name__ == '__main__':
    # Generate a 20MB file
    file_size = 20 * 1024 * 1024  # 20MB
    with open('testfile.txt', 'wb') as f:
        f.write(os.urandom(file_size))

    app.run(host='0.0.0.0', port=8000)
