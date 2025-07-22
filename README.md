# 🎤 Colorful Voice Assistant

A voice-controlled virtual assistant with a stylish and modern web interface using Flask and Python. It accepts spoken commands, responds using speech, and can execute tasks like opening apps, checking time, or browsing the web.

---

## 🧠 Features
- 🎧 Voice input using SpeechRecognition
- 🗣️ Voice output using pyttsx3
- 🌐 Flask web interface with a colorful design
- ⚙️ System command execution (open apps, websites, etc.)
- 📝 Command log interface (User vs Assistant)

---

## 📁 Project Structure
```
voice_assistant/
│
├── app.py                  # Flask backend
├── assistant.py            # Assistant logic (speech, commands)
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Colorful frontend
├── static/
│   └── style.css           # Optional styling file
└── README.md               # This file
``

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/colorful-voice-assistant.git
cd colorful-voice-assistant
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

---

## 💬 Example Voice Commands
- "What is the time?"
- "Open Chrome"
- "Open YouTube"
- "Shutdown the computer" ⚠️

---

## 🛠 Dependencies
- Flask
- SpeechRecognition
- pyttsx3
- subprocess, os, datetime (built-in)

Install them with:
```bash
pip install Flask SpeechRecognition pyttsx3
```

---

## 📄 License
MIT License — Free to use and modify.

---

Made with ❤️ by [Rahul Solanki]
