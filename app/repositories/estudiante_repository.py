from typing import List, Optional, Dict
from app.repositories.base_repository import BaseRepository
from app.models.estudiante import Estudiante

class EstudianteRepository(BaseRepository):
    def __init__(self):
        self._data: Dict[int, Estudiante] = {}

    def get_all(self) -> List[Estudiante]:
        return list(self._data.values())

    def get_by_id(self, id: int) -> Optional[Estudiante]:
        return self._data.get(id)

    def create(self, estudiante_data: dict) -> Estudiante:
        estudiante = Estudiante(
            id=estudiante_data["id"],
            nombre=estudiante_data["nombre"],
            programa=estudiante_data["programa"],
            semestre=estudiante_data["semestre"],
            promedio=estudiante_data["promedio"]
        )
        self._data[estudiante.id] = estudiante
        return estudiante

    def update(self, id: int, estudiante_data: dict) -> Optional[Estudiante]:
        estudiante = self.get_by_id(id)
        if estudiante:
            if "nombre" in estudiante_data and estudiante_data["nombre"] is not None:
                estudiante.nombre = estudiante_data["nombre"]
            if "programa" in estudiante_data and estudiante_data["programa"] is not None:
                estudiante.programa = estudiante_data["programa"]
            if "semestre" in estudiante_data and estudiante_data["semestre"] is not None:
                estudiante.semestre = estudiante_data["semestre"]
            if "promedio" in estudiante_data and estudiante_data["promedio"] is not None:
                estudiante.promedio = estudiante_data["promedio"]
            return estudiante
        return None

    def delete(self, id: int) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False
