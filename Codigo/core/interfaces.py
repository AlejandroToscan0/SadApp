from abc import ABC, abstractmethod

# ==========================================
# 1. Abstract Products (Interfaces)
# ==========================================

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


# ==========================================
# 4. Abstract Factory
# ==========================================

class SaludMentalFactory(ABC):
    """Fábrica Abstracta para crear familias de análisis."""
    @abstractmethod
    def crear_procesador(self) -> ProcesadorTexto:
        pass

    @abstractmethod
    def crear_analizador(self) -> AnalizadorRiesgo:
        pass
