from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
datos = [
    {"id": 1, "nombre": "Alex", "descripcion": "Alex estuvo aqui"},
    {"id": 2, "nombre": "Fabricio", "descripcion": "Fabricio tambien estuvo aqui"},
    {"id": 3, "nombre": "Luna", "descripcion": "Luna no estuvo aqui"},
]
@app.route('/datos')
def get_elementos():
    resp = jsonify(datos)
    return resp
if __name__ == '__main__':
    app.run(debug=True, port=5000)