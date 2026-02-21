from typing import List

import pytest
from fastapi.testclient import TestClient 
from random import random
from app.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
        
def test_when_app_running_status_endpoint_should_return_OK(client):
    response  = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
    
def test_when_given_user_name_should_create_a_student_in_db(client):
    first_name = f"John {random}"
    last_name = f"World {random}"
    
    create_response = client.post("/student/", json={"first_name": first_name, "last_name": last_name})
    assert create_response.status_code == 200
    student_id = create_response.json()['id']
    assert student_id != None

def test_get_all_students_should_return_a_list_of_students(client):
    response = client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, List)

def test_delete_student_should_remove_student_from_db(client):
    # First, create a student to ensure there is one to delete
    first_name = f"Jane {random}"
    last_name = f"Doe {random}"
    
    create_response = client.post("/student/", json={"first_name": first_name, "last_name": last_name})
    assert create_response.status_code == 200
    student_id = create_response.json()['id']
    
    # Now, delete the student
    delete_response = client.delete(f"/student/{student_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Student deleted successfully"}