"""
Observador concreto que registra logs de análisis.
"""

from core.observers.ObservadorAnalisis import ObservadorAnalisis
from datetime import datetime


class LoggerAnalisis(ObservadorAnalisis):
    """
    Implementación de observador que registra todos los análisis realizados.
    Útil para auditoría y debugging.
    """
    
    def actualizar(self, evento: str, resultado: dict) -> None:
        """Registra el evento de análisis en log."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if evento == "analisis_completado":
            nivel = resultado.get("analisis", {}).get("nivel", "Desconocido")
            score = resultado.get("analisis", {}).get("score", "N/A")
            print(f"\n[LOG {timestamp}] ✓ Análisis completado")
            print(f"    Nivel de riesgo: {nivel}")
            print(f"    Score: {score}")
        
        elif evento == "riesgo_detectado":
            nivel_riesgo = resultado.get("nivel_riesgo", "Desconocido")
            print(f"\n[LOG {timestamp}] ⚠️  Riesgo detectado: {nivel_riesgo}")
        
        elif evento == "procesamiento":
            metodo = resultado.get("metodo", "Desconocido")
            print(f"\n[LOG {timestamp}] 🔄 Procesamiento: {metodo}")
