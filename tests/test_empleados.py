import pytest
import os
import json
from gestor_empleados import GestorEmpleados

@pytest.fixture
def gestor(tmp_path):
    db_file = tmp_path / "test_empleados.json"
    return GestorEmpleados(str(db_file))

def test_agregar_empleado(gestor):
    emp = gestor.agregar_empleado("Juan Perez", "Dev")
    assert emp["id"] == 1
    assert emp["nombre"] == "Juan Perez"
    assert emp["cargo"] == "Dev"
    assert len(gestor.obtener_empleados()) == 1

def test_buscar_empleado(gestor):
    emp = gestor.agregar_empleado("Ana Lopez", "Manager")
    encontrado = gestor.buscar_empleado(emp["id"])
    assert encontrado is not None
    assert encontrado["nombre"] == "Ana Lopez"

def test_eliminar_empleado(gestor):
    emp = gestor.agregar_empleado("Luis", "QA")
    assert gestor.eliminar_empleado(emp["id"]) is True
    assert gestor.buscar_empleado(emp["id"]) is None

def test_actualizar_empleado(gestor):
    emp = gestor.agregar_empleado("Maria", "UX")
    assert gestor.actualizar_empleado(emp["id"], nombre="Maria Updated") is True
    actualizado = gestor.buscar_empleado(emp["id"])
    assert actualizado["nombre"] == "Maria Updated"
    assert actualizado["cargo"] == "UX"

def test_persistencia(tmp_path):
    db_file = tmp_path / "test_persist.json"
    g1 = GestorEmpleados(str(db_file))
    g1.agregar_empleado("Persist", "Test")
    
    g2 = GestorEmpleados(str(db_file))
    empleados = g2.obtener_empleados()
    assert len(empleados) == 1
    assert empleados[0]["nombre"] == "Persist"
