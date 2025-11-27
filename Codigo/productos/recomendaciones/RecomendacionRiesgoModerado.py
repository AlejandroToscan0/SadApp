from core.interfaces.Recomendacion import Recomendacion

class RecomendacionRiesgoModerado(Recomendacion):
    """Recomendaciones para riesgo MODERADO."""
    def generar(self, resultado: str) -> str:
        print("\n--- [Factory Method] Creando recomendaciones para RIESGO MODERADO ---")
        return (
            f"⚠ {resultado}\n"
            "Recomendaciones:\n"
            "• Hablar con un familiar o amigo de confianza.\n"
            "• Practicar ejercicios de respiración durante 5-10 minutos.\n"
            "• Considerar consultar con un psicólogo.\n"
            "• Establecer rutinas diarias de autocuidado.\n"
            "• Evitar el aislamiento social."
        )

    def obtener_recursos(self) -> list:
        return [
            "https://www.psicologia.org/consulta-online",
            "https://www.respiracion.com/tecnicas-basicas",
            "https://www.apoyo-emocional.org/linea24h",
            "Número de ayuda: 024 (España)"
        ]