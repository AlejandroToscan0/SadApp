from core.interfaces.Recomendacion import Recomendacion

class RecomendacionNingunProblema(Recomendacion):
    """Recomendaciones cuando no se detecta ningún problema."""
    def generar(self, resultado: str) -> str:
        print("\n--- [Factory Method] Creando recomendaciones para NINGÚN PROBLEMA ---")
        return (
            f"✓ {resultado}\n\n"
            "😊 ¡No encontré ningún problema que implique mi ayuda!\n\n"
            "Parece que todo está bien. Espero tengas un buen día.\n\n"
            "Recuerda que estoy aquí si en algún momento necesitas apoyo o simplemente quieres conversar."
        )

    def obtener_recursos(self) -> list:
        return [
            "https://www.bienestar.com/mantener-salud-mental",
            "https://www.mindfulness.com/practicas-diarias",
            "https://www.salud.gob.es/recursos-preventivos"
        ]
