from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str

clientes_db = []

@router.get("/clientes", response_model=List[Cliente])
async def get_clientes():
    return clientes_db

@router.post("/clientes", response_model=Cliente)
async def create_cliente(cliente: Cliente):
    if any(c.id == cliente.id for c in clientes_db):
        raise HTTPException(status_code=400, detail="Cliente already exists")
    clientes_db.append(cliente)
    return cliente
