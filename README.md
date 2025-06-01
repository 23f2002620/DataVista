# Predictive Maintenance for Satellite Systems

This project leverages machine learning to predict potential failures in satellite systems based on telemetry data. It includes a trained ML model, a FastAPI application for serving predictions, and a testing utility.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Model Details](#model-details)
- [API Usage](#api-usage)
- [Testing](#testing)
- [Setup Instructions](#setup-instructions)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

**Predictive Maintenance for Satellite Systems** is designed to:
- Analyze satellite telemetry data
- Predict imminent failures using a machine learning model
- Expose a REST API (via FastAPI) for real-time inference

---

## Model Details

- The model is trained in a Jupyter notebook (`.ipynb`) and exported as `satellite_pm_model.pkl`.
- It expects 24 input features: 3 operational settings and 21 sensor readings.
- The model outputs:
  - `prediction`: 1 (Fail Soon) or 0 (Healthy)
  - `probability_of_failure`: Probability score for failure
  - `status`: Human-readable health status

---

## API Usage

The FastAPI app (`app.py`) provides a `/predict` endpoint.

### Input Schema

Send a POST request to `/predict` with a JSON payload containing:

```json
{
  "op_setting_1": float,
  "op_setting_2": float,
  "op_setting_3": float,
  "sensor_1": float,
  ...
  "sensor_21": float
}
```

### Example Request

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "op_setting_1": 0.5,
        "op_setting_2": 1.2,
        "op_setting_3": 0.3,
        "sensor_1": 0.01,
        ...
        "sensor_21": 0.85
      }'
```

### Example Response

```json
{
  "prediction": 0,
  "probability_of_failure": 0.08,
  "status": "Healthy"
}
```

---

## Testing

- Automated tests for the API are provided in `test_api.py`.
- Run tests after starting the FastAPI app to verify endpoint correctness.

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/23f2002620/Predictive-Maintenance-for-Satellite-Systems.git
   cd Predictive-Maintenance-for-Satellite-Systems
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API server:**

   ```bash
   uvicorn app:app --reload
   ```

4. **Test the API:**

   ```bash
   python test_api.py
   ```

---

## Requirements

Dependencies (see `requirements.txt`):

---

## Project Structure

```
├── app.py                  # FastAPI app for predictions
├── satellite_pm_model.pkl  # Trained ML model
├── test_api.py             # API tests
├── requirements.txt        # Python dependencies
├── Datavista.ipynb        # Model training notebook
└── README.md               # Project documentation
```

---

## Contributors

- [Yuvasri S](https://github.com/yuvasriselvam0107)
- [Trisha P](https://github.com/23f1000097/)
- [Tiwari Riya](https://github.com/tiwarii-riya)



## License

This project is licensed under the MIT License.

---

> **Note:** For best results, adjust the input fields to match your model's features and update the testing instructions if your test script requires specific arguments or environment setup.
