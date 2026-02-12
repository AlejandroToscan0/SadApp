"""
PATRÓN ESTRUCTURAL: ADAPTER

Unifica la salida de procesadores que retornan formatos diferentes.
- ProcesadorPalabrasClave retorna: dict con features
- ProcesadorVectorial retorna: list con vectores

El adapter convierte ambos a un formato estándar universal.
"""

class AdaptadorProcesador:
    """
    Adapter que unifica la interfaz de salida de procesadores.
    Convierte formatos heterogéneos a un formato estándar.
    """
    
    def __init__(self, procesador):
        """
        Args:
            procesador: Instancia de ProcesadorTexto
        """
        self.procesador = procesador
    
    def procesar(self, texto: str) -> dict:
        """
        Procesa el texto y retorna un formato estándar universal.
        
        Returns:
            dict con estructura: {
                "tipo_procesador": identificador del procesador,
                "datos_originales": salida original del procesador,
                "features": dict con features normalizadas,
                "metadata": dict con información del procesamiento
            }
        """
        # Obtener salida original del procesador
        resultado_original = self.procesador.procesar(texto)
        
        # Adaptar según tipo de salida
        return self._adaptar_resultado(resultado_original)
    
    def _adaptar_resultado(self, resultado_original):
        """Convierte el resultado a formato universal."""
        
        # Si es un diccionario (ProcesadorPalabrasClave)
        if isinstance(resultado_original, dict):
            return {
                "tipo_procesador": "PalabrasClave",
                "datos_originales": resultado_original,
                "features": resultado_original,  # Ya está en formato features
                "metadata": {
                    "formato_original": "dict",
                    "procesador": self.procesador.__class__.__name__
                }
            }
        
        # Si es una lista (ProcesadorVectorial)
        elif isinstance(resultado_original, list):
            # Convertir vector a features normalizadas
            features_normalizadas = self._normalizar_vector(resultado_original)
            return {
                "tipo_procesador": "Vectorial",
                "datos_originales": resultado_original,
                "features": features_normalizadas,
                "metadata": {
                    "formato_original": "list",
                    "procesador": self.procesador.__class__.__name__,
                    "largo_vector": len(resultado_original)
                }
            }
        
        # Formato desconocido - retornar como está
        else:
            return {
                "tipo_procesador": "Desconocido",
                "datos_originales": resultado_original,
                "features": {},
                "metadata": {
                    "formato_original": type(resultado_original).__name__,
                    "procesador": self.procesador.__class__.__name__,
                    "advertencia": "Formato no reconocido, retornado sin conversión"
                }
            }
    
    def _normalizar_vector(self, vector: list) -> dict:
        """
        Convierte un vector numérico a features.
        Permite que el Analizador trabaje consistently.
        """
        if len(vector) >= 4:
            return {
                "negatividad": vector[0],
                "primera_persona": vector[1],
                "desesperanza": vector[2],
                "peligro": vector[3]
            }
        else:
            # Vector pequeño - rellena con defaults
            return {
                "negatividad": vector[0] if len(vector) > 0 else 0.0,
                "primera_persona": vector[1] if len(vector) > 1 else 0.0,
                "desesperanza": vector[2] if len(vector) > 2 else 0.0,
                "peligro": 0.0
            }
