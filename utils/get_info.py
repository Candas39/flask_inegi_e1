import requests

def get_info_inegi(tipo_establecimiento, coordenadas, radio):
    base_url = "https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{}/{}/{}/523a778b-026e-443c-85a6-fd5c619e4a5d"
    url_completa = base_url.format(tipo_establecimiento, coordenadas, radio)
    payload = ""
    headers = {
        'Cookie': 'BIGipServerLB_apis=3590494474.20480.0000'
    }
    response = requests.request("GET", url_completa, headers=headers, data=payload)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return {"error": "La respuesta no contiene un JSON válido"}
    else:
        return {"error": f"Error en la solicitud, código de estado: {response.status_code}"}
