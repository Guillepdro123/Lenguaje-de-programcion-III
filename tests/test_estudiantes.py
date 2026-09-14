def test_create_estudiante(client):
    response = client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Juan Perez",
        "programa": "Ingenieria de Sistemas",
        "semestre": 5,
        "promedio": 4.5
    })
    assert response.status_code == 201
    data = response.json()
    assert data["mensaje"] == "Estudiante registrado exitosamente"
    assert data["estudiante"]["id"] == 1
    assert data["estudiante"]["nombre"] == "Juan Perez"

def test_create_estudiante_id_duplicado(client):
    # Primer registro exitoso
    client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Maria",
        "programa": "Biologia",
        "semestre": 1,
        "promedio": 5.0
    })
    
    # Intento de registrar otro estudiante con el mismo ID
    response = client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Pedro",
        "programa": "Biologia",
        "semestre": 2,
        "promedio": 4.0
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "El ID del estudiante ya está en uso"

def test_get_estudiante_existente(client):
    client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Ana Gomez",
        "programa": "Medicina",
        "semestre": 3,
        "promedio": 4.8
    })
    response = client.get("/estudiantes/1")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Estudiante encontrado"
    assert response.json()["estudiante"]["nombre"] == "Ana Gomez"

def test_estudiante_no_existe_404(client):
    response = client.get("/estudiantes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Estudiante no encontrado"
    
    response = client.put("/estudiantes/999", json={"nombre": "Nuevo"})
    assert response.status_code == 404

def test_update_estudiante_exitoso(client):
    client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Carlos",
        "programa": "Derecho",
        "semestre": 2,
        "promedio": 3.9
    })
    response = client.put("/estudiantes/1", json={"promedio": 4.1})
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Estudiante actualizado correctamente"
    assert response.json()["estudiante"]["promedio"] == 4.1
    assert response.json()["estudiante"]["nombre"] == "Carlos"

def test_delete_estudiante_exitoso(client):
    client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Luis",
        "programa": "Arquitectura",
        "semestre": 8,
        "promedio": 4.0
    })
    response = client.delete("/estudiantes/1")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Estudiante eliminado exitosamente"
    
    response = client.get("/estudiantes/1")
    assert response.status_code == 404

def test_datos_invalidos_422(client):
    response = client.post("/estudiantes", json={
        "id": 1,
        "nombre": "Pedro",
        "semestre": "no es un numero",
        "promedio": 4.0
    })
    assert response.status_code == 422
