from fabricas.fabricas import FabricaLinguistica, FabricaMachineLearning
from core.singleton import AdministradorAnalisisTexto


if __name__ == "__main__":
    entrada = "Ya no quiero levantarme. Nada tiene sentido. Me siento sola y cansada todo el tiempo."

    print("\n=== USANDO SINGLETON CON ANÁLISIS LINGÜÍSTICO ===")
    manager = AdministradorAnalisisTexto.get_instancia(FabricaLinguistica())
    print("Resultado:", manager.analizar(entrada))

    print("\n=== CAMBIO DE ESTRATEGIA A MACHINE LEARNING ===")
    manager.set_factory(FabricaMachineLearning())
    print("Resultado:", manager.analizar(entrada))
