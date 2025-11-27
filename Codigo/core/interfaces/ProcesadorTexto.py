from abc import ABC, abstractmethod

class ProcesadorTexto(ABC):
    """Interfaz para el preprocesamiento del texto."""
    @abstractmethod
    def procesar(self, texto: str) -> any:
        pass
