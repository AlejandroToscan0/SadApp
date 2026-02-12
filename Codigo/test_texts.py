"""
Textos de Prueba para Sistema de Análisis de Riesgo Emocional

Este módulo contiene ejemplos de textos categorizados por nivel de riesgo
para realizar pruebas comprehensivas del sistema de análisis.

Categorías de riesgo:
- BAJO: 0.0 - 0.4
- MODERADO: 0.4 - 0.6
- ALTO: 0.6 - 0.85
- CRÍTICO: >= 0.85
"""

# Textos de RIESGO BAJO (0.0 - 0.4)
TEXTOS_RIESGO_BAJO = [
    "Hoy fue un día normal, nada especial.",
    "Me siento bien, todo va según lo planeado.",
    "Estoy contento con los resultados.",
    "La vida sigue su curso naturalmente.",
    "Tengo ganas de continuar con mis actividades.",
    "Los días pasan con tranquilidad.",
    "Me siento optimista sobre el futuro.",
    "Las cosas van mejorando poco a poco.",
    "Estoy satisfecho con mis logros.",
    "Tengo esperanza en lo que viene.",
    "Me siento feliz y realizado.",
    "Todo parece estar en orden.",
    "Puedo manejar los desafíos del día.",
    "Me encuentro en paz conmigo mismo.",
    "La vida me ofrece muchas oportunidades.",
    "Estoy agradecido por lo que tengo.",
    "Me siento motivado para seguir adelante.",
    "Mis relaciones sociales son positivas.",
    "Disfruto del tiempo que paso con mis seres queridos.",
    "Siento que controlo mi vida.",
]

# Textos de RIESGO MODERADO (0.4 - 0.6)
TEXTOS_RIESGO_MODERADO = [
    "Algunos días me siento preocupado sin razón aparente.",
    "A veces me siento bajo de ánimo.",
    "Tengo dudas sobre mis decisiones.",
    "Me cuesta trabajo concentrarme en las tareas.",
    "He tenido días difíciles recientemente.",
    "No me siento tan motivado como antes.",
    "Hay momentos donde me siento abrumado.",
    "Tengo pensamientos recurrentes que me molestan.",
    "Mi energía no es la de antes.",
    "Me cuesta dormir algunas noches.",
    "A menudo me siento cansado sin razón.",
    "Siento que algo anda mal conmigo.",
    "He estado más irritable últimamente.",
    "No disfruto de las cosas que solía disfrutar.",
    "Me siento alejado de mis amigos.",
    "Tengo miedo al futuro.",
    "A veces siento que no pertenezco aquí.",
    "Me resulta difícil tomar decisiones.",
    "He notado cambios en mi apetito.",
    "No puedo dejar de pensar en mis problemas.",
    "Siento que las cosas se me escapan de las manos.",
    "Hay días donde todo me parece gris.",
    "No sé qué me está pasando últimamente.",
    "Me siento perdido en la vida.",
]

# Textos de RIESGO ALTO (0.6 - 0.85)
TEXTOS_RIESGO_ALTO = [
    "Me siento desesperado y sin esperanza.",
    "Tengo pensamientos negativos continuos sobre mi vida.",
    "No veo mejora en mi situación, todo empeora.",
    "Me despierto con angustia cada mañana.",
    "Nada me importa ya, todo perdió sentido.",
    "Me siento completamente solo y abandonado.",
    "Quisiera desaparecer de este lugar.",
    "He pensado seriamente en hacerme daño.",
    "Mi vida es un fracaso total y no tiene remedio.",
    "Preferiría no despertar mañana.",
    "Mi dolor emocional es insoportable.",
    "Ya no encuentro razones para vivir.",
    "Me siento atrapado sin salida.",
    "Todo lo que intento falla miserablemente.",
    "Siento que soy una carga para los demás.",
    "Nadie realmente me entiende.",
    "No tengo futuro que esperar.",
    "Me odio a mí mismo constantemente.",
    "Mis problemas son demasiado grandes para resolverlos.",
    "Considero que la vida no vale la pena vivirla.",
    "He estado pensando en formas de escapar.",
    "Siento que la muerte sería un alivio.",
    "Todos estarían mejor sin mí.",
    "No merezco ser feliz.",
    "El sufrimiento nunca terminará.",
    "He perdido completamente el control.",
    "Mi situación es hopeless.",
    "Quisiera nunca haber nacido.",
]

