import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Setup folder to store uploaded handwriting photos
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Placeholder for AI Transcription logic
        # For now, we return a success message to the dashboard
        return jsonify({
            "status": "success",
            "filename": filename,
            "transcription": "AI ANALYSIS COMPLETE: This is where the AI would turn your handwritten ink into typed text. The system has detected your handwriting and preserved your unique author voice!"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
