Proyecto: Consulta y Análisis de Casos de COVID-19 en Colombia

Tabla de Contenidos
- Requerimientos Funcionales
- Estructura del Proyecto
- Hallazgos Clave
- Diagrama de Componentes
- Instalación y Uso
- Reproducir el Análisis
- Licencia

------------------------------------------------------------

Requerimientos Funcionales
- Consultar datos en tiempo real de la API del Portal de Datos Abiertos de Colombia: https://www.datos.gov.co/
- Filtrar casos por departamento y número máximo de registros.
- Mostrar resultados en formato tabular con las columnas:
  - Ciudad de ubicación
  - Departamento
  - Edad del paciente
  - Tipo de contagio
  - Estado del caso
  - País de procedencia (si aplica)
- Generar gráficos para análisis exploratorio (EDA).

------------------------------------------------------------

Estructura del Proyecto
proyecto_covid/
├── data/
│   └── covid_risaralda_limpio.csv
├── outputs/
│   └── evidencias/
│       ├── boxplot_edades_estado.png
│       ├── casos_por_ciudad.png
│       ├── histograma_edades.png
│       └── tendencias_mensuales.png
├── src/
│   ├── api.py
│   ├── ejercicio_practico.py
│   ├── limpieza.py
│   ├── main.py
│   ├── ui.py
│   └── visualizaciones.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
------------------------------------------------------------

Hallazgos Clave

Distribución de Edades:
- 70% de los casos se concentran entre 20 y 60 años.
- Edad máxima registrada: 105 años (Ver gráfico).

Ciudades más Afectadas:
- Pereira y Dosquebradas concentran el 80% de los casos (Ver gráfico).

Tipos de Contagio:
- 85% de los casos son de origen comunitario.

Tendencias Temporales:
- Pico máximo en Julio 2023 (Ver gráfico).

Relación Edad-Gravedad:
- Pacientes en estado Fallecido tienen mediana de edad más alta (Ver gráfico).

------------------------------------------------------------

Diagrama de Componentes

+-------------+       +-------------+       +-------------+
|   main.py   | ----> |   api.py    | ----> |   ui.py     |
+-------------+       +-------------+       +-------------+
       │                     │
       └-> | limpieza.py |   └-> | visualizaciones.py |

Funciones por Componente:
- main.py: Coordina la ejecución del programa.
- api.py: Consulta datos de la API gubernamental.
- ui.py: Gestiona interacción con el usuario.
- limpieza.py: Limpia y transforma datos crudos.
- visualizaciones.py: Genera gráficos para análisis exploratorio.

------------------------------------------------------------

Instalación y Uso

Dependencias:
pip install pandas matplotlib sodapy requests

Ejecutar Consulta Básica:
python main.py

Ejemplo de uso:
Ingrese el departamento (Ej: RISARALDA): RISARALDA
Ingrese el número de registros (Ej: 5): 10

------------------------------------------------------------

Reproducir el Análisis

Flujo Completo:

Obtener y limpiar datos:
python limpieza.py  # Genera: covid_risaralda_limpio.csv

Generar visualizaciones:
python visualizaciones.py  # Gráficos en /evidencias

Explorar datos (opcional):
python ejercicio_practico.py  # Análisis estadístico

------------------------------------------------------------

Licencia

Este proyecto es de código abierto bajo licencia MIT.
