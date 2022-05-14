from fastapi.testclient import TestClient


from blog import app

client = TestClient(app)


def test_read_main():
    response = client.get("/blog/unpublished")
    assert response.status_code == 200
    assert response.json() == {'message': 'unpublished blogs'}