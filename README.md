# 🫀 Heart Disease Predictor

A Machine Learning web application that predicts whether a patient has heart disease or not based on clinical data.

> 🔴 **Live Demo:** [Click Here to Try It](https://your-app-name.onrender.com)

---

## 🎯 Objective

Predict whether a patient has **Heart Disease** or **No Disease** based on 10 clinical features using Machine Learning.

---

## 📊 Dataset

- **Source:** [Heart Disease UCI Dataset - Kaggle](https://www.kaggle.com/datasets/navjotkaushal/heart-disease-uci-dataset)
- **Features:** 10
- **Target:** 0 = No Disease / 1 = Disease Present

---

## 🧠 Models Used

| Model | Description |
|---|---|
| Logistic Regression | Simple linear classifier |
| Random Forest | Ensemble of decision trees |
| SVM | Support Vector Machine with RBF kernel |

The best performing model is automatically saved and used for predictions.

---

## ⚙️ Features Used for Prediction

| Feature | Description |
|---|---|
| `age` | Age of the patient |
| `sex` | Sex (1 = Male, 0 = Female) |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl |
| `restecg` | Resting ECG results (0–2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise induced angina |
| `oldpeak` | ST depression induced by exercise |

---

## 🏗️ Project Structure

```
heart-disease-predictor/
│
├── app.py                        ← Flask backend
├── requirements.txt              ← Python dependencies
├── Procfile                      ← Render deployment config
├── best_model.pkl                ← Trained ML model
├── scaler.pkl                    ← Feature scaler
├── heart.csv                     ← Dataset
├── heart_disease_prediction.ipynb ← Full ML notebook
│
└── templates/
    └── index.html                ← Frontend UI
```

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/YourUsername/heart-disease-predictor.git
cd heart-disease-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```
