import joblib
import numpy as np

def load_model(path="models/rf_model.pkl"):
    return joblib.load(path)

def predict(model, scaler, sample):
    sample_scaled = scaler.transform([sample])
    prediction = model.predict(sample_scaled)
    return prediction