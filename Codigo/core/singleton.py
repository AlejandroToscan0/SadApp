from core.interfaces import SaludMentalFactory


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

    def analizar(self, texto: str) -> str:
        datos = self.procesador.procesar(texto)
        return self.analizador.evaluar_riesgo(datos)
