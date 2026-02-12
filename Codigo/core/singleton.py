from core.interfaces.SaludMentalFactory import SaludMentalFactory
from core.adapters.AdaptadorProcesador import AdaptadorProcesador
from core.observers.ObservadorAnalisis import GestorObservadores
from resource.GeneradorRecomendaciones import GeneradorRecomendaciones

class AdministradorAnalisisTexto:
    """
    PATRÓN CREACIONAL: SINGLETON
    Gestiona una única instancia del administrador de análisis.
    
    INTEGRACIÓN:
    - ADAPTER: Unifica la salida de diferentes procesadores
    - OBSERVER: Notifica observadores cuando se completa un análisis
    """

    _instancia = None

    def __init__(self, factory: SaludMentalFactory):
        print("Constructor Singleton ejecutado")
        self.factory = factory
        self.procesador_base = factory.crear_procesador()
        # ADAPTER PATTERN: Wrappear el procesador para unificar salida
        self.procesador = AdaptadorProcesador(self.procesador_base)
        self.analizador = factory.crear_analizador()
        # OBSERVER PATTERN: Inicializar gestor de observadores
        self.gestor_observadores = GestorObservadores()

    @classmethod
    def get_instancia(cls, factory: SaludMentalFactory = None):
        if cls._instancia is None:
            if factory is None:
                raise ValueError("Se debe proporcionar una fábrica al inicializar.")
            cls._instancia = cls(factory)

        return cls._instancia

    def set_factory(self, factory: SaludMentalFactory):
        """Cambia la fábrica y re-adapta los procesadores."""
        self.factory = factory
        self.procesador_base = factory.crear_procesador()
        # ADAPTER: Re-wrappear con la nueva fábrica
        self.procesador = AdaptadorProcesador(self.procesador_base)
        self.analizador = factory.crear_analizador()

    def analizar(self, texto: str) -> dict:
        """
        Realiza análisis completo del texto:
        1. Preprocesamiento (con ADAPTER)
        2. Análisis de riesgo
        3. Generación de recomendaciones (Factory Method)
        4. Notificación a OBSERVERS
        """
        # Paso 1: Preprocesamiento con ADAPTER (unifica formatos)
        datos_adaptados = self.procesador.procesar(texto)
        # Extraer features del resultado adaptado
        datos = datos_adaptados["features"]
        
        # Paso 2: Análisis de riesgo
        resultado_analisis = self.analizador.evaluar_riesgo(datos)
        
        # Paso 3: Factory Method - Generar recomendaciones según nivel de riesgo
        nivel_riesgo = resultado_analisis["nivel"].split(" (")[0]  # Extrae "Riesgo ALTO", "Riesgo MODERADO", etc.
        recomendacion_texto, recursos = GeneradorRecomendaciones.generar_recomendacion(
            nivel_riesgo, 
            resultado_analisis["nivel"]
        )
        
        resultado_completo = {
            "analisis": resultado_analisis,
            "recomendacion": recomendacion_texto,
            "recursos": recursos
        }
        
        # Paso 4: OBSERVER PATTERN - Notificar observadores
        self.gestor_observadores.notificar("analisis_completado", resultado_completo)
        
        return resultado_completo
    
    def registrar_observador(self, observador):
        """Registra un observador para recibir notificaciones."""
        self.gestor_observadores.registrar(observador)
    
    def desregistrar_observador(self, observador):
        """Desregistra un observador."""
        self.gestor_observadores.desregistrar(observador)

