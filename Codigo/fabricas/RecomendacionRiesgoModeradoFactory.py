from core.interfaces.Recomendacion import Recomendacion
from core.interfaces.RecomendacionFactory import RecomendacionFactory
from productos.recomendaciones.RecomendacionRiesgoModerado import RecomendacionRiesgoModerado

class RecomendacionRiesgoModeradoFactory(RecomendacionFactory):
    """Factory Method para crear recomendación de RIESGO MODERADO."""
    def crear_recomendacion(self) -> Recomendacion:
        return RecomendacionRiesgoModerado()
