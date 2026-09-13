from typing import List
from fastapi import HTTPException
from app.repositories.base_repository import BaseRepository
from app.schemas.estudiante_schema import EstudianteCreate, EstudianteUpdate, EstudianteOut
from app.models.estudiante import Estudiante

class EstudianteService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_all(self) -> List[EstudianteOut]:
        estudiantes = self.repository.get_all()
        return [EstudianteOut(id=e.id, nombre=e.nombre, programa=e.programa, semestre=e.semestre, promedio=e.promedio) for e in estudiantes]

    def get_by_id(self, id: int) -> EstudianteOut:
        estudiante = self.repository.get_by_id(id)
        if not estudiante:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return EstudianteOut(id=estudiante.id, nombre=estudiante.nombre, programa=estudiante.programa, semestre=estudiante.semestre, promedio=estudiante.promedio)

    def create(self, estudiante_create: EstudianteCreate) -> EstudianteOut:
        if self.repository.get_by_id(estudiante_create.id):
            raise HTTPException(status_code=400, detail="El ID del estudiante ya está en uso")
        
        estudiante = self.repository.create(estudiante_create.model_dump())
        return EstudianteOut(id=estudiante.id, nombre=estudiante.nombre, programa=estudiante.programa, semestre=estudiante.semestre, promedio=estudiante.promedio)

    def update(self, id: int, estudiante_update: EstudianteUpdate) -> EstudianteOut:
        estudiante = self.repository.update(id, estudiante_update.model_dump(exclude_unset=True))
        if not estudiante:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return EstudianteOut(id=estudiante.id, nombre=estudiante.nombre, programa=estudiante.programa, semestre=estudiante.semestre, promedio=estudiante.promedio)

    def delete(self, id: int):
        if not self.repository.delete(id):
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
