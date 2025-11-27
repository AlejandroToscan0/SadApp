from fabricas.FabricaLinguistica import FabricaLinguistica
from fabricas.FabricaMachineLearning import FabricaMachineLearning
from core.singleton import AdministradorAnalisisTexto


def mostrar_resultado(resultado: dict, titulo: str):
    """Función auxiliar para mostrar resultados de forma legible."""
    print(f"\n{'='*70}")
    print(f"  {titulo}")
    print(f"{'='*70}")
    
    # Mostrar análisis
    print(f"\n[ANÁLISIS REALIZADO]")
    print(f"Método: {resultado['analisis']['metodo']}")
    print(f"Resultado: {resultado['analisis']['nivel']}")
    
    if 'score' in resultado['analisis']:
        print(f"Score: {resultado['analisis']['score']:.2f}")
    if 'probabilidad' in resultado['analisis']:
        print(f"Probabilidad: {resultado['analisis']['probabilidad']:.2f}")
    
    # Mostrar recomendaciones
    print(f"\n[RECOMENDACIONES - Factory Method]")
    print(resultado['recomendacion'])
    
    # Mostrar recursos
    print(f"\n[RECURSOS Y ENLACES]")
    for i, recurso in enumerate(resultado['recursos'], 1):
        print(f"  {i}. {recurso}")


if __name__ == "__main__":
    # Entrada del usuario (ejemplo del documento de requisitos)
    entrada = input("Ingrese el texto para analizar: ")
    
    print("\n" + "="*70)
    print("  SISTEMA DE ANÁLISIS DE SALUD MENTAL")
    print("="*70)
    print(f"Texto ingresado: '{entrada}'")
    
    # ============ ANÁLISIS CON ESTRATEGIA LINGÜÍSTICA ============
    print("\n\n[PASO 1] Inicializando Singleton con Fábrica Lingüística...")
    manager = AdministradorAnalisisTexto.get_instancia(FabricaLinguistica())
    
    print("\n[PASO 2] Ejecutando análisis lingüístico...")
    resultado_linguistico = manager.analizar(entrada)
    mostrar_resultado(resultado_linguistico, "ANÁLISIS LINGÜÍSTICO (Abstract Factory + Factory Method)")
    
    # ============ ANÁLISIS CON ESTRATEGIA MACHINE LEARNING ============
    print("\n\n[PASO 3] Cambiando a estrategia de Machine Learning...")
    manager.set_factory(FabricaMachineLearning())
    
    print("\n[PASO 4] Ejecutando análisis con ML...")
    resultado_ml = manager.analizar(entrada)
    mostrar_resultado(resultado_ml, "ANÁLISIS MACHINE LEARNING (Abstract Factory + Factory Method)")
    
    # ============ RESUMEN FINAL ============
    print("\n\n" + "="*70)
    print("  RESUMEN DE PATRONES DE DISEÑO UTILIZADOS")
    print("="*70)
    print("✓ SINGLETON: Instancia única del AdministradorAnalisisTexto")
    print("✓ ABSTRACT FACTORY: FabricaLinguistica y FabricaMachineLearning")
    print("✓ STRATEGY: Diferentes procesadores y analizadores intercambiables")
    print("✓ FACTORY METHOD: GeneradorRecomendaciones crea recomendaciones específicas")
    print("  - RecomendacionRiesgoBajoFactory")
    print("  - RecomendacionRiesgoModeradoFactory")
    print("  - RecomendacionRiesgoAltoFactory")
    print("="*70)