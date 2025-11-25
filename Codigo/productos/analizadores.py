from core.interfaces import AnalizadorRiesgo

# ==========================================
# Analizadores - Lingüístico
# ==========================================

class AnalizadorPuntajePonderado(AnalizadorRiesgo):
    def evaluar_riesgo(self, features: dict) -> str:
        score = (0.40 * features["negatividad"]) + \
                (0.30 * features["primera_persona"]) + \
                (0.20 * features["desesperanza"])

        print(f"--- [Analizador Lingüistico] Score Calculado: {score:.2f} ---")

        if score >= 0.60:
            return "Riesgo ALTO"
        elif 0.40 <= score < 0.60:
            return "Riesgo MODERADO"
        else:
            return "Riesgo BAJO"


# ==========================================
# Analizadores - Machine Learning
# ==========================================

class ClasificadorNaiveBayes(AnalizadorRiesgo):
    def evaluar_riesgo(self, vector: list) -> str:
        probabilidad = 0.78
        print(f"--- [Clasificador ML] Probabilidad detectada: {probabilidad} ---")

        if probabilidad > 0.7:
            return "Riesgo ALTO (Predicción ML)"
        return "Riesgo BAJO (Predicción ML)"
