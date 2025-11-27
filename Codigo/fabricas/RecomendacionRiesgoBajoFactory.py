from core.interfaces.Recomendacion import Recomendacion
from core.interfaces.RecomendacionFactory import RecomendacionFactory
from productos.recomendaciones.RecomendacionRiesgoBajo import RecomendacionRiesgoBajo

class RecomendacionRiesgoBajoFactory(RecomendacionFactory):
    """Factory Method para crear recomendación de RIESGO BAJO."""
    def crear_recomendacion(self) -> Recomendacion:
        return RecomendacionRiesgoBajo()