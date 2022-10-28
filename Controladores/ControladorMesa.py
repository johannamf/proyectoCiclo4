from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        nuevoMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)

    def show(self, id):
        elMesa = Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__

    def update(self, id, infoMesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        mesaActual.total_votos = infoMesa["total_votos"]
        mesaActual.id_candidato_ganador = infoMesa["id_candidato_ganador"]
        mesaActual.id_partido_ganador = infoMesa["id_partido_ganador"]
        mesaActual.cant_votos_ganador = infoMesa["cant_votos_inscritos"]

        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)
