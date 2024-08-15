from fastapi import FastAPI, HTTPException
from app.weather import get_weather_data

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/weather/{city}/{date}")
async def get_weather(city: str, date: str):
    try:
        weather_data = get_weather_data(city, date)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
