from core.interfaces.RecomendacionFactory import RecomendacionFactory
from fabricas.RecomendacionRiesgoBajoFactory import RecomendacionRiesgoBajoFactory
from fabricas.RecomendacionRiesgoModeradoFactory import RecomendacionRiesgoModeradoFactory
from fabricas.RecomendacionRiesgoAltoFactory import RecomendacionRiesgoAltoFactory

class GeneradorRecomendaciones:
    """Context que utiliza Factory Method para generar recomendaciones dinámicamente."""

    # Mapeo de niveles de riesgo a factories
    _factories_map = {
        "Riesgo BAJO": RecomendacionRiesgoBajoFactory(),
        "Riesgo MODERADO": RecomendacionRiesgoModeradoFactory(),
        "Riesgo ALTO": RecomendacionRiesgoAltoFactory(),
    }

    @classmethod
    def obtener_factory(cls, nivel_riesgo: str) -> RecomendacionFactory:
        """Factory Method: Retorna la factory correspondiente al nivel de riesgo."""
        return cls._factories_map.get(nivel_riesgo, RecomendacionRiesgoModeradoFactory())

    @classmethod
    def generar_recomendacion(cls, nivel_riesgo: str, resultado: str) -> tuple:
        """
        Genera una recomendación usando el patrón Factory Method.
        Retorna: (recomendación_texto, recursos)
        """
        factory = cls.obtener_factory(nivel_riesgo)
        recomendacion = factory.crear_recomendacion()
        
        texto = recomendacion.generar(resultado)
        recursos = recomendacion.obtener_recursos()
        
        return texto, recursos
