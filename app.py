<<<<<<< HEAD
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from io import BytesIO
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
app = Flask(__name__)
model = load_model("pneumonia_model_mobilenetv2.h5")

def predict_image(file_stream):
    img = Image.open(BytesIO(file_stream.read())).convert("RGB")
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_tensor = np.expand_dims(img_array, axis=0)
    prob = model.predict(img_tensor)[0][0]
    label = "Pneumonia" if prob > 0.5 else "Normal"
    confidence = round(prob * 100, 2) if label == "Pneumonia" else round((1 - prob) * 100, 2)
    return label, confidence, prob

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = []
    if request.method == 'POST':
        files = request.files.getlist('images')
        for file in files:
            label, confidence, prob = predict_image(file)
            predictions.append({
                'filename': file.filename,
                'label': label,
                'confidence': confidence,
                'prob': round(prob, 4)
            })
    return render_template('index.html', predictions=predictions)

if __name__ == '__main__':
    app.run()
=======
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from io import BytesIO

app = Flask(__name__)
model = load_model("pneumonia_model_mobilenetv2.h5")

def predict_image(file_stream):
    img = Image.open(BytesIO(file_stream.read())).convert("RGB")
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_tensor = np.expand_dims(img_array, axis=0)
    prob = model.predict(img_tensor)[0][0]
    label = "Pneumonia" if prob > 0.5 else "Normal"
    confidence = round(prob * 100, 2) if label == "Pneumonia" else round((1 - prob) * 100, 2)
    return label, confidence, prob

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = []
    if request.method == 'POST':
        files = request.files.getlist('images')
        for file in files:
            label, confidence, prob = predict_image(file)
            predictions.append({
                'filename': file.filename,
                'label': label,
                'confidence': confidence,
                'prob': round(prob, 4)
            })
    return render_template('index.html', predictions=predictions)

if __name__ == '__main__':
    app.run()
>>>>>>> bf01a4b (Initial commit)
