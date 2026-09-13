import pytest
from fastapi.testclient import TestClient
from typing import Dict, List, Optional
from app.main import app
from app.dependencies.dependencies import get_estudiante_repository
from app.repositories.base_repository import BaseRepository
from app.models.estudiante import Estudiante

class FakeEstudianteRepository(BaseRepository):
    def __init__(self):
        self._data: Dict[int, Estudiante] = {}
        self._current_id = 1

    def get_all(self) -> List[Estudiante]:
        return list(self._data.values())

    def get_by_id(self, id: int) -> Optional[Estudiante]:
        return self._data.get(id)

    def create(self, estudiante_data: dict) -> Estudiante:
        estudiante = Estudiante(
            id=self._current_id,
            nombre=estudiante_data.get("nombre", ""),
            programa=estudiante_data.get("programa", ""),
            semestre=estudiante_data.get("semestre", 1),
            promedio=estudiante_data.get("promedio", 0.0)
        )
        self._data[self._current_id] = estudiante
        self._current_id += 1
        return estudiante

    def update(self, id: int, estudiante_data: dict) -> Optional[Estudiante]:
        estudiante = self.get_by_id(id)
        if estudiante:
            for key, value in estudiante_data.items():
                if value is not None and hasattr(estudiante, key):
                    setattr(estudiante, key, value)
            return estudiante
        return None

    def delete(self, id: int) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False

@pytest.fixture
def fake_repo():
    return FakeEstudianteRepository()

@pytest.fixture
def client(fake_repo):
    app.dependency_overrides[get_estudiante_repository] = lambda: fake_repo
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
