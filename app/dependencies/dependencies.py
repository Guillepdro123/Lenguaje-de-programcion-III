from fastapi import Depends
from app.repositories.estudiante_repository import EstudianteRepository
from app.services.estudiante_service import EstudianteService

_estudiante_repository = EstudianteRepository()

def get_estudiante_repository() -> EstudianteRepository:
    return _estudiante_repository

def get_estudiante_service(repository: EstudianteRepository = Depends(get_estudiante_repository)) -> EstudianteService:
    return EstudianteService(repository)
