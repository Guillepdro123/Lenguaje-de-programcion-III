def test_create_estudiante(client):
    response = client.post("/estudiantes", json={
        "nombre": "Juan Perez",
        "programa": "Ingenieria de Sistemas",
        "semestre": 5,
        "promedio": 4.5
    })
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["nombre"] == "Juan Perez"

def test_get_estudiante_existente(client):
    client.post("/estudiantes", json={
        "nombre": "Ana Gomez",
        "programa": "Medicina",
        "semestre": 3,
        "promedio": 4.8
    })
    response = client.get("/estudiantes/1")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Ana Gomez"

def test_estudiante_no_existe_404(client):
    response = client.get("/estudiantes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Estudiante no encontrado"
    
    response = client.put("/estudiantes/999", json={"nombre": "Nuevo"})
    assert response.status_code == 404

def test_update_estudiante_exitoso(client):
    client.post("/estudiantes", json={
        "nombre": "Carlos",
        "programa": "Derecho",
        "semestre": 2,
        "promedio": 3.9
    })
    response = client.put("/estudiantes/1", json={"promedio": 4.1})
    assert response.status_code == 200
    assert response.json()["promedio"] == 4.1
    assert response.json()["nombre"] == "Carlos"

def test_delete_estudiante_exitoso(client):
    client.post("/estudiantes", json={
        "nombre": "Luis",
        "programa": "Arquitectura",
        "semestre": 8,
        "promedio": 4.0
    })
    response = client.delete("/estudiantes/1")
    assert response.status_code == 204
    
    response = client.get("/estudiantes/1")
    assert response.status_code == 404

def test_datos_invalidos_422(client):
    response = client.post("/estudiantes", json={
        "nombre": "Pedro",
        "semestre": "no es un numero",
        "promedio": 4.0
    })
    assert response.status_code == 422
