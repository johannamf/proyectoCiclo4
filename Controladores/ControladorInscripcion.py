from Modelos.Inscripcion import Inscripcion
from Modelos.Ciudadano import Ciudadano
from Modelos.Materia import Materia
from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Repositorios.RepositorioCiudadano import RepositorioCiudadano
from Repositorios.RepositorioMateria import RepositorioMateria
class ControladorInscripcion():
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioCiudadanos = RepositorioCiudadano()
        self.repositorioMaterias = RepositorioMateria()

    def index(self):
        return self.repositorioInscripcion.findAll()

    """
    Asignacion estudiante y materia a inscripción
    """
    def create(self, infoInscripcion,id_ciudadano,id_materia):
        nuevaInscripcion = Inscripcion(infoInscripcion)
        elCiudadano = Ciudadano(self.repositorioCiudadanos.findById(id_ciudadano))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        nuevaInscripcion.ciudadano = elCiudadano
        nuevaInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        elInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return elInscripcion.__dict__

    """
    Modificación de inscripción (ciudadano y materia)
    """
    def update(self,id,infoInscripcion,id_ciudadano,id_materia):
        laInscripcion=Inscripcion(self.repositorioInscripcion.findById(id))
        laInscripcion.año=infoInscripcion["año"]
        laInscripcion.semestre = infoInscripcion["semestre"]
        laInscripcion.notaFinal=infoInscripcion["nota_final"]
        elCiudadano =Ciudadano(self.repositorioCiudadano.findById(id_ciudadano))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        laInscripcion.ciudadano = elCiudadano
        laInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(laInscripcion)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)