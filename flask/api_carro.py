from flask import Flask, request, jsonify
import db

#app = Flask(__name__)
app = Flask("API CARRO")

@app.route("/hello", methods=["GET"])
def get_hello():
    info = {
        "msg": "Hello World!"
    }
    return (info, 200) #sempre retornamos uma tupla

#associando uma URL à função get_all_carros
@app.route("/carros", methods=["GET"])
def get_all_carros():
    return (jsonify(db.carros), 200)

@app.route("/carros/<int:id>", methods=["GET"])
def get_carros_by_id(id: int):
    for car in db.carros:
        if car['id'] == id:
            return (jsonify(car), 200)
    info = {"msg": "Carro não encontrado", "status": 404}
    return (jsonify(info), 404)

@app.route("/carros", methods=["PUT"]) #atualizando recurso
def atualiza_carro():
    #recuperando a informação enviada pelo cliente
    carro = request.json 
    for i in range(len(db.carros)):
        car = db.carros[i]
        if car['id'] == carro['id']:
            db.carros[i] = carro
            return (jsonify(carro), 200)

    msg = {"msg": "Carro com o id nao encontrado", 'status': 404}
    return (jsonify(msg), 404)




app.run(debug=True)