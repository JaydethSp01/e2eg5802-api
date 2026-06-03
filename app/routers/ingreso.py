from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Ingreso(BaseModel):
    id: int
    monto: float
    fecha: str

ingresos_db = []

@router.get("/ingresos", response_model=List[Ingreso])
async def get_ingresos():
    return ingresos_db

@router.post("/ingresos", response_model=Ingreso)
async def create_ingreso(ingreso: Ingreso):
    if any(i.id == ingreso.id for i in ingresos_db):
        raise HTTPException(status_code=400, detail="Ingreso already exists")
    ingresos_db.append(ingreso)
    return ingreso
