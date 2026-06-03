from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Barbero(BaseModel):
    id: int
    nombre: str
    especialidad: str

barberos_db = []

@router.get("/barberos", response_model=List[Barbero])
async def get_barberos():
    return barberos_db

@router.post("/barberos", response_model=Barbero)
async def create_barbero(barbero: Barbero):
    if any(b.id == barbero.id for b in barberos_db):
        raise HTTPException(status_code=400, detail="Barbero already exists")
    barberos_db.append(barbero)
    return barbero
