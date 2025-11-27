from core.interfaces.Recomendacion import Recomendacion
from core.interfaces.RecomendacionFactory import RecomendacionFactory
from productos.recomendaciones.RecomendacionRiesgoAlto import RecomendacionRiesgoAlto

class RecomendacionRiesgoAltoFactory(RecomendacionFactory):
    """Factory Method para crear recomendación de RIESGO ALTO."""
    def crear_recomendacion(self) -> Recomendacion:
        return RecomendacionRiesgoAlto()