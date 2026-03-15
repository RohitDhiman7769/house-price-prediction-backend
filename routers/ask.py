from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    age: int

@router.post("/ask")
async def predict(features: HouseFeatures, request: Request):
    
    model = request.app.state.model
    prediction = model.predict([[features.area, features.bedrooms, features.bathrooms, features.age]])
    return {"predicted_price": round(prediction[0], 2)}
