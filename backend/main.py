import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
import pymysql




timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-127185cc-ogsparrowb-d804.i.aivencloud.com",
  password="AVNS_dXK_PYUiS8iNnJx1_gj",
  read_timeout=timeout,
  port=19856,
  user="avnadmin",
  write_timeout=timeout,
)
  
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.post("/api/chat")
async def chat_with_groq(prompt: dict):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    body = {
        "model": "llama-3.1-8b-instant",   # example Groq model
        "messages": [{"role": "user", "content": prompt["message"]}],
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()

@app.get("/")
async def read_root():
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mytest (id INTEGER PRIMARY KEY)")
        cursor.execute("INSERT IGNORE INTO mytest (id) VALUES (1), (2)")
        cursor.execute("SELECT * FROM mytest")
        results = cursor.fetchall()
        cursor.close()
        return {"message": "Hello, World!", "data": results}
    except Exception as e:
        return {"error": str(e)}

@app.get("/{student_id}")
def read_item(student_id: int, q: str = None):
    return {"student_id": student_id, "q": q}

