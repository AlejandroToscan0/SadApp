"""
Observador concreto que alerta cuando se detecta riesgo alto.
"""

from core.observers.ObservadorAnalisis import ObservadorAnalisis


class AlertaRiesgoAlto(ObservadorAnalisis):
    """
    Implementación de observador que emite alertas cuando se detecta RIESGO ALTO.
    Puede integrarse con sistemas de notificación externa.
    """
    
    def actualizar(self, evento: str, resultado: dict) -> None:
        """Alerta si el riesgo es ALTO."""
        if evento == "analisis_completado":
            nivel = resultado.get("analisis", {}).get("nivel", "")
            
            if "ALTO" in nivel:
                self._generar_alerta(resultado)
    
    def _generar_alerta(self, resultado: dict) -> None:
        """Genera una alerta visual prominente."""
        print("\n" + "="*70)
        print("🚨 ALERTA DE RIESGO ALTO DETECTADA 🚨")
        print("="*70)
        print(f"Nivel: {resultado.get('analisis', {}).get('nivel', 'Desconocido')}")
        print(f"Score: {resultado.get('analisis', {}).get('score', 'N/A'):.2f}")
        print(f"Método: {resultado.get('analisis', {}).get('metodo', 'Desconocido')}")
        print("\nRECOMENDACIONES INMEDIATAS:")
        print(resultado.get('recomendacion', 'No disponible'))
        print("="*70 + "\n")
