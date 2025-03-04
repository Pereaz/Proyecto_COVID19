import pandas as pd
from api import obtener_datos

# Configurar parámetros de consulta
departamento = "RISARALDA"
limite_registros = 500  # Número manejable para pruebas

# Obtener datos de la API
try:
    datos = obtener_datos(departamento, limite_registros)
    df = pd.DataFrame(datos)
    print("Datos obtenidos correctamente. Filas:", len(df))
except Exception as e:
    print("Error al obtener datos:", e)

# --- Análisis Exploratorio (EDA) ---
print("\n=== Primeras filas del DataFrame ===")
print(df.head())

print("\n=== Información del DataFrame ===")
print(df.info())

print("\n=== Valores faltantes por columna ===")
print(df.isnull().sum())

print("\n=== Estadísticas descriptivas de columnas numéricas ===")
print(df.describe())

print("\n=== Frecuencia de Tipos de Recuperación ===")
print(df['tipo_recuperacion'].value_counts())

print("\n=== Frecuencia de Estados de Pacientes ===")
print(df['estado'].value_counts())

print("\n=== Fuentes de Contagio ===")
print(df['fuente_tipo_contagio'].value_counts())

# Convertir fecha a tipo datetime
df['fecha_reporte_web'] = pd.to_datetime(df['fecha_reporte_web'])

# Extraer mes y año
df['mes_reporte'] = df['fecha_reporte_web'].dt.month
casos_por_mes = df.groupby('mes_reporte').size()

print("\n=== Casos por Mes ===")
print(casos_por_mes)

print("\n=== Edad Promedio por Estado ===")
print(df.groupby('estado')['edad'].mean())

print("\n=== Edades Extremas ===")
print(f"Máxima edad: {df['edad'].max()} años")
print(f"Mínima edad: {df['edad'].min()} años")

print("\n=== Rango de Fechas ===")
print(f"Fecha más antigua: {df['fecha_reporte_web'].min()}")
print(f"Fecha más reciente: {df['fecha_reporte_web'].max()}")