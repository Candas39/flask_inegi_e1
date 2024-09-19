from flask import Flask, request, jsonify
from utils.get_info import get_info_inegi


app = Flask(__name__)

@app.route('/buscar_establecimientos', methods=['POST'])
def buscar_establecimientos():
    # Obtener los datos desde el JSON enviado en el POST
    data = request.get_json()
    tipo_establecimiento = data.get("tipo_establecimiento")
    coordenadas = data.get("coordenadas")
    radio = data.get("radio")
    
        # Llamar a la función get_info_inegi con los parámetros recibidos
    resultado = get_info_inegi(tipo_establecimiento, coordenadas, radio)
    
    # Devolver la respuesta en formato JSON
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)