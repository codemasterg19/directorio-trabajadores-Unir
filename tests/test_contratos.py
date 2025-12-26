import pytest
from datetime import datetime, timedelta
from gestor_empleados import GestorEmpleados
from gestor_contratos import GestorContratos

@pytest.fixture
def gestor_con(tmp_path):
    db_file = tmp_path / "test_contratos.json"
    g_emp = GestorEmpleados(str(db_file))
    g_emp.agregar_empleado("Test Contract", "Worker")
    return GestorContratos(g_emp), g_emp

def test_asociar_contrato_valido(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    contrato = g_con.asociar_contrato(emp["id"], "2023-01-01", "2023-12-31", 1000)
    assert contrato["salario"] == 1000
    assert len(emp["contratos"]) == 1

def test_asociar_contrato_indefinido(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    contrato = g_con.asociar_contrato(emp["id"], "2023-01-01", None, 1200)
    assert contrato["salario"] == 1200
    assert contrato["fecha_fin"] is None
    assert len(emp["contratos"]) == 1

def test_asociar_contrato_fechas_invalidas(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    with pytest.raises(ValueError, match="La fecha de fin no puede ser anterior"):
        g_con.asociar_contrato(emp["id"], "2023-12-31", "2023-01-01", 1000)

def test_asociar_contrato_salario_invalido(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    with pytest.raises(ValueError, match="El salario debe ser mayor que 0"):
        g_con.asociar_contrato(emp["id"], "2023-01-01", "2023-12-31", -10)

def test_listar_contratos_vencidos(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    # Contrato vencido (fecha fin ayer)
    ayer = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    hace_un_mes = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    
    g_con.asociar_contrato(emp["id"], hace_un_mes, ayer, 1000)
    
    vencidos = g_con.listar_contratos_vencidos()
    assert len(vencidos) == 1
    assert vencidos[0]["id_empleado"] == emp["id"]

def test_listar_contratos_activos_no_vencidos(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    # Contrato futuro
    futuro = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    g_con.asociar_contrato(emp["id"], "2023-01-01", futuro, 1000)
    
    vencidos = g_con.listar_contratos_vencidos()
    assert len(vencidos) == 0

def test_listar_contratos_indefinidos_no_vencidos(gestor_con):
    g_con, g_emp = gestor_con
    emp = g_emp.obtener_empleados()[0]
    
    # Contrato indefinido
    g_con.asociar_contrato(emp["id"], "2023-01-01", None, 1500)
    
    vencidos = g_con.listar_contratos_vencidos()
    assert len(vencidos) == 0
