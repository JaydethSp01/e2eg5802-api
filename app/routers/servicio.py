from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Servicio(BaseModel):
    id: int
    nombre: str
    precio: float

servicios_db = []

@router.get("/servicios", response_model=List[Servicio])
async def get_servicios():
    return servicios_db

@router.post("/servicios", response_model=Servicio)
async def create_servicio(servicio: Servicio):
    if any(s.id == servicio.id for s in servicios_db):
        raise HTTPException(status_code=400, detail="Servicio already exists")
    servicios_db.append(servicio)
    return servicio
