from core.interfaces.SaludMentalFactory import SaludMentalFactory
from productos.procesadores.ProcesadorVectorial import ProcesadorVectorial
from productos.analizadores.ClasificadorNaiveBayes import ClasificadorNaiveBayes

class FabricaMachineLearning(SaludMentalFactory):
    def crear_procesador(self):
        return ProcesadorVectorial()

    def crear_analizador(self):
        return ClasificadorNaiveBayes()
