from core.interfaces.AnalizadorRiesgo import AnalizadorRiesgo

class AnalizadorPuntajePonderado(AnalizadorRiesgo):
    def evaluar_riesgo(self, features: dict) -> dict:
        # Si el procesador marcó 'danger' (términos de ideación suicida), forzamos Riesgo ALTO
        if features.get("danger"):
            score = 1.0
            print(f"--- [Analizador Lingüistico] Danger flag detectada, forzando Riesgo ALTO ---")
            nivel = "Riesgo ALTO"
        else:
            # Pesos ajustados para dar más importancia a negatividad
            score = (0.60 * features["negatividad"]) + \
                    (0.25 * features["primera_persona"]) + \
                    (0.15 * features["desesperanza"])

            print(f"--- [Analizador Lingüistico] Score Calculado: {score:.2f} ---")

            # Regla especial: si negatividad >= 0.65 y es la señal principal, 
            # garantizar al menos nivel MODERADO
            if features["negatividad"] >= 0.65 and score < 0.40:
                score = 0.45
                print(f"--- [Analizador Lingüistico] Ajuste por alta negatividad, nuevo score: {score:.2f} ---")

            if score >= 0.60:
                nivel = "Riesgo ALTO"
            elif 0.40 <= score < 0.60:
                nivel = "Riesgo MODERADO"
            elif 0.15 <= score < 0.40:
                nivel = "Riesgo BAJO"
            else:
                nivel = "Sin Problema"
        
        return {
            "nivel": nivel,
            "score": score,
            "features": features,
            "metodo": "Análisis Lingüístico"
        }
