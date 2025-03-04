from api import obtener_datos
from ui import pedir_datos, mostrar_resultados
import requests

def main():
    departamento, limite = pedir_datos()
    try:
        datos = obtener_datos(departamento, limite)
        mostrar_resultados(datos)
    except requests.exceptions.ConnectionError:
        print("Error: Sin conexión a Internet.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()