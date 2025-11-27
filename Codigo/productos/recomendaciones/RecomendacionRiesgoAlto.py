from core.interfaces.Recomendacion import Recomendacion

class RecomendacionRiesgoAlto(Recomendacion):
    """Recomendaciones para riesgo ALTO."""
    def generar(self, resultado: str) -> str:
        print("\n--- [Factory Method] Creando recomendaciones para RIESGO ALTO ---")
        return (
            f"🚨 {resultado}\n"
            "ACCIÓN INMEDIATA REQUERIDA:\n"
            "• Contactar INMEDIATAMENTE con un profesional de salud mental.\n"
            "• Llamar a la línea de prevención de suicidio: 024 (España) o 1-800-273-8255 (USA).\n"
            "• No quedarse solo/a.\n"
            "• Buscar apoyo de familia o amigos cercanos.\n"
            "• Ir a la emergencia más cercana si es necesario.\n"
            "• Evitar cualquier acción que pueda causar daño."
        )

    def obtener_recursos(self) -> list:
        return [
            "Emergencia: 024 (España - Línea Prevención Suicidio)",
            "Emergencia: 1-800-273-8255 (USA - National Suicide Prevention)",
            "Emergencia: 911 o 112 (Ambulancia)",
            "https://www.teleline.es/024",
            "https://suicidepreventionlifeline.org"
        ]
