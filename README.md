# ☢️ Toxic Shield: AI-Powered Comment Guardian

Toxic Shield is a high-performance, full-stack Deep Learning application designed to detect and categorize toxicity in both text and images. Built with a sleek, neon-themed interface and powered by state-of-the-art NLP models, it provides real-time analysis to keep online communities safe.

---

## 🚀 Features

- **Text Analysis**: Real-time toxicity detection using `Toxic-BERT`.
- **Image OCR**: Extracts text from images using `EasyOCR` for cross-media analysis.
- **Detailed Categorization**: Detects levels of *Toxicity, Severe Toxicity, Obscenity, Threats, Insults,* and *Identity Hate*.
- **Word Attribution**: Highlights specific tokens in the text that triggered the detector.
- **Analysis History**: Persistently tracks previous scans using an integrated SQLite database.
- **Cyberpunk UI**: A modern, responsive React interface with fluid animations using Framer Motion.

---

## 🛠️ Technical Stack

### **Frontend**
- **Framework**: React 18 (Vite)
- **Styling**: Tailwind CSS (Dark Mode/Neon)
- **Animations**: Framer Motion
- **Data Visualization**: Recharts (for toxicity scoring)

### **Backend**
- **API Framework**: FastAPI (Asynchronous Python)
- **DL Models**:
  - `unitary/toxic-bert` (Transformer model for NLP)
  - `EasyOCR` (Computer Vision for text extraction)
- **Database**: SQLite with SQLAlchemy ORM
- **Containerization**: Docker & Docker Compose

---

## 📦 Installation & Setup

### **Prerequisites**
- Docker Desktop installed and running.
- Git installed.

### **Run with Docker (Fastest)**
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/dl-project.git
   cd dl-project
   ```
2. Build and launch:
   ```bash
   docker-compose up --build
   ```
3. Access the application:
   - **Frontend**: [http://localhost:3000](http://localhost:3000)
   - **Backend API**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 How it Works

1. **Input**: Users provide a text snippet or upload an image containing text.
2. **Preprocessing**: The backend cleans the input and extracts text from images if necessary.
3. **Inference**: The `Toxic-BERT` model calculates a probability score (0 to 1) for various toxicity categories.
4. **Attribution**: The system identifies which words contributed most to the score.
5. **Storage**: Results are logged in the database for history tracking.
6. **Visualization**: The React frontend displays the results with dynamic charts and highlighted text.

---

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact
Project Link: [https://github.com/YOUR_USERNAME/dl-project](https://github.com/YOUR_USERNAME/dl-project)
