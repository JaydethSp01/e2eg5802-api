from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Cita(BaseModel):
    id: int
    clienteId: int
    barberoId: int
    hora: str

citas_db = []

@router.get("/citas", response_model=List[Cita])
async def get_citas():
    return citas_db

@router.post("/citas", response_model=Cita)
async def create_cita(cita: Cita):
    if any(c.id == cita.id for c in citas_db):
        raise HTTPException(status_code=400, detail="Cita already exists")
    citas_db.append(cita)
    return cita
