from sodapy import Socrata

def obtener_datos(departamento, limite):
    cliente = Socrata("www.datos.gov.co", None)
    resultados = cliente.get("gt2j-8ykr", departamento_nom=departamento, limit=limite)
    return resultados