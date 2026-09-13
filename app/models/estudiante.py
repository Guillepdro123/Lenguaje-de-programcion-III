from dataclasses import dataclass

@dataclass
class Estudiante:
    id: int
    nombre: str
    programa: str
    semestre: int
    promedio: float
