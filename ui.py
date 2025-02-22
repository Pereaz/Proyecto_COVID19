def pedir_datos():
    while True:
        departamento = input("Ingrese el departamento (Ej: RISARALDA): ").strip().upper()
        if departamento:  # Evitar campos vacíos
            break
    while True:
        try:
            limite = int(input("Ingrese el número de registros (Ej: 5): "))
            if limite > 0:
                break
        except ValueError:
            print("Debe ingresar un número")
    return departamento, limite

def mostrar_resultados(datos):
    nombres_amigables = {
        "ciudad_municipio_nom": "Ciudad",
        "departamento_nom": "Departamento",
        "edad": "Edad",
        "fuente_tipo_contagio": "Tipo de contagio",
        "estado": "Estado",
        "pais_viajo_1_nom": "País de procedencia"
    }
    
    for registro in datos:
        print("----------------------------------------")
        for clave_tecnica, nombre_legible in nombres_amigables.items():
            valor = registro.get(clave_tecnica, "N/A")
            print("{:<20}: {:<15}".format(nombre_legible, valor))