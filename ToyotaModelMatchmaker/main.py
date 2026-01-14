import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from catboost import CatBoostClassifier

# 1. Initialize FastAPI
app = FastAPI(title="Toyota Model Matchmaker API")

# 2. Load your trained artifacts
# Ensure these files are in the same folder as main.py
try:
    model = joblib.load("toyota_model.pkl")
    le = joblib.load("label_encoder.pkl")
except Exception as e:
    print(f"Error loading model files: {e}")

# 3. Define the Input Schema (Matches the UI fields)
class ToyotaInput(BaseModel):
    age: int
    gender: str
    income: float
    family_size: int
    daily_commute_miles: float
    loyalty_score: int
    occupation: str
    fuel_preference: str
    area: str  # This will be mapped to 'urban_rural'

@app.get("/")
def home():
    return {"message": "Toyota API is online. Go to /docs for testing."}

@app.post("/predict")
def do_prediction(data: ToyotaInput):
    try:
        # A. Convert input to dict
        d = data.model_dump()
        
        # B. Re-create the 14 features in the EXACT order from your Notebook
        # Note: We fill 'price_vs_msrp' and 'income_to_zip_ratio' with defaults (1.0) 
        # because the UI doesn't collect them, but the model requires them.
        processed_data = {
            # --- Categorical Features ---
            'gender': str(d['gender']),
            'occupation': str(d['occupation']),
            'fuel_preference': str(d['fuel_preference']),
            'urban_rural': str(d['area']),
            
            # --- Numerical Features ---
            'age': float(d['age']),
            'income': float(d['income']),
            'family_size': int(d['family_size']),
            'weekly_commute_miles': float(d['daily_commute_miles'] * 5),
            'price_vs_msrp': 1.0, 
            'income_to_zip_ratio': 1.0,
            
            # --- Engineered Features ---
            'affordability_index': float(d['income'] / 35000),
            'daily_usage_score': float(d['daily_commute_miles'] / 10),
            'suv_affinity_score': float(d['family_size'] * 0.8),
            'sedan_affinity_score': 1.0 if d['family_size'] <= 2 else 0.5
        }

        # C. Create DataFrame and enforce strict Column Order
        df = pd.DataFrame([processed_data])
        
        column_order = [
            'gender', 'occupation', 'fuel_preference', 'urban_rural',
            'age', 'income', 'family_size', 'weekly_commute_miles', 
            'price_vs_msrp', 'income_to_zip_ratio', 
            'affordability_index', 'daily_usage_score', 
            'suv_affinity_score', 'sedan_affinity_score'
        ]
        df = df[column_order]

        # D. Get Probabilities for Top 3
        probs = model.predict_proba(df)[0]
        
        # E. Map probabilities to class names
        all_predictions = []
        for i, prob in enumerate(probs):
            all_predictions.append({
                "vehicle": str(le.classes_[i]),
                "confidence": round(float(prob), 4)
            })
        
        # F. Sort and take Top 3
        top_3 = sorted(all_predictions, key=lambda x: x['confidence'], reverse=True)[:3]
        
        # G. Return the result (This prevents the 'null' response)
        return {"top_recommendations": top_3}

    except Exception as e:
        # This will show the actual error in the response if it crashes
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)