from core.interfaces.ProcesadorTexto import ProcesadorTexto

class ProcesadorPalabrasClave(ProcesadorTexto):
    def procesar(self, texto: str) -> dict:
        print(f"--- [Procesador Lingüistico] Tokenizando y buscando palabras clave en: '{texto}' ---")
        palabras = texto.lower().split()

        features = {
            "negatividad": 0.80 if "no" in palabras or "nada" in palabras else 0.1,
            "primera_persona": 0.40 if "me" in palabras or "yo" in palabras else 0.0,
            "desesperanza": 0.65 if "sentido" in palabras else 0.0
        }
        return features