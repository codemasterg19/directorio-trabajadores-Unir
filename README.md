# Directorio de Empleados

Aplicación de consola (CLI) en Python para la administración de empleados y sus contratos laborales, con persistencia de datos en JSON.

## Objetivo
Gestionar el ciclo de vida de los empleados (creación, actualización, eliminación, consulta) y sus contratos, permitiendo identificar contratos vigentes y vencidos.

## Requisitos
- Python 3.8 o superior.
- Librería `pytest` para pruebas unitarias.

## Instalación

1. Clonar o descargar este repositorio/archivo.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar la aplicación, ejecute el script principal:

```bash
python main.py
```

Siga las instrucciones del menú interactivo.

## Ejecución de Pruebas

Para validar el funcionamiento del sistema, ejecute las pruebas unitarias:

```bash
pytest
```
O para más detalle:
```bash
pytest -v
```

## Ejemplo de Uso

1. Inicie la aplicación: `python main.py`
2. Seleccione la opción **1 (Agregar empleado)**.
   - Nombre: `Juan Perez`
   - Cargo: `Desarrollador`
3. Seleccione la opción **6 (Asociar contrato)**.
   - ID Empleado: `1`
   - Fecha Inicio: `2023-01-01`
   - Fecha Fin: `2023-12-31`
   - Salario: `3000`
4. Seleccione la opción **8 (Reporte: Contratos vencidos)** para verificar si aparece (dependiendo de la fecha actual).
5. Seleccione **9** para salir.

## Estructura del Proyecto
- `main.py`: Punto de entrada y menú CLI.
- `gestor_empleados.py`: Lógica de gestión de empleados y persistencia.
- `gestor_contratos.py`: Lógica de gestión de contratos.
- `empleados.json`: Archivo de base de datos (se crea automáticamente).
- `tests/`: Pruebas unitarias.

## Autor
Estudiante Pablo Jiménez - UNIR,  Actividad Módulo 2
