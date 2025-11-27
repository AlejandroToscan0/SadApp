from core.interfaces import SaludMentalFactory
from resource.GeneradorRecomendaciones import GeneradorRecomendaciones

class AdministradorAnalisisTexto:

    _instancia = None

    def __init__(self, factory: SaludMentalFactory):
        print("Constructor Singleton ejecutado")
        self.factory = factory
        self.procesador = factory.crear_procesador()
        self.analizador = factory.crear_analizador()

    @classmethod
    def get_instancia(cls, factory: SaludMentalFactory = None):
        if cls._instancia is None:
            if factory is None:
                raise ValueError("Se debe proporcionar una fábrica al inicializar.")
            cls._instancia = AdministradorAnalisisTexto(factory)

        return cls._instancia

    def set_factory(self, factory: SaludMentalFactory):
        self.factory = factory
        self.procesador = factory.crear_procesador()
        self.analizador = factory.crear_analizador()

    def analizar(self, texto: str) -> dict:
        """
        Realiza análisis completo del texto:
        1. Preprocesamiento
        2. Análisis de riesgo
        3. Generación de recomendaciones (Factory Method)
        """
        # Paso 1: Preprocesamiento
        datos = self.procesador.procesar(texto)
        
        # Paso 2: Análisis de riesgo
        resultado_analisis = self.analizador.evaluar_riesgo(datos)
        
        # Paso 3: Factory Method - Generar recomendaciones según nivel de riesgo
        nivel_riesgo = resultado_analisis["nivel"].split(" (")[0]  # Extrae "Riesgo ALTO", "Riesgo MODERADO", etc.
        recomendacion_texto, recursos = GeneradorRecomendaciones.generar_recomendacion(
            nivel_riesgo, 
            resultado_analisis["nivel"]
        )
        
        return {
            "analisis": resultado_analisis,
            "recomendacion": recomendacion_texto,
            "recursos": recursos
        }
