from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/{student_id}")
def read_item(student_id: int, q: str = None):
    return {"student_id": student_id, "q": q}