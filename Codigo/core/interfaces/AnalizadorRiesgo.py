from abc import ABC, abstractmethod

class AnalizadorRiesgo(ABC):
    """Interfaz para determinar el nivel de riesgo emocional."""
    @abstractmethod
    def evaluar_riesgo(self, datos_procesados: any) -> dict:
        pass

