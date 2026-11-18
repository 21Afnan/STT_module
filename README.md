<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A0D2E,50:C2185B,100:FF8FC7&height=190&section=header&text=STT%20Module&fontSize=52&fontColor=FFFFFF&fontAlignY=36&desc=Speak%20to%20a%20chatbot%3A%20browser%20audio%20in%2C%20text%20out&descSize=16&descAlignY=58" width="100%" alt="STT Module"/>

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/MediaRecorder%20API-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="MediaRecorder"/>
</p>

</div>

---

## Why it exists

Typing is the slowest part of talking to a chatbot. This module lets a user simply speak: the browser records the voice, the API turns it into text, and that text can go straight to any chatbot. It is a small, self-contained service, so it can sit in front of an existing bot without changing it.

It is one of three reusable voice modules I packaged during my Conversational AI internship at Prudential Solutions, where I evaluated and benchmarked GPT-based speech components for an enterprise HR chatbot. Its siblings are [TTS_module](https://github.com/21Afnan/TTS_module) (text to speech) and [STS_module](https://github.com/21Afnan/STS_module) (speech to speech).

## Features

- **Record in the browser:** `index.html` captures the microphone with the MediaRecorder API, with no plugin or app to install.
- **Accurate transcription:** audio is sent to OpenAI's transcription API and the text comes back in a single JSON field.
- **Any common format:** the file extension is kept when the upload is saved, with `.webm` (the browser default) as the fallback.
- **Clean temporary files:** each upload is written to a temp file and deleted as soon as it is transcribed.
- **Chat endpoint included:** the transcript can be passed to `/chat` to get an AI reply, so the whole voice-to-answer loop can be tested from one page.
- **Fails early on setup errors:** the app refuses to start if `OPENAI_API_KEY` is missing.

## API

| Method | Endpoint | Input | Returns |
|---|---|---|---|
| `GET` | `/` | | the recording page |
| `POST` | `/transcribe` | multipart audio file (`file`) | `{"text": "..."}` |
| `POST` | `/chat` | `{"message": "..."}` | `{"reply": "..."}` |

```
Microphone ──> MediaRecorder (webm) ──POST /transcribe──> temp file ──> OpenAI transcription ──> text
                                                                                            │
                                                              POST /chat ──> AI reply <─────┘
```

## Run it

```bash
git clone https://github.com/21Afnan/STT_module.git
cd STT_module
python -m venv venv && venv\Scripts\activate      # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_key_here
```

Start the server and open `http://127.0.0.1:8000`, then allow microphone access:

```bash
uvicorn app.main:app --reload
```

## Project structure

```
STT_module/
├── app/
│   ├── main.py           # FastAPI routes: page, /transcribe, /chat
│   ├── stt_service.py    # audio file to text
│   ├── chat_service.py   # text to AI reply
│   ├── config.py         # loads and checks the API key
│   └── index.html
├── index.html            # recording interface served at /
└── requirements.txt
```

## Tech stack

Python, FastAPI, Uvicorn, OpenAI Python SDK, python-dotenv, python-multipart, HTML and JavaScript (MediaRecorder API).

---

<div align="center">

**Afnan Shoukat**

<a href="mailto:afnanshoukat35@gmail.com"><img src="https://img.shields.io/badge/Email-afnanshoukat35%40gmail.com-FF4FA3?style=for-the-badge&logo=gmail&logoColor=white&labelColor=4A0D2E" alt="Email"/></a>
<a href="https://www.linkedin.com/in/afnanshoukat"><img src="https://img.shields.io/badge/LinkedIn-Afnan%20Shoukat-FF4FA3?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=4A0D2E" alt="LinkedIn"/></a>
<a href="https://github.com/21Afnan"><img src="https://img.shields.io/badge/GitHub-21Afnan-FF4FA3?style=for-the-badge&logo=github&logoColor=white&labelColor=4A0D2E" alt="GitHub"/></a>

</div>

