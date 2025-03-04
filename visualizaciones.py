import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos limpios
df = pd.read_csv('covid_risaralda_limpio.csv')

# Convertir columna de fechas a datetime (¡FIX PRINCIPAL!)
df['fecha_reporte_web'] = pd.to_datetime(df['fecha_reporte_web'], errors='coerce')

# Eliminar filas con fechas inválidas (opcional, pero recomendado)
df = df.dropna(subset=['fecha_reporte_web'])

# ------------------------------------------------------------
# 1. Histograma de edades
plt.figure(figsize=(10, 6))
plt.hist(df['edad'], bins=20, color='#4CAF50', edgecolor='black')
plt.title('Distribución de Edades de Casos COVID-19 en Risaralda')
plt.xlabel('Edad')
plt.ylabel('Número de Casos')
plt.grid(axis='y', alpha=0.5)
plt.savefig('histograma_edades.png')
plt.show()

# ------------------------------------------------------------
# 2. Casos por ciudad
plt.figure(figsize=(12, 6))
df['ciudad_municipio_nom'].value_counts().plot(kind='bar', color='#2196F3')
plt.title('Casos de COVID-19 por Ciudad en Risaralda')
plt.xlabel('Ciudad')
plt.ylabel('Número de Casos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('casos_por_ciudad.png')
plt.show()

# ------------------------------------------------------------
# 3. Tendencia mensual de casos (¡CORREGIDO!)
plt.figure(figsize=(12, 6))

# Extraer mes y ordenar
df['mes_reporte'] = df['fecha_reporte_web'].dt.month
casos_por_mes = df['mes_reporte'].value_counts().sort_index()

# Nombres de meses (solo los necesarios)
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'][:len(casos_por_mes)]

plt.plot(meses, casos_por_mes.values, marker='o', color='#FF5722', linestyle='--')
plt.title('Tendencia Mensual de Casos en Risaralda')
plt.xlabel('Mes')
plt.ylabel('Número de Casos')
plt.grid(True)
plt.savefig('tendencias_mensuales.png')
plt.show()

# ------------------------------------------------------------
# 4. Boxplot de edades por estado (¡CORREGIDO!)
plt.figure(figsize=(10, 6))
df.boxplot(column='edad', by='estado', grid=False, patch_artist=True)
plt.title('Distribución de Edades por Estado del Paciente')
plt.suptitle('')  # Eliminar título automático
plt.xlabel('Estado')
plt.ylabel('Edad (años)')
plt.savefig('boxplot_edades_estado.png')
plt.show()