from core.interfaces.SaludMentalFactory import SaludMentalFactory
from productos.procesadores.ProcesadorPalabrasClave import ProcesadorPalabrasClave
from productos.analizadores.AnalizadorPuntajePonderado import AnalizadorPuntajePonderado

class FabricaLinguistica(SaludMentalFactory):
    def crear_procesador(self):
        return ProcesadorPalabrasClave()

    def crear_analizador(self):
        return AnalizadorPuntajePonderado()