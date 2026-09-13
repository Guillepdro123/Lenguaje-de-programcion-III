from pydantic import BaseModel, Field
from typing import Optional

class EstudianteBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    programa: str = Field(..., min_length=1)
    semestre: int = Field(..., ge=1)
    promedio: float = Field(..., ge=0.0)

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(EstudianteBase):
    nombre: Optional[str] = None
    programa: Optional[str] = None
    semestre: Optional[int] = None
    promedio: Optional[float] = None

class EstudianteOut(EstudianteBase):
    id: int

    class Config:
        from_attributes = True
