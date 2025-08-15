# 🎙️ Speech-to-Text API using OpenAI Whisper

A lightweight **FastAPI** service that converts speech to text using **OpenAI's Whisper API**.  
Supports multiple audio formats and returns high-accuracy transcriptions in JSON format.

---

## 📌 Features
- **Multi-format audio support**: `.wav`, `.mp3`, `.webm`, `.ogg`
- **High accuracy** transcription powered by OpenAI Whisper
- **FastAPI** backend for speed & scalability
- Secure API key management using `.env`
- Temporary file handling with `tempfile`

---

## 📂 Project Structure
stt_module/
│
├── __init__.py         # Marks the folder as a Python package
├── config.py           # Environment variables and configuration
├── requirements.txt    # Python dependencies
├── main.py              # FastAPI app entry point
├── stt_service.py      # Speech-to-text logic implementation
├── utils.py            # Helper functions
├── README.md           # Project documentation




---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AroonKumarr/voice_chatbot.git
cd speech-to-text-api
2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here
🚀 Running the API


uvicorn main:app --reload
The server will start at:
http://127.0.0.1:8000

📡 API Endpoints
POST /transcribe
Description: Accepts an audio file and returns the transcription.

Request:
Method: POST

Form-data:

file: Audio file (.wav, .mp3, .webm, .ogg)

Example:
curl -X POST "http://127.0.0.1:8000/transcribe" \
  -H "accept: application/json" \
  -F "file=@sample.mp3"

Response:
{
  "transcription": "Hello, this is a test audio file."
}
🛠️ Tech Stack
Python 3.8+

FastAPI - API framework

Uvicorn - ASGI server

OpenAI Whisper API - Speech-to-text engine

python-dotenv - Environment variable management

📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.

👨‍💻 Author

📧 afnanshoukat35@gmail.com


---

If you want, I can also **add a “Research & Development” section** directly into this README so it’s ready for your university submission without a separate report. That way, you don’t have to rewrite it later.  
