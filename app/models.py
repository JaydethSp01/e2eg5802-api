from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int]
    nombre: str
    telefono: str
    email: str

class Cita(BaseModel):
    id: Optional[int]
    cliente_id: int
    barbero_id: int
    fecha: str

# More models...