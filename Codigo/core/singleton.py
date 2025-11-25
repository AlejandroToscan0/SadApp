from core.interfaces import SaludMentalFactory


class AdministradorAnalisisTexto:
    """
    Singleton que administra el proceso de análisis completo.
    """

    _instancia = None

    def __init__(self, factory: SaludMentalFactory):
        self.factory = factory
        self._procesador = factory.crear_procesador()
        self._analizador = factory.crear_analizador()

    @classmethod
    def get_instancia(cls, factory: SaludMentalFactory = None):
        if cls._instancia is None:
            if factory is None:
                raise ValueError("Se debe proporcionar una fábrica al inicializar.")
            cls._instancia = AdministradorAnalisisTexto(factory)

        return cls._instancia

    def set_factory(self, factory: SaludMentalFactory):
        self.factory = factory
        self._procesador = factory.crear_procesador()
        self._analizador = factory.crear_analizador()

    def analizar(self, texto: str) -> str:
        datos = self._procesador.procesar(texto)
        return self._analizador.evaluar_riesgo(datos)
