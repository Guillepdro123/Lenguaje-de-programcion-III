from fastapi import FastAPI, Depends, status
from fastapi.responses import RedirectResponse
from typing import List
from app.schemas.estudiante_schema import (
    EstudianteCreate, EstudianteUpdate, EstudianteOut, 
    EstudianteResponse, EstudianteListResponse, EstudianteDeleteResponse
)
from app.services.estudiante_service import EstudianteService
from app.dependencies.dependencies import get_estudiante_service

app = FastAPI(title="API Estudiantes")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/estudiantes", response_model=EstudianteListResponse)
def get_estudiantes(service: EstudianteService = Depends(get_estudiante_service)):
    estudiantes = service.get_all()
    return {"mensaje": "Listado de estudiantes", "cantidad": len(estudiantes), "estudiantes": estudiantes}

@app.get("/estudiantes/{id}", response_model=EstudianteResponse)
def get_estudiante(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    return {"mensaje": "Estudiante encontrado", "estudiante": service.get_by_id(id)}

@app.post("/estudiantes", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED)
def create_estudiante(estudiante: EstudianteCreate, service: EstudianteService = Depends(get_estudiante_service)):
    return {"mensaje": "Estudiante registrado exitosamente", "estudiante": service.create(estudiante)}

@app.put("/estudiantes/{id}", response_model=EstudianteResponse)
def update_estudiante(id: int, estudiante: EstudianteUpdate, service: EstudianteService = Depends(get_estudiante_service)):
    return {"mensaje": "Estudiante actualizado correctamente", "estudiante": service.update(id, estudiante)}

@app.delete("/estudiantes/{id}", response_model=EstudianteDeleteResponse, status_code=status.HTTP_200_OK)
def delete_estudiante(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    service.delete(id)
    return {"mensaje": "Estudiante eliminado exitosamente"}
