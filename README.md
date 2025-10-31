# 🧠 Detectify.AI – Fake Media Detection using Deep Learning

## 🚀 Overview

**Detectify.AI** is an AI-powered application designed to detect whether an uploaded **image** or **video** is *real* or *fake*.
With the rapid growth of generative AI and synthetic media, distinguishing real from fake content has become critical for digital trust and online safety.

This project leverages **Deep Learning models** and **computer vision** techniques to analyze visual cues, facial inconsistencies, and spatio-temporal patterns in videos to accurately detect deepfakes in real time.

---

## 🎯 Problem Statement

Deepfakes can spread misinformation, create reputational damage, and undermine public trust.
The challenge is to build a **robust, scalable, and accurate deepfake detection system** capable of working on both **images** and **videos** uploaded by users.

---

## 🧩 Solution

We built a **web-based application** that:

1. Accepts **image** or **video** uploads.
2. Runs a **deepfake detection model** (EfficientNet / Vision Transformer / RNN-based).
3. Generates a **confidence score** indicating how likely the media is fake.
4. Works in **real time** using GPU-accelerated inference.

---

## ⚙️ Tech Stack

| Category           | Tools/Frameworks                                                       |
| ------------------ | ---------------------------------------------------------------------- |
| **Frontend**       | Streamlit                                                              |
| **Deep Learning**  | PyTorch / TensorFlow                                                   |
| **Models Used**    | EfficientNet, Vision Transformer (ViT)                                 |
| **Storage**        | Local                                                                  |

---

## 🧠 Model Architecture

* **For Images:** pre-trained ViT base family of EfficientNet trained on `deepfake and reali mages` .
* **For Videos:**  EfficientNet-B0 for feature extraction and Transformer-based temporal modeling with classification head

---

## 💡 Key Features

✅ Detects fake content in both **images** and **videos**
✅ Supports multiple input formats (JPG, PNG, MP4)
✅ Provides **confidence scores** (e.g., “Fake – 87% confidence”)
✅ Simple **web interface** for non-technical users
✅ Modular architecture for easy **model swapping**

---

## 🧰 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/DeepFakeShield.git
cd DeepFakeShield
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Access the UI

Open your browser at `http://localhost:8000` (or the Streamlit app if using Streamlit).

---

## 📊 Example Output

**Input:** `fake_video.mp4`
**Output:**

```
Result: FAKE
Confidence: 92.4%
Visualization: Grad-CAM heatmap highlighting altered facial regions
```

---

## 📁 Project Structure

```
DeepFakeShield/
│
├── app/
│   ├── main.py                 # FastAPI backend
│   ├── model_loader.py         # Model loading logic
│   ├── inference.py            # Image/Video inference
│   ├── utils.py                # Helper functions
│
├── frontend/                   # Streamlit or React frontend
│
├── models/                     # Pre-trained weights
│
├── data/                       # Sample inputs
│
├── requirements.txt
└── README.md
```

---

## 🧪 Datasets Used

* [FaceForensics++](https://github.com/ondyari/FaceForensics)
* [DeepFake Detection Challenge Dataset (DFDC)](https://ai.facebook.com/datasets/dfdc)
* [Celeb-DF v2](https://github.com/yuezunli/celeb-deepfakeforensics)

---

## ⚡ Future Enhancements

* 🔹 Add **audio-based** deepfake detection
* 🔹 Integrate **transformer-based multimodal models**
* 🔹 Real-time deepfake detection via webcam stream
* 🔹 Support for **mobile app interface**

---

## 🏆 Hackathon Impact

This solution empowers users, media agencies, and fact-checkers to:

* Detect manipulated content early
* Build trust in shared media
* Promote AI safety and responsible AI usage

---

## 👥 Team Members

| Name         | Role         | Responsibility                 |
| ------------ | ------------ | ------------------------------ |
| [Your Name]  | ML Engineer  | Model training & optimization  |
| [Teammate 1] | Backend Dev  | API & inference service        |
| [Teammate 2] | Frontend Dev | UI/UX & visualization          |
| [Teammate 3] | Researcher   | Dataset preparation & analysis |

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

Would you like me to tailor this README specifically to your **Stack (e.g., FastAPI + Streamlit + PyTorch)** and the **model types you’re using (e.g., CNN, 3D CNN, or ViT)** so it looks more realistic for your submission?
