import pytest
from flask import Flask
from app import app, get_data_meteo, get_user_location


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_data_meteo(monkeypatch):
    # Mock da resposta da API
    class MockResponse:
        @staticmethod
        def json():
            return {
                "hourly": {
                    "time": ["2023-10-01T00:00", "2023-10-01T01:00"],
                    "temperature_2m": [20, 21],
                    "precipitation": [0, 0],
                    "relativehumidity_2m": [50, 55],
                    "windspeed_10m": [5, 10]
                }
            }

        status_code = 200

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    data = get_data_meteo(40.7128, -74.0060)
    assert data is not None
    assert data['hourly']['temperature_2m'] == [20, 21]
    assert data['hourly']['precipitation'] == [0, 0]


def test_get_user_location(monkeypatch):
    # Mock da resposta da API
    class MockResponse:
        @staticmethod
        def json():
            return {
                "city": "Ashburn",
                "country": "US"
            }

        status_code = 200

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    city, country = get_user_location()
    assert city == "Ashburn"
    assert country == "US"


def test_index(client, monkeypatch):
    # Mock da função get_user_location
    monkeypatch.setattr("app.get_user_location", lambda: ("Nueva York", "US"))

    # Mock da função get_data_meteo
    class MockResponse:
        @staticmethod
        def json():
            return {
                "hourly": {
                    "time": ["2023-10-01T00:00", "2023-10-01T01:00"],
                    "temperature_2m": [20, 21],
                    "precipitation": [0, 0],
                    "relativehumidity_2m": [50, 55],
                    "windspeed_10m": [5, 10]
                }
            }

        status_code = 200

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    # Testa a rota principal
    # Seleciona a cidade de índice 0
    response = client.post('/', data={'city': '0'})
    assert response.status_code == 200
    assert b"Nueva York" in response.data  # Verifica se a cidade está na resposta
    # Verifica se o gráfico de temperatura está presente
    assert b"Temperatures (°C)" in response.data
