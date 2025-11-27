from core.interfaces.Recomendacion import Recomendacion

class RecomendacionRiesgoBajo(Recomendacion):
    """Recomendaciones para riesgo BAJO."""
    def generar(self, resultado: str) -> str:
        print("\n--- [Factory Method] Creando recomendaciones para RIESGO BAJO ---")
        return (
            f"✓ {resultado}\n"
            "Recomendaciones:\n"
            "• Mantener hábitos de sueño regulares.\n"
            "• Realizar actividad física moderada (30 min diarios).\n"
            "• Socializar regularmente con amigos y familia.\n"
            "• Practicar técnicas de relajación como meditación."
        )

    def obtener_recursos(self) -> list:
        return [
            "https://www.mindfulness.com/meditacion-basica",
            "https://www.ejercicio.org/rutinas-30min",
            "https://www.salud.gob.es/autoayuda"
        ]