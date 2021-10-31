from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CityInfo(BaseModel):
    """
    城市信息
    """
    province: str
    country: str
    is_affected: Optional[bool] = None


@app.get("/")
def hello():
    return {"hello": "world"}


@app.get('/city/{city}')
def result(city: str, q: Optional[str] = None):
    return {'city': city, 'q': q}
