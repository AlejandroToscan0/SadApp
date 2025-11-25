from fabricas.fabricas import FabricaLinguistica, FabricaMachineLearning
from core.singleton import AdministradorAnalisisTexto


if __name__ == "__main__":
    entrada = input("Ingrese el texto para analizar: ")
    
    print("\n=== USANDO SINGLETON CON ANALISIS LINGÜÍSTICO ===")
    manager = AdministradorAnalisisTexto.get_instancia(FabricaLinguistica())
    print("Resultado:", manager.analizar(entrada))

    print("\n=== CAMBIO DE ESTRATEGIA A MACHINE LEARNING ===")
    manager.set_factory(FabricaMachineLearning())
    print("Resultado:", manager.analizar(entrada))

    # inst1 = AdministradorAnalisisTexto.get_instancia(FabricaLinguistica())
    # inst2 = AdministradorAnalisisTexto.get_instancia()
    # inst3 = AdministradorAnalisisTexto.get_instancia()