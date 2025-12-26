from gestor_empleados import GestorEmpleados
from gestor_contratos import GestorContratos
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_input_numerico(mensaje, min_val, max_val):
    while True:
        try:
            val = int(input(mensaje))
            if min_val <= val <= max_val:
                return val
            print(f"Por favor ingrese un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

def menu_principal():
    print("\n--- Directorio de Empleados ---")
    print("1. Agregar empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Buscar empleado por ID")
    print("5. Listar empleados")
    print("6. Asociar contrato a empleado")
    print("7. Ver contratos de un empleado")
    print("8. Reporte: Contratos vencidos")
    print("9. Salir")

def main():
    gestor_emp = GestorEmpleados()
    gestor_con = GestorContratos(gestor_emp)

    while True:
        menu_principal()
        opcion = validar_input_numerico("Seleccione una opción: ", 1, 9)

        if opcion == 1:
            nombre = input("Nombre del empleado: ").strip()
            cargo = input("Cargo del empleado: ").strip()
            if nombre and cargo:
                emp = gestor_emp.agregar_empleado(nombre, cargo)
                print(f"Empleado agregado con ID: {emp['id']}")
            else:
                print("Nombre y cargo son obligatorios.")

        elif opcion == 2:
            try:
                id_emp = int(input("ID del empleado a actualizar: "))
                nombre = input("Nuevo nombre (Enter para omitir): ").strip()
                cargo = input("Nuevo cargo (Enter para omitir): ").strip()
                if gestor_emp.actualizar_empleado(id_emp, nombre or None, cargo or None):
                    print("Empleado actualizado correctamente.")
                else:
                    print("Empleado no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == 3:
            try:
                id_emp = int(input("ID del empleado a eliminar: "))
                if gestor_emp.eliminar_empleado(id_emp):
                    print("Empleado eliminado.")
                else:
                    print("Empleado no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == 4:
            try:
                id_emp = int(input("ID del empleado: "))
                emp = gestor_emp.buscar_empleado(id_emp)
                if emp:
                    print(f"ID: {emp['id']}, Nombre: {emp['nombre']}, Cargo: {emp['cargo']}")
                else:
                    print("Empleado no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == 5:
            empleados = gestor_emp.obtener_empleados()
            if not empleados:
                print("No hay empleados registrados.")
            else:
                for emp in empleados:
                    print(f"ID: {emp['id']}, Nombre: {emp['nombre']}, Cargo: {emp['cargo']}")

        elif opcion == 6:
            try:
                id_emp = int(input("ID del empleado: "))
                f_inicio = input("Fecha Inicio (YYYY-MM-DD): ")
                f_fin = input("Fecha Fin (YYYY-MM-DD, Enter para indefinido): ").strip()
                salario = float(input("Salario: "))
                gestor_con.asociar_contrato(id_emp, f_inicio, f_fin, salario)
                print("Contrato asociado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == 7:
            try:
                id_emp = int(input("ID del empleado: "))
                contratos = gestor_con.obtener_contratos(id_emp)
                if contratos is None:
                    print("Empleado no encontrado.")
                elif not contratos:
                    print("El empleado no tiene contratos.")
                else:
                    for c in contratos:
                        print(f"ID: {c['id_contrato']}, Inicio: {c['fecha_inicio']}, Fin: {c['fecha_fin']}, Salario: {c['salario']}")
            except ValueError:
                print("ID inválido.")

        elif opcion == 8:
            vencidos = gestor_con.listar_contratos_vencidos()
            if not vencidos:
                print("No hay contratos vencidos.")
            else:
                for item in vencidos:
                    print(f"Empleado: {item['empleado']} (ID: {item['id_empleado']}) - Contrato {item['contrato']['id_contrato']} venció el {item['contrato']['fecha_fin']}")

        elif opcion == 9:
            print("Saliendo...")
            break
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()
