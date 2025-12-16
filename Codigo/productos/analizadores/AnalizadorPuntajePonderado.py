from core.interfaces.AnalizadorRiesgo import AnalizadorRiesgo

class AnalizadorPuntajePonderado(AnalizadorRiesgo):
    def evaluar_riesgo(self, features: dict) -> dict:
        # Si el procesador marcó 'danger' (términos de ideación suicida), forzamos Riesgo ALTO
        if features.get("danger"):
            score = 1.0
            print(f"--- [Analizador Lingüistico] Danger flag detectada, forzando Riesgo ALTO ---")
            nivel = "Riesgo ALTO"
        else:
            score = (0.40 * features["negatividad"]) + \
                    (0.30 * features["primera_persona"]) + \
                    (0.20 * features["desesperanza"])

            print(f"--- [Analizador Lingüistico] Score Calculado: {score:.2f} ---")

            if score >= 0.60:
                nivel = "Riesgo ALTO"
            elif 0.40 <= score < 0.60:
                nivel = "Riesgo MODERADO"
            else:
                nivel = "Riesgo BAJO"
        
        return {
            "nivel": nivel,
            "score": score,
            "features": features,
            "metodo": "Análisis Lingüístico"
        }
