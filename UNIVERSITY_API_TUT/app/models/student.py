from pydantic import BaseModel

class StudentCreate(BaseModel):
    
    first_name: str
    last_name: str
    
class Student(StudentCreate):
    id: int
    