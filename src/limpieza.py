import pandas as pd
from api import obtener_datos

# 1. Obtener datos de la API
departamento = "RISARALDA"
limite = 500
try:
    datos = obtener_datos(departamento, limite)
    df = pd.DataFrame(datos)
    print("Datos iniciales obtenidos (sin procesar)")
    print("Filas/columnas originales:", df.shape)
except Exception as e:
    print("Error al obtener datos:", e)
    exit()

# 2. Eliminar columnas innecesarias (ejemplo)
columnas_a_eliminar = [
    'nom_grupo_',        # 495/500 NaN
    'per_etn_',          # Pocos valores útiles
    'fecha_muerte',       # 486/500 NaN
    'id_de_caso'          # Identificador no útil para análisis
]
df = df.drop(columns=columnas_a_eliminar, errors='ignore')
print("\nColumnas eliminadas:", columnas_a_eliminar)

# 3. Convertir tipos de datos
# 3.1 Convertir edad a numérico
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')  # coerce = convertir errores a NaN

# 3.2 Convertir fechas a formato datetime
columnas_fecha = [
    'fecha_reporte_web',
    'fecha_de_notificaci_n',
    'fecha_inicio_sintomas',
    'fecha_diagnostico'
]
for col in columnas_fecha:
    df[col] = pd.to_datetime(df[col], errors='coerce')

print("\nTipos de datos actualizados:")
print(df.dtypes)

# 4. Manejar valores faltantes
# 4.1 Eliminar filas donde 'edad' es NaN
df = df.dropna(subset=['edad'])

# 4.2 Imputar valores faltantes en 'tipo_recuperacion'
moda_recuperacion = df['tipo_recuperacion'].mode()[0]
df['tipo_recuperacion'] = df['tipo_recuperacion'].fillna(moda_recuperacion)

print("\nValores faltantes después de limpieza:")
print(df.isnull().sum())

# 5. Guardar datos limpios
df.to_csv('data/covid_risaralda_limpio.csv', index=False)
print("\nDatos guardados en: covid_risaralda_limpio.csv")
print("Formato final:", df.shape)