# Textos de RIESGO CRÍTICO (>= 0.85)
TEXTOS_RIESGO_CRITICO = [
    "No quiero vivir, nadie me necesita.",
    "Voy a terminar con esto de una vez por todas.",
    "Tengo un plan para suicidarme esta noche.",
    "Nadie puede ayudarme, todo es demasiado.",
    "Me voy a inyectar veneno.",
    "Voy a saltar desde el puente, es la única solución.",
    "Tengo las pastillas listas para terminar con todo.",
    "La muerte es mi única esperanza.",
    "Todos estarían mejor sin mí.",
    "Voy a dejar notas de despedida para mi familia.",
    "He decidido que mañana será mi último día.",
    "Ya no hay nada que pueda salvarme.",
    "Voy a acabar con mi vida porque no puedo más.",
    "He decidido cómo me suicidaré.",
    "Estoy buscando un lugar seguro para hacerlo.",
    "Mi familia merece alguien mejor que yo.",
    "Esto terminará ahora, no puede esperar más.",
    "He rentado una habitación para estar solo.",
    "Dejé todo en orden para cuando me vaya.",
    "Ya he dicho adiós a las personas que amo.",
    "La próxima vez que me vean será en mi funeral.",
    "No hay razón para que continúe respirando.",
    "Mi existencia es nociva para todos.",
    "Estoy preparando todo para esta noche.",
    "Encontré la manera perfecta de hacerlo.",
]


def obtener_textos_por_nivel(nivel):
    """
    Obtiene textos de prueba para un nivel de riesgo específico.

    Args:
        nivel (str): Nivel de riesgo ('bajo', 'moderado', 'alto', 'critico')

    Returns:
        list: Lista de textos para el nivel especificado
    """
    nivel = nivel.lower().strip()
    
    if nivel == 'bajo':
        return TEXTOS_RIESGO_BAJO
    elif nivel == 'moderado':
        return TEXTOS_RIESGO_MODERADO
    elif nivel == 'alto':
        return TEXTOS_RIESGO_ALTO
    elif nivel == 'critico':
        return TEXTOS_RIESGO_CRITICO
    else:
        raise ValueError(f"Nivel de riesgo no válido: {nivel}")


def obtener_todos_los_textos():
    """Obtiene todos los textos de prueba organizados por nivel."""
    return {
        'bajo': TEXTOS_RIESGO_BAJO,
        'moderado': TEXTOS_RIESGO_MODERADO,
        'alto': TEXTOS_RIESGO_ALTO,
        'critico': TEXTOS_RIESGO_CRITICO,
    }


def obtener_resumen_textos():
    """Imprime un resumen de los textos disponibles."""
    print("=" * 70)
    print("TEXTOS DE PRUEBA DISPONIBLES")
    print("=" * 70)
    
    todos = obtener_todos_los_textos()
    
    for nivel, textos in todos.items():
        print(f"\n{nivel.upper() } ({len(textos)} textos):")
        print("-" * 70)
        for i, texto in enumerate(textos, 1):
            print(f"  {i:2d}. {texto[:60]}..." if len(texto) > 60 else f"  {i:2d}. {texto}")


def probar_textos_modo_masivo():
    """
    Ejecuta pruebas en modo masivo con todos los textos de prueba.
    Útil para verificar el funcionamiento del sistema.
    """
    from main import ejecutar_analisis
    
    todos = obtener_todos_los_textos()
    resultados = {'bajo': [], 'moderado': [], 'alto': [], 'critico': []}
    
    print("\n" + "=" * 70)
    print("PRUEBA EN MODO MASIVO")
    print("=" * 70)
    
    for nivel, textos in todos.items():
        print(f"\nAnalyzing {len(textos)} texts at {nivel.upper()} risk level...")
        print("-" * 70)
        
        for i, texto in enumerate(textos, 1):
            try:
                resultado = ejecutar_analisis(texto, 'linguistica')
                resultados[nivel].append(resultado)
                status = "✓" if resultado else "✗"
                print(f"  {status} [{i:2d}/{len(textos)}] Processed")
            except Exception as e:
                print(f"  ✗ [{i:2d}/{len(textos)}] Error: {str(e)[:40]}")
    
    print("\n" + "=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    for nivel, resultados_nivel in resultados.items():
        exito = len([r for r in resultados_nivel if r])
        total = len(resultados_nivel)
        print(f"{nivel.upper()}: {exito}/{total} textos procesados exitosamente")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Textos de prueba para Sistema de Análisis de Riesgo Emocional"
    )
    parser.add_argument(
        '--nivel',
        choices=['bajo', 'moderado', 'alto', 'critico', 'todos'],
        default='todos',
        help='Nivel de riesgo de textos a mostrar'
    )
    parser.add_argument(
        '--masivo',
        action='store_true',
        help='Ejecutar pruebas en modo masivo'
    )
    
    args = parser.parse_args()
    
    if args.masivo:
        probar_textos_modo_masivo()
    else:
        if args.nivel == 'todos':
            obtener_resumen_textos()
        else:
            textos = obtener_textos_por_nivel(args.nivel)
            print("\n" + "=" * 70)
            print(f"TEXTOS DE RIESGO {args.nivel.upper()}")
            print("=" * 70)
            for i, texto in enumerate(textos, 1):
                print(f"{i:2d}. {texto}")
