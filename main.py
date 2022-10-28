
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
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion

miControladorCiudadano=ControladorCiudadano()
miControladorCandidato=ControladorCandidato()
miControladorMateria=ControladorMateria()
miControladorDepartamento=ControladorDepartamento()
miControladorInscripcion=ControladorInscripcion()


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

#  Rutas Materias
@app.route("/materias",methods=['GET'])
def getMaterias():
    json=miControladorMateria.index()
    return jsonify(json)
@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorMateria.create(data)
    return jsonify(json)
@app.route("/materias/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorMateria.show(id)
    return jsonify(json)
@app.route("/materias/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json=miControladorMateria.update(id,data)
    return jsonify(json)
@app.route("/materias/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    json=miControladorMateria.delete(id)
    return jsonify(json)

#  Rutas Departamentos
@app.route("/departamentos",methods=['GET'])
def getDepartamentos():
    json=miControladorDepartamento.index()
    return jsonify(json)
@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json=miControladorDepartamento.create(data)
    return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['GET'])
def getDepartamento(id):
    json=miControladorDepartamento.show(id)
    return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json=miControladorDepartamento.update(id,data)
    return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    json=miControladorDepartamento.delete(id)
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

@app.route("/inscripciones/ciudadano/<string:id_ciudadano>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_ciudadano,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_ciudadano,id_materia)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>/ciudadano/<string:id_ciudadano>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_ciudadano,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_ciudadano,id_materia)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)

# Otras Rutas
@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoAMateria(id,id_departamento):
    json=miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(json)


# Funciones globales
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


