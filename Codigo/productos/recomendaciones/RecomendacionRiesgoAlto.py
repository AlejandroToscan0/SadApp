from core.interfaces.Recomendacion import Recomendacion


class RecomendacionRiesgoAlto(Recomendacion):
    """Recomendaciones para riesgo ALTO."""

    def generar(self, resultado: str) -> str:
        print(
            "\n--- [Factory Method] Creando recomendaciones para RIESGO ALTO ---")
        return (
            "ACCIÓN INMEDIATA REQUERIDA:\n"
            "• Contactar INMEDIATAMENTE con un profesional de salud mental.\n"
            "• Llamar a la línea de prevención de suicidio: 171 (Ecuador).\n"
            "• No quedarse solo/a.\n"
            "• Buscar apoyo de familia o amigos cercanos.\n"
            "• Ir a la emergencia más cercana si es necesario.\n"
            "• Evitar cualquier acción que pueda causar daño."
        )

    def obtener_recursos(self) -> list:
        return [
            "Emergencia: 171 (Ecuador - Línea de Ayuda en Crisis)",
            "Emergencia: 911 (Policía/Ambulancia Ecuador)",
            "DINAPEN: 1800-356-236 (Protección de niños y adolescentes)",
            "MSP Salud Mental: (02) 3814-400",
            "https://www.salud.gob.ec"
        ]
