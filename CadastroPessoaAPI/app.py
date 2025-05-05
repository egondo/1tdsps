from flask import Flask, jsonify, request
from flask_cors import cross_origin, CORS

import negocio
import traceback

app = Flask("API_PESSOA")

CORS(app, origins="http://127.0.0.1:5000")

@app.route("/pessoas", methods=["GET"])
@cross_origin()
def get_pessoa():
    return ({"nome": "FIAP"}, 200)



@app.route("/pessoas", methods=["POST"])
@cross_origin()
def grava_pessoa():
    dados = request.json
    try:
        pes = dados['pessoa']
        end = dados['endereco']

        negocio.cadastra_pessoa(pes, end)
        return (dados, 201)
    except Exception as erro:
        traceback.print_exc()
        info = {'title': "erro no cadastramento", "status": 400}
        return (info, 400)

app.run(debug=True)

