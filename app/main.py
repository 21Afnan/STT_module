from fastapi import FastAPI, File, UploadFile, Body
from fastapi.middleware.cors import CORSMiddleware
from .stt_service import transcribe_audio_file
from .chat_service import get_chat_response
from fastapi.responses import FileResponse
app = FastAPI(title="STT Module")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change 1 in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return FileResponse("index.html") # Change 2: For frontend: Serve index.html
@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        text = transcribe_audio_file(file_bytes, file.filename)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
@app.post("/chat")
async def chat(payload: dict = Body(...)):
    message = payload.get("message", "").strip()
    if not message:
        return {"error": "No message provided"}
    try:
        reply = get_chat_response(message)
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}
