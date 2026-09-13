from fastapi import FastAPI, Depends, status
from fastapi.responses import RedirectResponse
from typing import List
from app.schemas.estudiante_schema import EstudianteCreate, EstudianteUpdate, EstudianteOut
from app.services.estudiante_service import EstudianteService
from app.dependencies.dependencies import get_estudiante_service

app = FastAPI(title="API Estudiantes")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/estudiantes", response_model=List[EstudianteOut])
def get_estudiantes(service: EstudianteService = Depends(get_estudiante_service)):
    return service.get_all()

@app.get("/estudiantes/{id}", response_model=EstudianteOut)
def get_estudiante(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    return service.get_by_id(id)

@app.post("/estudiantes", response_model=EstudianteOut, status_code=status.HTTP_201_CREATED)
def create_estudiante(estudiante: EstudianteCreate, service: EstudianteService = Depends(get_estudiante_service)):
    return service.create(estudiante)

@app.put("/estudiantes/{id}", response_model=EstudianteOut)
def update_estudiante(id: int, estudiante: EstudianteUpdate, service: EstudianteService = Depends(get_estudiante_service)):
    return service.update(id, estudiante)

@app.delete("/estudiantes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_estudiante(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    service.delete(id)
