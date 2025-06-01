from fastapi.testclient import TestClient
from app import app  # Make sure 'app' is your FastAPI instance

client = TestClient(app)

def test_predict():
    payload = {
        "op_setting_1": 0.5,
        "op_setting_2": 0.1,
        "op_setting_3": 100.0,
        "sensor_1": 518.67,
        "sensor_2": 641.82,
        "sensor_3": 1589.7,
        "sensor_4": 1400.6,
        "sensor_5": 14.62,
        "sensor_6": 21.61,
        "sensor_7": 554.37,
        "sensor_8": 2388.06,
        "sensor_9": 9046.19,
        "sensor_10": 1.3,
        "sensor_11": 47.47,
        "sensor_12": 521.66,
        "sensor_13": 2388.06,
        "sensor_14": 8138.7,
        "sensor_15": 8.4195,
        "sensor_16": 0.03,
        "sensor_17": 392.0,
        "sensor_18": 2388.06,
        "sensor_19": 100.0,
        "sensor_20": 39.06,
        "sensor_21": 23.419
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
