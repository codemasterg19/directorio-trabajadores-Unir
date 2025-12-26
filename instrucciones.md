- Quiero desarrollar una aplicación en Python que administre un directorio de empleados y sus contratos laborales usando un archivo JSON como almacenamiento persistente.
- Debe permitir:
  - Agregar empleados.
  - Actualizar empleados.
  - Eliminar empleados.
  - Consultar empleados.
  - Asociar contratos laborales a empleados.
  - Consultar contratos por empleado.
  - Filtrar contratos activos y vencidos.
  - Generar un reporte básico: lista de empleados con contratos vencidos.
  - Guardar y recuperar datos desde un archivo JSON llamado empleados.json.
  - Implementar pruebas unitarias con pytest para funcionalidades clave.
  - Incluir documentación en README.md con objetivo, instalación, ejecución y ejemplo de uso.

- Estructura obligatoria del proyecto (módulos):
  - gestor_empleados.py
    - Maneja la creación, actualización, eliminación y consulta de empleados.
    - Carga y guarda datos en empleados.json.
    - Métodos clave mínimos:
      - agregar_empleado(nombre, cargo) -> dict
      - eliminar_empleado(id) -> bool
      - buscar_empleado(id) -> dict
    - Debe asegurar IDs únicos para empleados.
  - gestor_contratos.py
    - Maneja la asociación de contratos a empleados.
    - Permite filtrar contratos activos y vencidos.
    - Métodos clave mínimos:
      - asociar_contrato(id_empleado, fecha_inicio, fecha_fin, salario) -> dict
      - listar_contratos_vencidos() -> list
    - Debe asegurar IDs únicos para contratos por empleado o globalmente (definir y documentar).
  - main.py
    - Interfaz de terminal (CLI) con un menú interactivo para gestionar empleados y contratos.
    - Debe solicitar datos al usuario por consola y mostrar resultados legibles.

- Formato de almacenamiento (empleados.json):
  - Debe respetar esta estructura base:
    {
      "empleados": [
        {
          "id": 1,
          "nombre": "Carlos Pérez",
          "cargo": "Desarrollador",
          "contratos": [
            {
              "id_contrato": 101,
              "fecha_inicio": "2023-02-15",
              "fecha_fin": "2024-02-15",
              "salario": 3500
            }
          ]
        }
      ]
    }

- Reglas y validaciones:
  - Fechas deben manejarse en formato ISO "YYYY-MM-DD".
  - Validar que fecha_fin >= fecha_inicio.
  - Salario debe ser numérico y mayor que 0.
  - Si un empleado no existe, las operaciones deben devolver errores controlados (sin reventar el programa).
  - Si empleados.json no existe al iniciar:
    - Se debe crear automáticamente con estructura vacía: {"empleados": []}
  - Todas las operaciones que modifican datos deben persistir en empleados.json.
  - Evitar duplicidad de empleados por ID y contratos por id_contrato.
  - Separar lógica de negocio (gestores) de la interfaz (main.py).

- Menú mínimo de main.py (sugerido):
  1) Agregar empleado
  2) Actualizar empleado
  3) Eliminar empleado
  4) Buscar empleado por ID
  5) Listar empleados
  6) Asociar contrato a empleado
  7) Ver contratos de un empleado
  8) Reporte: empleados con contratos vencidos
  9) Salir

- Pruebas unitarias (pytest):
  - Crear carpeta tests/ con al menos:
    - test_empleados.py
    - test_contratos.py
  - Pruebas mínimas obligatorias:
    - Probar que se agrega empleado correctamente.
    - Probar que se elimina un empleado.
    - Probar la búsqueda de un empleado.
    - Probar que un empleado tiene contrato (asociación correcta).
  - Las pruebas NO deben usar el empleados.json real:
    - Usar un archivo temporal o mocking para no ensuciar datos reales.

- Documentación (README.md):
  - Debe incluir:
    - Objetivo del proyecto.
    - Requisitos.
    - Instalación (venv + dependencias).
    - Ejecución (cómo correr main.py).
    - Ejecución de pruebas (pytest).
    - Ejemplo de uso con entradas y salidas.

- Entregable:
  - El proyecto debe poder comprimirse en zip con nombre:
    actmod2_nombre_apellido.zip
  - Si hay repositorio, incluir enlace en README.md.

- Pasos de construcción (guía paso a paso):
  - Paso 1: Crear el entorno virtual y activarlo.
  - Paso 2: Instalar dependencias necesarias.
  - Paso 3: Crear requirements.txt.
  - Paso 4: Crear gestor_empleados.py y su persistencia en empleados.json.
  - Paso 5: Crear gestor_contratos.py y su lógica de contratos vencidos/activos.
  - Paso 6: Crear main.py con menú interactivo.
  - Paso 7: Crear pruebas unitarias con pytest.
  - Paso 8: Crear README.md con documentación.
