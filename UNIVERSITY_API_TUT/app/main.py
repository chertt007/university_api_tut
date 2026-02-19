from fastapi import FastAPI, HTTPException

from app.db import get_db_connection
from app.models.student import StudentCreate



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
async def status():
    return{"message": "OK"}

@app.post("/student/")
def create_student(student: StudentCreate):
    conn, cursor = get_db_connection()
    try:
        cursor.execute(
            "INSERT INTO students (first_name, last_name) VALUES (%s, %s) RETURNING id",
            (student.first_name, student.last_name),
        )
        new_student = cursor.fetchone()
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    conn.close()
    
    if new_student:
        return {"id": new_student["id"]}
    
    raise HTTPException(status_code=400, detail="Error creating student")
