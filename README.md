# ☢️ ToxicScan: AI-Powered Comment Guardian

🚀 **Live Demo:** [https://toxic-comment-analyzer-1wr9.onrender.com](https://toxic-comment-analyzer-1wr9.onrender.com)

ToxicScan is a high-performance, full-stack AI Laboratory application designed to detect and categorize toxicity in both text and images. Built with a sophisticated light-themed interface and powered by state-of-the-art NLP models via the Hugging Face Inference API, it provides real-time analysis with lightning-fast response times.

---

## 🚀 Features

- **Text Analysis**: Real-time toxicity detection using `Toxic-BERT` via high-speed API.
- **Image OCR**: Extracts text from images using `EasyOCR` for cross-media analysis.
- **Detailed Categorization**: Detects levels of *Toxicity, Severe Toxicity, Obscenity, Threats, Insults,* and *Identity Hate*.
- **Word Attribution**: Highlights specific tokens in the text that triggered the detector with wavy animations.
- **Analysis History**: Persistently tracks previous scans using an integrated SQLite database.
- **AI-Lab UI**: A professional, premium light-themed interface with fluid animations using Framer Motion.
- **Floating Toxic Visuals**: Dynamic floating "toxic" elements that react to the user's presence.

---

## 🛠️ Technical Stack

### **Frontend**
- **Framework**: React 18 (Vite)
- **Styling**: Tailwind CSS (Premium Light Theme)
- **Animations**: Framer Motion
- **Data Visualization**: Recharts (for toxicity scoring)

### **Backend**
- **API Framework**: FastAPI (Asynchronous Python)
- **AI Engine**: 
  - `Hugging Face Inference API` (For fast `Toxic-BERT` text analysis)
  - `EasyOCR` (Computer Vision for text extraction from images)
- **Database**: SQLite with SQLAlchemy ORM
- **Containerization**: Docker & Docker Compose (with Hot Module Replacement)

---

## 📦 Installation & Setup

### **Prerequisites**
- Docker Desktop installed and running.
- Hugging Face API Key (Free)

### **Run with Docker (Live Dev Mode)**
1. Clone the repository:
   ```bash
   git clone https://github.com/Alisha-bhatti/Toxic-Comment-Analyzer.git
   cd Toxic-Comment-Analyzer
   ```
2. Set your Hugging Face API Key:
   ```bash
   $env:HF_API_KEY="your_token_here"
   ```
3. Build and launch:
   ```bash
   docker-compose up --build
   ```
4. Access the application:
   - **Frontend**: [http://localhost:3000](http://localhost:3000)
   - **Backend API**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 How it Works

1. **Input**: Users provide a text snippet or upload an image containing text.
2. **Preprocessing**: The backend cleans the input and extracts text from images if necessary.
3. **Inference**: The system calls the `Toxic-BERT` model via Hugging Face for instant probability scoring.
4. **Attribution**: The system identifies which words contributed most to the score.
5. **Storage**: Results are logged in the database for history tracking.
6. **Visualization**: The React frontend displays the results with dynamic charts and highlighted text animations.
