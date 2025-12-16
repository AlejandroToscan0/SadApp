from core.interfaces.ProcesadorTexto import ProcesadorTexto

class ProcesadorPalabrasClave(ProcesadorTexto):
    def procesar(self, texto: str) -> dict:
        """Preprocesamiento simple basado en reglas/keywords.

        Mejora: detecta muchas más señales de riesgo (triste, morir, matar, suicid,
        sin sentido, etc.) y usa substrings para frases como "sin sentido".
        """
        texto_lower = texto.lower()
        print(f"--- [Procesador Lingüistico] Tokenizando y buscando palabras clave en: '{texto}' ---")

        # Palabras/fragmentos que indican alta negatividad
        high_neg = ["triste", "deprim", "matar", "morir", "suicid", "suicida", "lastim", "anim", "no quiero", "no puedo"]
        med_neg = ["mal", "bajo", "cansado", "agotado", "ansiedad", "ansioso"]

        # Primera persona (señala internalización)
        primera = ["me ", " yo", "mi ", "mí ", "estoy ", "me siento"]

        # Desesperanza / falta de sentido
        desesperanza = ["sin sentido", "nada tiene sentido", "no tiene sentido", "vale la pena", "sin ganas"]

        negatividad = 0.1
        if any(k in texto_lower for k in high_neg):
            negatividad = 0.90
        elif any(k in texto_lower for k in med_neg):
            negatividad = 0.60

        primera_persona = 0.0
        if any(k in texto_lower for k in primera):
            primera_persona = 0.50

        desesperanza_score = 0.0
        if any(k in texto_lower for k in desesperanza):
            desesperanza_score = 0.80

        # Also catch explicit short negatives
        if "no" in texto_lower.split() or "nada" in texto_lower.split() or "nunca" in texto_lower.split():
            negatividad = max(negatividad, 0.6)

        features = {
            "negatividad": negatividad,
            "primera_persona": primera_persona,
            "desesperanza": desesperanza_score
        }
        return features