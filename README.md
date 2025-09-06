# 🌿 Skinalyze – AI-Powered Personalized Skincare

Skinalyze is an AI-based skincare analysis project that detects **skin types**, identifies **skin issues**, and provides **personalized product recommendations**.  
It leverages **deep learning (MobileNetV2)** for skin type classification, **YOLOv8** for skin issue detection, and a rule-based recommender for skincare products.

---

## 🚀 Features
- ✅ Detects **skin type** (Dry, Normal, Oily) using MobileNetV2.  
- ✅ Identifies **skin issues** (Wrinkles, Redness, Dryness, Acne Levels).  
- ✅ Provides **personalized product recommendations**.  
- ✅ Modular design with separate scripts for training, scraping, and inference.  

---

## 🛠️ Tech Stack
- **Python**  
- **TensorFlow / Keras** – skin type classification (MobileNetV2, EfficientNet)  
- **YOLOv8 (Ultralytics)** – skin issue detection  
- **PIL (Pillow)** – image preprocessing  
- **NumPy / Pandas** – preprocessing & analysis  
- **Custom Rule-Based Engine** – skincare product recommendations  
- **Scrapers** – to gather skincare product data  

---

## 📂 Project Structure

Skinalyze/
│── app.py # Main entry point (skin type + issue detection + recommendations)
│── recommendation.py # Standalone recommendation system
│── skin_model_mobilenetv2_finetuned.h5 # Pretrained MobileNetV2 model (skin type)
│── skin_issue_model.pt # Trained YOLOv8 model (skin issues)
│── training/ # Training scripts for skin type & issue models
│ ├── train_skin_type.py
│ ├── train_skin_issues.py
│── scrapers/ # Web scraping scripts for skincare product data
│ ├── product_scraper.py
│── utils/ # Helper functions (preprocessing, evaluation, etc.)
│── sample_images/ # Test images
│── requirements.txt
│── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/duanoor/skinalyze.git
cd skinalyze
```

### 2️⃣ Setup Virtual Environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Usage
Run Full Analysis (skin type + skin issues + recommendations)
```bash
python app.py path/to/image.jpg
```

Sample Output
```
{
  "skin_type": {
    "predicted_class": "oily",
    "confidence": 0.92
  },
  "skin_issue": {
    "predicted_class": "acne_Level_1",
    "confidence": 0.87
  },
  "recomended_products": [
    "1. Oil-Free Cleanser",
    "2. Acne Spot Treatment",
    "3. Soothing Gel"
  ]
}
```
### 🧪 Run Recommender Only
```bash
python recommendation.py
```

Output
```
Recommended Products:
1. Oil-Free Cleanser
2. Acne Spot Treatment
3. Soothing Gel
```
### 🧑‍🔬 Model Training

Training scripts are available in the directory as well:

typeSkin.py → trains skin type classifier (MobileNetV2/EfficientNet).

skin_issues.py → trains YOLOv8 for detecting wrinkles, acne, redness, etc.

Models provided in this repo are pretrained — retraining is optional if you want to improve performance.

### 🌐 Scrapers

Located in scrapers/ folder.

scraper.py → scrapes skincare product data for recommendation engine.

Extendable for adding new product sources.

### 📌 Future Improvements

Add multi-label detection for multiple skin issues simultaneously.

Expand recommendation engine with real-world product APIs.

Deploy as a web app with frontend + backend integration.

### 👩‍💻 Author

Dua Noor

🎓 CS Graduate ’25 | AI/ML Enthusiast | Computer Vision Explorer

📫 Email: duahashmi47@gmail.com

🌐 GitHub: duahashmi47
