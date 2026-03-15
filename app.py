from fastapi import FastAPI
import joblib
from routers import ask

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "https://house-price-prediction-frontend.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.model = joblib.load("model.pkl")

app.include_router(ask.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
