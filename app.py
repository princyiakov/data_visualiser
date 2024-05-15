from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        df = pd.read_csv(file)
        data = df.values.tolist()
        data.insert(0, df.columns.tolist())
        return jsonify(data)
    return jsonify({'error': 'File upload failed'})

if __name__ == '__main__':
    app.run(debug=True)
