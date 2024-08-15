from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_weather():
    response = client.get("/weather/London/2024-08-14")
    assert response.status_code == 200
    data = response.json()

    assert data['city'] == 'London'
    assert data['date'] == '2024-08-14'
    assert 'min_temp' in data
    assert 'max_temp' in data
    assert 'avg_temp' in data
    assert 'avg_humidity' in data
