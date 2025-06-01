from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your trained model
model = joblib.load("satellite_pm_model.pkl")

# Define the expected input schema
class TelemetryInput(BaseModel):
    op_setting_1: float
    op_setting_2: float
    op_setting_3: float
    sensor_1: float
    sensor_2: float
    sensor_3: float
    sensor_4: float
    sensor_5: float
    sensor_6: float
    sensor_7: float
    sensor_8: float
    sensor_9: float
    sensor_10: float
    sensor_11: float
    sensor_12: float
    sensor_13: float
    sensor_14: float
    sensor_15: float
    sensor_16: float
    sensor_17: float
    sensor_18: float
    sensor_19: float
    sensor_20: float
    sensor_21: float

app = FastAPI()

@app.post("/predict")
def predict_failure(data: TelemetryInput):
    input_data = np.array([[getattr(data, field) for field in data.model_fields]])
    pred = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]
    return {
        "prediction": int(pred),
        "probability_of_failure": float(proba),
        "status": "Fail Soon" if pred == 1 else "Healthy"
    }
