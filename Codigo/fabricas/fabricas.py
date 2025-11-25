from core.interfaces import SaludMentalFactory
from productos.procesadores import ProcesadorPalabrasClave, ProcesadorVectorial
from productos.analizadores import AnalizadorPuntajePonderado, ClasificadorNaiveBayes


class FabricaLinguistica(SaludMentalFactory):
    def crear_procesador(self):
        return ProcesadorPalabrasClave()

    def crear_analizador(self):
        return AnalizadorPuntajePonderado()


class FabricaMachineLearning(SaludMentalFactory):
    def crear_procesador(self):
        return ProcesadorVectorial()

    def crear_analizador(self):
        return ClasificadorNaiveBayes()
