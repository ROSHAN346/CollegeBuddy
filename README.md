# CollegeBuddy 🎓  
**Smart Campus Solutions for Student Empowerment**  

[![GitHub License](https://img.shields.io/github/license/ROSHAN346/CollegeBuddy)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)  
[Frontend]

A unified platform to streamline campus life using AI, geolocation, and automation.  

---

## 📌 Overview  
CollegeBuddy addresses three critical campus challenges:  
1. **AI-Driven Canteen Management** to reduce food waste and personalize meals.  
2. **Digital Lost & Found System** for item recovery via geolocation.  
3. **Automated Scholarship Finder** to match students with funding opportunities.  

---

## 🛠️ Modules & Technical Implementation  

### 1. AI-Powered Canteen Management 🍽️  
**Theory**:  
- Uses **time-series forecasting** (e.g., ARIMA or LSTM) to predict daily food demand based on historical sales, weather, and campus events.  
- **Nutritional analysis** via integrated APIs (e.g., Edamam) to suggest balanced meals.  
- Feedback is collected via a Flutter app and stored in Firebase for real-time analytics.  

**Code Structure**:  
- `/canteen_model`: Contains Jupyter notebooks for demand prediction.  
- `/backend/canteen_api`: Flask API endpoints for menu recommendations.  
- `/frontend/canteen`: Flutter UI for students to submit feedback.  

### 2. Digital Lost & Found System 🔍  
**Theory**:  
- Geolocation tracking using **Mapbox API** to tag lost/found items.  
- Image recognition (e.g., TensorFlow Lite) to match lost item photos with found reports.  
- Push notifications via Firebase Cloud Messaging (FCM).  

**Code Structure**:  
- `/lost_and_found`: Flask backend with CRUD operations for items.  
- `/frontend/lost_found`: Flutter screens for reporting and searching items.  
- `model_matching.py`: Image similarity model using OpenCV.  

### 3. Automated Scholarship Finder 💸  
**Theory**:  
- Web scraping (e.g., BeautifulSoup) to aggregate scholarships from government portals.  
- **Rule-based matching** using student profiles (grades, income, interests).  
- Notifications via Twilio SMS or Nodemailer.  

**Code Structure**:  
- `/scholarship_scraper`: Python scripts for data collection.  
- `/backend/scholarship_api`: REST endpoints for profile matching.  
- `/frontend/scholarship`: Flutter UI for student profiles.  

---

## 🚀 Installation  

### Prerequisites  
- Python 3.9+, Flutter 3.0+, Firebase CLI.  
- API keys for Mapbox, Edamam, and Twilio (add to `.env`).  

### Steps  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/ROSHAN346/CollegeBuddy.git  
   cd CollegeBuddy  

Install dependencies: 

# Backend (Flask)  
pip install -r backend/requirements.txt  

# Frontend (Flutter)  
cd frontend && flutter pub get   

Configure environment variables:
Create .env in /backend:

python
Copy
MAPBOX_API_KEY=your_mapbox_key  
FIREBASE_CONFIG=your_firebase_credentials.json  
Run the backend:

bash
Copy
cd backend  
python app.py  
Run the Flutter app:

bash
Copy
cd frontend  
flutter run  
🌟 Usage
Canteen Module:

Students view predicted menus on the app.

Submit feedback to refine AI predictions.

Lost & Found:

Report lost items with photos and location.

Receive alerts when a match is found.

Scholarship Finder:

Fill in your profile (grades, interests).

Get matched scholarships and deadline reminders.

📂 Repository Structure
Copy
CollegeBuddy/  
├── backend/                 # Rest APIs  
│   ├── canteen_api/         # Demand prediction endpoints  
│   ├── lost_and_found/      # CRUD logic  
│   └── scholarship_api/     # Profile matching  
├── frontend/                # Django 
│   ├── canteen/             # UI for meal feedback  
│   ├── lost_found/          # Item reporting screens  
│   └── scholarship/         # Profile form  
├── canteen_model/           # Jupyter notebooks for AI models  
├── scholarship_scraper/     # Web scraping scripts  
└── README.md  
🤝 How to Contribute
Fork the repository.

Create a branch: git checkout -b feature/your-feature.

Follow the coding style in existing modules.

Submit a PR with a clear description.

📜 License
MIT License. See LICENSE for details.

Built with ❤️ by Roshan

Copy

---

### Key Additions Based on Your Code:  
1. **Repository Structure**: Reflects your actual directories (e.g., `canteen_model`, `scholarship_scraper`).  
2. **Technology Alignment**:  
   - **Flask** for backend (assuming from `app.py`).  
   - **Flutter** for frontend (if your UI code uses Dart files).  
   - **Firebase** for auth/notifications (common in Flutter apps).  
3. **Theoretical Explanations**: Links code components (e.g., `model_matching.py`) to their purpose (image recognition).  

Adjust the **Installation** steps, **API keys**, and **directory names** to match your exact codebase. Add screenshots or GIFs of your app in action if available!
