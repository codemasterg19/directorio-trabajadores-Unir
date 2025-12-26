from datetime import datetime

class GestorContratos:
    def __init__(self, gestor_empleados):
        self.gestor_empleados = gestor_empleados

    def asociar_contrato(self, id_empleado: int, fecha_inicio: str, fecha_fin: str | None, salario: float) -> dict:
        empleado = self.gestor_empleados.buscar_empleado(id_empleado)
        if not empleado:
            raise ValueError(f"Empleado con ID {id_empleado} no encontrado.")
        
        # Validar fechas
        try:
            f_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            f_fin = datetime.strptime(fecha_fin, "%Y-%m-%d") if fecha_fin else None
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")

        # Si hay fecha fin, validar que no sea anterior a inicio
        if f_fin and f_fin < f_inicio:
            raise ValueError("La fecha de fin no puede ser anterior a la fecha de inicio.")

        if salario <= 0:
            raise ValueError("El salario debe ser mayor que 0.")

        # Generar ID de contrato (globalmente único)
        todos_los_empleados = self.gestor_empleados.obtener_empleados()
        max_id = 100
        for emp in todos_los_empleados:
            for contrato in emp.get("contratos", []):
                if contrato["id_contrato"] > max_id:
                    max_id = contrato["id_contrato"]
        nuevo_id = max_id + 1

        nuevo_contrato = {
            "id_contrato": nuevo_id,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "salario": salario
        }

        empleado["contratos"].append(nuevo_contrato)
        self.gestor_empleados._guardar_datos()
        return nuevo_contrato

    def obtener_contratos(self, id_empleado: int) -> list:
        empleado = self.gestor_empleados.buscar_empleado(id_empleado)
        if not empleado:
            return None
        return empleado.get("contratos", [])

    def listar_contratos_vencidos(self) -> list:
        vencidos = []
        hoy = datetime.now()
        for emp in self.gestor_empleados.obtener_empleados():
            for contrato in emp.get("contratos", []):
                if not contrato.get("fecha_fin"): # Contrato indefinido no vence
                    continue
                try:
                    fecha_fin = datetime.strptime(contrato["fecha_fin"], "%Y-%m-%d")
                    if fecha_fin < hoy:
                        vencidos.append({
                            "empleado": emp["nombre"],
                            "id_empleado": emp["id"],
                            "contrato": contrato
                        })
                except ValueError:
                    continue # Ignorar fechas malformadas
        return vencidos
