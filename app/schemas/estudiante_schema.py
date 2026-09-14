from pydantic import BaseModel, Field
from typing import Optional

class EstudianteBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    programa: str = Field(..., min_length=1)
    semestre: int = Field(..., ge=1)
    promedio: float = Field(..., ge=0.0)

class EstudianteCreate(EstudianteBase):
    id: int = Field(..., ge=1)

class EstudianteUpdate(EstudianteBase):
    nombre: Optional[str] = None
    programa: Optional[str] = None
    semestre: Optional[int] = None
    promedio: Optional[float] = None

class EstudianteOut(EstudianteBase):
    id: int

    class Config:
        from_attributes = True

class EstudianteResponse(BaseModel):
    mensaje: str
    estudiante: EstudianteOut

class EstudianteListResponse(BaseModel):
    mensaje: str
    cantidad: int
    estudiantes: list[EstudianteOut]

class EstudianteDeleteResponse(BaseModel):
    mensaje: str
