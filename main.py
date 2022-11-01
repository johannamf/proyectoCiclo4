
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCiudadano import ControladorCiudadano
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorInscripcion import ControladorInscripcion
from Controladores.ControladorMesa import ControladorMesa

miControladorCiudadano=ControladorCiudadano()
miControladorCandidato=ControladorCandidato()
miControladorPartido=ControladorPartido()
miControladorMesa=ControladorMesa()
miControladorInscripcion=ControladorInscripcion()
miControladorMesa=ControladorMesa()


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Hola Mundo, Server Running ..."
    return jsonify(json)

#  Rutas Ciudadanos
@app.route("/ciudadanos",methods=['GET'])
def getCiudadanos():
    json=miControladorCiudadano.index()
    return jsonify(json)
@app.route("/ciudadanos",methods=['POST'])
def crearCiudadano():
    data = request.get_json()
    json=miControladorCiudadano.create(data)
    return jsonify(json)
@app.route("/ciudadanos/<string:id>",methods=['GET'])
def getCiudadano(id):
    json=miControladorCiudadano.show(id)
    return jsonify(json)
@app.route("/ciudadanos/<string:id>",methods=['PUT'])
def modificarCiudadano(id):
    data = request.get_json()
    json=miControladorCiudadano.update(id,data)
    return jsonify(json)
@app.route("/ciudadanos/<string:id>",methods=['DELETE'])
def eliminarCiudadano(id):
    json=miControladorCiudadano.delete(id)
    return jsonify(json)

# Rutas Candidatos
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

#  Rutas Partidos
@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

#  Rutas Mesas
@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

#  Rutas Inscripcion
@app.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json=miControladorInscripcion.index()
    return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)

@app.route("/inscripciones/ciudadano/<string:id_ciudadano>/partido/<string:id_partido>",methods=['POST'])
def crearInscripcion(id_ciudadano,id_partido):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_ciudadano,id_partido)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>/ciudadano/<string:id_ciudadano>/partido/<string:id_partido>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_ciudadano,id_partido):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_ciudadano,id_partido)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)

# Otras Rutas
@app.route("/partidos/<string:id>/mesa/<string:id_mesa>",methods=['PUT'])
def asignarMesaAPartido(id,id_mesa):
    json=miControladorPartido.asignarMesa(id,id_mesa)
    return jsonify(json)
@app.route("/resultado",methods=['GET'])
def mostrarResultado():
    return "El resultado ira aqui pronto!"

# Funciones globales
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


