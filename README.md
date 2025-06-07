# 🫁 Lung X-ray Pneumonia Detection Web App

A smart, AI-powered web application to detect pneumonia from chest X-ray images. Built with a deep learning model (CNN) and deployed via Flask with a modern TailwindCSS-based interface.

---

## 🧩 Problem Statement

Pneumonia is a serious lung infection that requires timely detection for effective treatment. Traditional diagnosis through manual X-ray examination can be time-consuming and error-prone. This project automates pneumonia detection from chest X-rays using a trained deep learning model, offering a quick and accessible web interface for predictions.

---

## 🖼️ Dataset

- **Source**: [Kaggle Chest X-ray Dataset (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
- **Categories**:  
  - `Normal`
  - `Pneumonia`
- **Images**:  
  - 5,000+ grayscale X-ray images
- **Split**:  
  - `train/`, `val/`, `test/` folders

---

## 🧠 Model Details

- **Architecture**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow / Keras
- **Input Size**: 224×224
- **Layers**: 4 convolutional + 2 dense layers
- **Loss**: Binary Crossentropy
- **Optimizer**: Adam

### 🎯 Evaluation Metrics:
| Metric     | Value    |
|------------|----------|
| Accuracy   | ~92%     |
| Precision  | ~91%     |
| Recall     | ~93%     |

---

## 🌐 Web Application Features

- 🖼️ Drag & drop or select multiple X-ray images
- 📊 Real-time probability charts for Normal vs Pneumonia
- 🌙 Dark mode toggle for user comfort
- 📱 Fully responsive UI using Tailwind CSS
- 📚 Educational info section on pneumonia
- 🔗 Easily shareable public web link (after deployment)

---

## 🧪 Try It Locally

### 1️⃣ Clone this repository
```bash
git clone https://github.com/yourusername/pneumonia-detector-webapp.git
cd pneumonia-detector-webapp
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🚀 Deployment

You can deploy the app using:

- 🔹 [Render](https://render.com) (recommended)
- 🔹 Replit
- 🔹 PythonAnywhere

Public link example:
```
https://pneumonia-detector.onrender.com
```

---

## 📦 Requirements

```bash
Flask
tensorflow
pillow
numpy
gunicorn
```

You can save them using:

```bash
pip freeze > requirements.txt
```

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- TensorFlow/Keras
- HTML, Tailwind CSS, JavaScript
- Chart.js

---

## 🙋‍♂️ Author

Developed by **Abhiroop Pamula**  
🔗 [LinkedIn](https://www.linkedin.com/) | ✉️ abhiroop@email.com

---

⭐ **Star this repo if it helped you!**
