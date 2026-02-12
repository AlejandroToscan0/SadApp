import argparse
import os
from fabricas.FabricaLinguistica import FabricaLinguistica
from fabricas.FabricaMachineLearning import FabricaMachineLearning
from core.singleton import AdministradorAnalisisTexto
from core.observers.LoggerAnalisis import LoggerAnalisis
from core.observers.AlertaRiesgoAlto import AlertaRiesgoAlto



def obtener_factory_por_nombre(name: str):
    """Retorna la fábrica correspondiente según el nombre dado."""
    if name and name.lower().startswith('ml'):
        return FabricaMachineLearning()
    return FabricaLinguistica()


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
    parser = argparse.ArgumentParser(description="CLI para probar patrones (Singleton, Abstract Factory, Strategy, Factory Method)")
    parser.add_argument('--text', '-t', help='Texto a analizar. Si no se provee, se pedirá interactivamente.')
    parser.add_argument('--strategy', '-s', choices=['linguistica', 'ml'], default='linguistica', help='Estrategia/fábrica a usar para el análisis.')
    parser.add_argument('--web', action='store_true', help='Levanta el front web (Flask).')
    parser.add_argument('--port', type=int, default=int(os.environ.get('PORT', 5000)), help='Puerto para el front web si se usa --web.')
    args = parser.parse_args()

    if args.web:
        # Ejecutar el front web (importa y arranca la app flask)
        print(f"Arrancando front web en http://127.0.0.1:{args.port}")
        # import local de la app y arrancarla
        try:
            from webapp import app
            app.run(host='127.0.0.1', port=args.port)
        except Exception as e:
            print('No se pudo iniciar la aplicación web:', e)
        raise SystemExit(0)

    # Si no pedimos web, procesar en modo CLI
    if args.text:
        entrada = args.text
    else:
        entrada = input('Ingrese el texto para analizar: ')

    print('\n' + '='*70)
    print('  SISTEMA DE ANÁLISIS DE SALUD MENTAL (CLI)')
    print('='*70)
    print(f"Texto ingresado: '{entrada}'")

    # Inicializar singleton con la fábrica seleccionada
    factory = obtener_factory_por_nombre(args.strategy)
    print('\n[PASO 1] Inicializando/obteniendo Administrador con la fábrica seleccionada...')
    manager = AdministradorAnalisisTexto.get_instancia(factory)
    manager.set_factory(factory)
    
    # OBSERVER PATTERN: Registrar observadores
    print('[PASO 1.5] Registrando observadores...')
    logger = LoggerAnalisis()
    alerta = AlertaRiesgoAlto()
    manager.registrar_observador(logger)
    manager.registrar_observador(alerta)

    print('\n[PASO 2] Ejecutando análisis...')
    resultado = manager.analizar(entrada)
    mostrar_resultado(resultado, f"ANÁLISIS ({'ML' if args.strategy=='ml' else 'Lingüístico'})")

    # Resumen
    print('\n' + '='*70)
    print('  RESUMEN DE PATRONES DE DISEÑO UTILIZADOS')
    print('='*70)
    print('\n🔵 PATRONES CREACIONALES:')
    print('  ✓ SINGLETON: Instancia única del AdministradorAnalisisTexto')
    print('  ✓ ABSTRACT FACTORY: FabricaLinguistica y FabricaMachineLearning')
    print('  ✓ FACTORY METHOD: GeneradorRecomendaciones crea recomendaciones específicas')
    print('\n🟢 PATRONES ESTRUCTURALES:')
    print('  ✓ ADAPTER: AdaptadorProcesador unifica salida de procesadores heterogéneos')
    print('\n🟡 PATRONES DE COMPORTAMIENTO:')
    print('  ✓ STRATEGY: Diferentes procesadores y analizadores intercambiables')
    print('  ✓ OBSERVER: LoggerAnalisis y AlertaRiesgoAlto notificados de eventos')
    print('='*70)