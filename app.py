from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("pneumonia_model_mobilenetv2.h5")

def predict_image(file_path):
    img = image.load_img(file_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0) / 255.
    prob = model.predict(img_tensor)[0][0]
    label = "Pneumonia" if prob > 0.5 else "Normal"
    confidence = round(prob * 100, 2) if label == "Pneumonia" else round((1 - prob) * 100, 2)
    return label, confidence, prob

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = []
    files_saved = []

    if request.method == 'POST':
        files = request.files.getlist('images')
        for file in files:
            filepath = os.path.join('static', file.filename)
            file.save(filepath)
            label, confidence, prob = predict_image(filepath)
            predictions.append({
                'filename': file.filename,
                'label': label,
                'confidence': confidence,
                'prob': round(prob, 4)
            })
            files_saved.append(filepath)

        return render_template('index.html',
                               predictions=predictions,
                               image_paths=files_saved)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
