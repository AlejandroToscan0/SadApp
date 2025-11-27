from core.interfaces.AnalizadorRiesgo import AnalizadorRiesgo

class ClasificadorNaiveBayes(AnalizadorRiesgo):
    def evaluar_riesgo(self, vector: list) -> dict:
        probabilidad = 0.78
        print(f"--- [Clasificador ML] Probabilidad detectada: {probabilidad} ---")

        if probabilidad > 0.7:
            nivel = "Riesgo ALTO (Predicción ML)"
        else:
            nivel = "Riesgo BAJO (Predicción ML)"
        
        return {
            "nivel": nivel,
            "probabilidad": probabilidad,
            "vector": vector,
            "metodo": "Machine Learning"
        }
