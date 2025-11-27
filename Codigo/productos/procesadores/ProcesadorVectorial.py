from core.interfaces.ProcesadorTexto import ProcesadorTexto

class ProcesadorVectorial(ProcesadorTexto):
    def procesar(self, texto: str) -> list:
        print("--- [Procesador ML] Convirtiendo texto a vectores numericos ---")
        return [0.1, 0.5, 0.9, 0.0]
