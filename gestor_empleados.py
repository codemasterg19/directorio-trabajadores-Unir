import json
import os

class GestorEmpleados:
    def __init__(self, archivo_db="empleados.json"):
        self.archivo_db = archivo_db
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo_db):
            return {"empleados": []}
        try:
            with open(self.archivo_db, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"empleados": []}

    def _guardar_datos(self):
        try:
            with open(self.archivo_db, "w", encoding="utf-8") as f:
                json.dump(self.datos, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False

    def agregar_empleado(self, nombre: str, cargo: str) -> dict:
        empleados = self.datos["empleados"]
        nuevo_id = 1
        if empleados:
            nuevo_id = max(emp["id"] for emp in empleados) + 1
        
        nuevo_empleado = {
            "id": nuevo_id,
            "nombre": nombre,
            "cargo": cargo,
            "contratos": []
        }
        empleados.append(nuevo_empleado)
        self._guardar_datos()
        return nuevo_empleado

    def buscar_empleado(self, id_empleado: int) -> dict:
        for emp in self.datos["empleados"]:
            if emp["id"] == id_empleado:
                return emp
        return None

    def actualizar_empleado(self, id_empleado: int, nombre: str = None, cargo: str = None) -> bool:
        empleado = self.buscar_empleado(id_empleado)
        if empleado:
            if nombre:
                empleado["nombre"] = nombre
            if cargo:
                empleado["cargo"] = cargo
            self._guardar_datos()
            return True
        return False

    def eliminar_empleado(self, id_empleado: int) -> bool:
        empleado = self.buscar_empleado(id_empleado)
        if empleado:
            self.datos["empleados"].remove(empleado)
            self._guardar_datos()
            return True
        return False

    def obtener_empleados(self) -> list:
        return self.datos["empleados"]
