# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

# 1. Initialize the FastAPI App
app = FastAPI(
    title="Iris Species Prediction API",
    description="An API to predict the species of an Iris flower based on its measurements.",
    version="1.0.0"
)

# 2. Load the Model
try:
    model = joblib.load('iris_model.joblib')
except FileNotFoundError:
    raise RuntimeError("Model file not found. Please run train.py first.")

# 3. Define Request and Response Models
class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisResponse(BaseModel):
    prediction: int
    species_name: str

# 4. Define the Prediction Endpoint
@app.post("/predict", response_model=IrisResponse)
def predict_species(request: IrisRequest):
    """
    Receives Iris measurements and predicts the species.
    """
    try:
        # Convert the request data to a NumPy array for the model
        input_data = np.array([[
            request.sepal_length,
            request.sepal_width,
            request.petal_length,
            request.petal_width
        ]])

        # Make a prediction
        prediction = model.predict(input_data)
        prediction_int = int(prediction[0])

        # Map the prediction to the species name
        species_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        species_name = species_map.get(prediction_int, "Unknown")

        return IrisResponse(prediction=prediction_int, species_name=species_name)

    except Exception as e:
        # Handle potential errors during prediction
        raise HTTPException(status_code=500, detail=str(e))

# 5. Add a Root Endpoint for Health Check
@app.get("/")
def read_root():
    return {"status": "API is running"}