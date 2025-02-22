# Proyecto: Consulta de Casos de COVID-19 en Colombia

## Requerimientos Funcionales
- Consulta datos de la API del portal de Datos Abiertos de Colombia.
- Filtra por departamento y número de registros.
- Muestra resultados en formato tabular con las columnas: Ciudad, Departamento, Edad, Tipo de contagio, Estado y País de procedencia.

## Estructura del Proyecto
proyecto_covid/
├── api.py # Módulo para consultar la API
├── ui.py # Módulo para interacción con el usuario
├── main.py # Archivo principal de ejecución
└── README.md # Documentación

## Diagrama de Componentes
Un "componente" es un módulo independiente con una función específica.  
El "diagrama de componentes" muestra cómo interactúan los módulos:
+-------------+ +-------------+ +-------------+
| main.py | ----> | api.py | ----> | ui.py |
+-------------+ +-------------+ +-------------+
- main.py: Inicia el programa y coordina los demás módulos.
- api.py: Gestiona la conexión y consulta a la API.
- ui.py: Maneja la entrada y salida de datos.

## ¿Para qué sirve un Diagrama de Componentes?
- Visualizar la arquitectura modular del software.
- Entender las dependencias entre módulos.
- Facilitar el mantenimiento y escalabilidad.

## Instalación y Uso
1. Instalar dependencias:
   ```bash
   pip install sodapy requests

2. Ejecutar el programa:
   python main.py