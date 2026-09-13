# API REST de Gestión de Estudiantes - FastAPI

**Autor:** Guillermo Luis Sandoval Ricardo  
**Programa:** Ingeniería de Sistemas  
**Institución:** Corporación Universitaria Remington  

Esta es una API REST moderna y robusta construida con Python, diseñada para la gestión de estudiantes. El proyecto está diseñado siguiendo estrictamente principios de Arquitectura Limpia, separación de responsabilidades (Routes, Services, Repositories) y el patrón de Inyección de Dependencias, lo que garantiza un código altamente modular, testeable y mantenible.

---

## Tecnologías Utilizadas

- **Python 3+**
- **FastAPI:** Framework web moderno y de alto rendimiento para construir APIs.
- **Uvicorn:** Servidor ASGI para la ejecución rápida de FastAPI.
- **Pydantic:** Validación de datos y gestión de configuraciones a través de esquemas.
- **Pytest:** Framework para pruebas unitarias.
- **Httpx:** Cliente HTTP asíncrono, utilizado internamente por TestClient.

---

## Arquitectura del Proyecto

El proyecto se divide en las siguientes capas lógicas:

- **Configuración y Rutas (`main.py`):** Contiene la instancia de la aplicación FastAPI y expone los endpoints. No contiene lógica de negocio.
- **Modelos y Esquemas:** Definen las entidades del sistema y los contratos (schemas Pydantic) de entrada/salida para la validación automática de datos.
- **Capa de Servicios (`services/`):** Encapsula toda la lógica de negocio y las reglas del sistema (ej. validar si un estudiante existe).
- **Capa de Repositorios (`repositories/`):** Gestiona el acceso a los datos. En este proyecto, utiliza una persistencia en memoria (diccionario) para simular el almacenamiento.

**Inyección de Dependencias (Dependency Injection):**
El servicio no instancia el repositorio de datos de manera directa. A través del sistema de `Depends` de FastAPI, la instancia del repositorio se inyecta en el servicio, y este último se inyecta en los endpoints. Esto permite desacoplar la lógica de negocio de la infraestructura y facilita enormemente el reemplazo de componentes durante las pruebas unitarias.

---

## Instrucciones de Instalación y Configuración

Sigue estos pasos para levantar el proyecto en tu entorno local:

1. **Clonar el repositorio** (Si aplica):
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd API_ESTUDIANTES
   ```

2. **Crear el entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual (Windows):**
   ```bash
   venv\Scripts\activate
   ```

4. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución del Servidor

Una vez instalado, puedes levantar el servidor de desarrollo utilizando Uvicorn. Ejecuta el siguiente comando en la raíz del proyecto:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en tu máquina local. Para probar la API de forma interactiva sin necesidad de herramientas externas como Postman, abre tu navegador en la siguiente URL (Swagger UI):

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## Endpoints Disponibles

La API expone las siguientes operaciones (CRUD):

| Método HTTP | Endpoint | Descripción |
| :---: | :--- | :--- |
| **GET** | `/estudiantes` | Obtener la lista de todos los estudiantes registrados |
| **GET** | `/estudiantes/{id}` | Buscar los detalles de un estudiante en específico por su ID |
| **POST** | `/estudiantes` | Crear y registrar un nuevo estudiante en el sistema |
| **PUT** | `/estudiantes/{id}` | Actualizar los datos (nombre, semestre, etc.) de un estudiante existente |
| **DELETE** | `/estudiantes/{id}` | Eliminar de forma definitiva a un estudiante del sistema |

---

## Pruebas Unitarias

El proyecto cuenta con una cobertura completa de pruebas unitarias sobre los casos de uso principales. 

Durante las pruebas, se aprovecha la Inyección de Dependencias para sobreescribir temporalmente la base de datos real con un `FakeRepository`. Esto permite simular escenarios (éxito, registro no existente, datos inválidos) de manera rápida y sin ensuciar la base de datos de producción.

Para ejecutar la batería de pruebas, utiliza el siguiente comando:

```bash
pytest
```
*(También se puede utilizar `python -m pytest tests/ -v` si surgen problemas con la ruta del comando).*

