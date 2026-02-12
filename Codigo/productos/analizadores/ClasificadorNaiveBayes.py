from core.interfaces.AnalizadorRiesgo import AnalizadorRiesgo

class ClasificadorNaiveBayes(AnalizadorRiesgo):
    def evaluar_riesgo(self, vector: list) -> dict:
        probabilidad = 0.78
        print(f"--- [Clasificador ML] Probabilidad detectada: {probabilidad} ---")

        if probabilidad > 0.7:
            nivel = "Riesgo ALTO (Predicción ML)"
        elif probabilidad >= 0.3:
            nivel = "Riesgo BAJO (Predicción ML)"
        else:
            nivel = "Sin Problema (Predicción ML)"
        
        return {
            "nivel": nivel,
            "probabilidad": probabilidad,
            "vector": vector,
            "metodo": "Machine Learning"
        }
