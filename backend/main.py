from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# Allow requests from the React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React runs here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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