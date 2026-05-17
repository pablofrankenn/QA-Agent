import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": os.getenv("REQRES_API_KEY")}

def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=1", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1
    assert len(data["data"]) > 0

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 1
    assert "email" in data["data"]
    assert "first_name" in data["data"]

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "Pablo", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Pablo"
    assert data["job"] == "QA Engineer"
    assert "id" in data

def test_update_user():
    payload = {"name": "Pablo Updated", "job": "Senior QA Engineer"}
    response = requests.put(f"{BASE_URL}/users/1", json=payload, headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pablo Updated"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/1", headers=HEADERS)
    assert response.status_code == 204

def test_successful_login():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()

def test_failed_login():
    payload = {"email": "wrong@email.com", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 400