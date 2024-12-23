import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # Замените на URL вашего API

def test_get_posts():
    """Тест GET-запроса для получения списка постов."""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    
def test_get_single_post():
    """Тест GET-запроса для получения одного поста по ID."""
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["id"] == post_id

def test_create_post():
    """Тест POST-запроса для создания нового поста."""
    new_post = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == new_post["title"]

def test_update_post():
    """Тест PUT-запроса для обновления существующего поста."""
    post_id = 1
    updated_post = {
        "id": post_id,
        "title": "Updated Post",
        "body": "This is an updated post.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == updated_post["title"]

def test_delete_post():
    """Тест DELETE-запроса для удаления поста."""
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200