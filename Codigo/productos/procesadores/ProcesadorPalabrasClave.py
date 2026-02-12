from core.interfaces.ProcesadorTexto import ProcesadorTexto

class ProcesadorPalabrasClave(ProcesadorTexto):
    def procesar(self, texto: str) -> dict:
        """Preprocesamiento simple basado en reglas/keywords.

        Mejora: detecta muchas más señales de riesgo (triste, morir, matar, suicid,
        sin sentido, etc.) y usa substrings para frases como "sin sentido".
        """
        texto_lower = texto.lower()
        print(f"--- [Procesador Lingüistico] Tokenizando y buscando palabras clave en: '{texto}' ---")

        # Palabras de riesgo CRÍTICO (ideación suicida / autolesión)
        danger_terms = ["matar", "morir", "suicid", "suicida", "me quiero morir", "me quiero matar", 
                       "voy a matarme", "voy a morir", "me voy a matar", "quiero desaparecer", 
                       "mejor muerto", "terminar con todo"]

        # Palabras de riesgo ALTO (depresión severa, desesperanza)
        high_neg = ["deprim", "desesper", "sin esperanza", "no tiene sentido", "sin sentido", 
                    "nada tiene sentido", "no quiero vivir", "no quiero seguir", "sin ganas de vivir"]

        # Palabras de riesgo MODERADO (tristeza, melancolía, sinónimos)
        med_neg = ["triste", "tristeza", "melancól", "apesadumbr", "aflig", "abatid", "decaíd", 
                   "desolad", "desanim", "desconsolad", "angustiad", "apenado", "adolorido",
                   "mal", "bajo", "cansado", "agotado", "ansiedad", "ansioso", "preocupado"]

        # Palabras POSITIVAS (felicidad y sinónimos) - RIESGO BAJO o SIN PROBLEMA
        positive = ["feliz", "felicidad", "alegr", "contento", "satisfecho", "dichoso", 
                   "gozoso", "jovial", "optimista", "bien", "genial", "excelente", 
                   "maravilloso", "fantástico", "radiante", "animado"]

        # Primera persona (señala internalización)
        primera = ["me ", " yo", "mi ", "mí ", "estoy ", "me siento", "muy ", "soy "]

        # Desesperanza / falta de sentido
        desesperanza = ["sin sentido", "nada tiene sentido", "no tiene sentido", "vale la pena", 
                        "sin ganas", "no quiero vivir", "no quiero seguir", "sin esperanza", 
                        "todo es inútil", "para qué"]

        # Detectar términos de riesgo grave primero
        danger = any(k in texto_lower for k in danger_terms)

        # Detectar contexto positivo
        es_positivo = any(k in texto_lower for k in positive)

        # Calcular negatividad según jerarquía
        negatividad = 0.1
        if danger:
            negatividad = 1.0  # Riesgo crítico
        elif any(k in texto_lower for k in high_neg):
            negatividad = 0.85  # Riesgo alto
        elif any(k in texto_lower for k in med_neg):
            negatividad = 0.70  # Riesgo moderado (aumentado para asegurar score moderado)
        elif es_positivo:
            negatividad = 0.05  # Solo contextos positivos tienen negatividad muy baja
        else:
            # También catch explicit short negatives
            if "no" in texto_lower.split() or "nada" in texto_lower.split() or "nunca" in texto_lower.split():
                negatividad = 0.55

        primera_persona = 0.0
        if any(k in texto_lower for k in primera):
            primera_persona = 0.50

        desesperanza_score = 0.0
        if any(k in texto_lower for k in desesperanza):
            desesperanza_score = 0.80

        features = {
            "negatividad": negatividad,
            "primera_persona": primera_persona,
            "desesperanza": desesperanza_score,
            "danger": danger
        }
        return features