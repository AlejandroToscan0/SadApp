from abc import ABC, abstractmethod

class ProcesadorTexto(ABC):
    """Interfaz para el preprocesamiento del texto."""
    @abstractmethod
    def procesar(self, texto: str) -> any:
        pass


class AnalizadorRiesgo(ABC):
    """Interfaz para determinar el nivel de riesgo emocional."""
    @abstractmethod
    def evaluar_riesgo(self, datos_procesados: any) -> str:
        pass




class SaludMentalFactory(ABC):
    """Fábrica Abstracta para crear familias de analisis."""
    @abstractmethod
    def crear_procesador(self) -> ProcesadorTexto:
        pass

    @abstractmethod
    def crear_analizador(self) -> AnalizadorRiesgo:
        pass
