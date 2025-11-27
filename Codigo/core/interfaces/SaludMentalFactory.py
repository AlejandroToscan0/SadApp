from abc import ABC, abstractmethod
from core.interfaces.AnalizadorRiesgo import AnalizadorRiesgo
from core.interfaces.ProcesadorTexto import ProcesadorTexto

class SaludMentalFactory(ABC):
    """Fábrica Abstracta para crear familias de analisis."""
    @abstractmethod
    def crear_procesador(self) -> ProcesadorTexto:
        pass

    @abstractmethod
    def crear_analizador(self) -> AnalizadorRiesgo:
        pass

