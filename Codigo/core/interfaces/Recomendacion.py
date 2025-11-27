from abc import ABC, abstractmethod

class Recomendacion(ABC):
    """Interfaz para generar recomendaciones según el nivel de riesgo."""
    @abstractmethod
    def generar(self, resultado: str) -> str:
        pass

    @abstractmethod
    def obtener_recursos(self) -> list:
        pass



