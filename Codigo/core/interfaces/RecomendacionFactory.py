from abc import ABC, abstractmethod
from core.interfaces.Recomendacion import Recomendacion

class RecomendacionFactory(ABC):
    """Factory Method - Fábrica abstracta para crear recomendaciones por nivel de riesgo."""
    @abstractmethod
    def crear_recomendacion(self) -> Recomendacion:
        pass
