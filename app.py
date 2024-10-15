from flask import Flask, request, jsonify, render_template
from utils.get_info import get_info_inegi
from database.sqlite import insert_data, filter_data 




app = Flask(__name__)

    
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/tabla', methods=['GET','POST'])
def index_tabla():
        tipo_establecimiento = request.args.get("tipo_establecimiento")
        coordenadas = request.args.get("coordenadas")
        radio = request.args.get("radio")
        print(tipo_establecimiento, radio, coordenadas)
        datos = get_info_inegi(tipo_establecimiento, coordenadas, radio)
        print(type(datos), datos[0])
        json_data= {
            "tipo_establecimiento":tipo_establecimiento,
            "coordenadas":coordenadas,
            "radio":radio
        }
        if request.args.get("json"):
            return jsonify(datos)    

        return render_template('table.html', datos=datos, json_data=json_data)

@app.route('/buscar_establecimientos', methods=['POST'])
def buscar_establecimientos():
    data = request.get_json()
    if not data or not all(k in data for k in ("tipo_establecimiento", "coordenadas", "radio")):
        return jsonify({"error": "Parámetros incompletos"}), 400
    
    tipo_establecimiento = data.get("tipo_establecimiento")
    coordenadas = data.get("coordenadas")
    radio = data.get("radio")
    resultado = get_info_inegi(tipo_establecimiento, coordenadas, radio)
    return jsonify(resultado), 200


@app.route('/insert_data', methods=['POST'])
def insert_data_api():
    data = request.get_json()
    if not data or not all(k in data for k in ("tipo_establecimiento", "coordenadas", "radio")):
        return jsonify({"error": "Parámetros incompletos"}), 400
    
    tipo_establecimiento = data.get("tipo_establecimiento")
    coordenadas = data.get("coordenadas")
    radio = data.get("radio")
    resultado = get_info_inegi(tipo_establecimiento, coordenadas, radio)
    return jsonify(insert_data(resultado, 'inegi_test.db', tipo_establecimiento)), 200


@app.route('/filter_data', methods=['POST'])
def search_data_api():
    data = request.get_json()
    if not data or "palabra_clave" not in data:
        return jsonify({"error": "Parámetros incompletos"}), 400

    palabra_clave = data.get("palabra_clave")
    resultados = filter_data(palabra_clave)
    return jsonify(resultados), 200
    


if __name__ == '__main__':
    app.app_context().push()
    app.run(debug=True, port=5000)
 
