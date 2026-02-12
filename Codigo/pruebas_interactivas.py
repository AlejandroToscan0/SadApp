#!/usr/bin/env python3
"""
Script de prueba interactivo para el Sistema de Análisis de Riesgo Emocional.

Permite seleccionar y analizar textos de prueba de forma interactiva,
facilitando la demostración y validación del sistema.
"""

import sys
import os
from pathlib import Path

# Agregar el directorio actual al path para importar módulos locales
sys.path.insert(0, str(Path(__file__).parent))

from test_texts import obtener_todos_los_textos, obtener_resumen_textos
from main import ejecutar_analisis


def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('clear' if os.name != 'nt' else 'cls')


def mostrar_menu_principal():
    """Muestra el menú principal."""
    print("\n" + "=" * 70)
    print("HERRAMIENTA DE PRUEBA - SISTEMA DE ANÁLISIS DE RIESGO EMOCIONAL")
    print("=" * 70)
    print("\n1. Ver textos disponibles")
    print("2. Probar un texto específico")
    print("3. Probar todos los textos de un nivel")
    print("4. Prueba comparativa (todos los niveles)")
    print("5. Probar texto personalizado")
    print("6. Salir")
    print("\n" + "-" * 70)
    return input("Selecciona una opción (1-6): ").strip()


def mostrar_textos_disponibles():
    """Muestra todos los textos disponibles."""
    limpiar_pantalla()
    obtener_resumen_textos()
    input("\nPresiona ENTER para volver al menú...")


def probar_texto_especifico():
    """Permite seleccionar y probar un texto específico."""
    limpiar_pantalla()
    
    todos = obtener_todos_los_textos()
    
    print("\nSelecciona el nivel de riesgo:")
    print("1. BAJO")
    print("2. MODERADO")
    print("3. ALTO")
    print("4. CRÍTICO")
    
    opciones_nivel = {'1': 'bajo', '2': 'moderado', '3': 'alto', '4': 'critico'}
    opcion = input("\nOpción (1-4): ").strip()
    
    if opcion not in opciones_nivel:
        print("Opción no válida.")
        return
    
    nivel = opciones_nivel[opcion]
    textos = todos[nivel]
    
    print(f"\nTextos disponibles de riesgo {nivel.upper()}:")
    print("-" * 70)
    
    for i, texto in enumerate(textos, 1):
        preview = texto[:55] + "..." if len(texto) > 55 else texto
        print(f"{i:2d}. {preview}")
    
    try:
        seleccion = int(input(f"\nSelecciona un número (1-{len(textos)}): ").strip())
        if 1 <= seleccion <= len(textos):
            texto_seleccionado = textos[seleccion - 1]
            analizar_y_mostrar(texto_seleccionado, nivel)
        else:
            print("Número no válido.")
    except ValueError:
        print("Entrada no válida.")
    
    input("\nPresiona ENTER para volver al menú...")


def probar_todos_textos_nivel():
    """Prueba todos los textos de un nivel específico."""
    limpiar_pantalla()
    
    todos = obtener_todos_los_textos()
    
    print("\nSelecciona el nivel de riesgo a probar:")
    print("1. BAJO")
    print("2. MODERADO")
    print("3. ALTO")
    print("4. CRÍTICO")
    
    opciones_nivel = {'1': 'bajo', '2': 'moderado', '3': 'alto', '4': 'critico'}
    opcion = input("\nOpción (1-4): ").strip()
    
    if opcion not in opciones_nivel:
        print("Opción no válida.")
        return
    
    nivel = opciones_nivel[opcion]
    textos = todos[nivel]
    
    print(f"\n{'=' * 70}")
    print(f"ANALIZANDO {len(textos)} TEXTOS DE RIESGO {nivel.upper()}")
    print(f"{'=' * 70}\n")
    
    resultados_exitosos = 0
    resultados_error = 0
    
    for i, texto in enumerate(textos, 1):
        print(f"[{i:2d}/{len(textos)}] {texto[:50]}...")
        try:
            resultado = ejecutar_analisis(texto, 'linguistica')
            if resultado:
                resultados_exitosos += 1
                print(f"        Resultado: {resultado.get('nivel_riesgo', 'desconocido')} " +
                      f"(Score: {resultado.get('score', 0):.3f})")
            else:
                resultados_error += 1
                print("        Error: No se obtuvo resultado")
        except Exception as e:
            resultados_error += 1
            print(f"        Error: {str(e)[:50]}")
        print()
    
    print(f"{'=' * 70}")
    print(f"RESUMEN: {resultados_exitosos} exitosos, {resultados_error} errores")
    print(f"{'=' * 70}")
    
    input("\nPresiona ENTER para volver al menú...")


def prueba_comparativa():
    """Realiza una prueba comparativa con textos de todos los niveles."""
    limpiar_pantalla()
    
    todos = obtener_todos_los_textos()
    
    print("\n" + "=" * 70)
    print("PRUEBA COMPARATIVA - TODOS LOS NIVELES")
    print("=" * 70)
    
    resumen_total = {'bajo': {'exitosos': 0, 'errores': 0},
                     'moderado': {'exitosos': 0, 'errores': 0},
                     'alto': {'exitosos': 0, 'errores': 0},
                     'critico': {'exitosos': 0, 'errores': 0}}
    
    for nivel, textos in todos.items():
        print(f"\n{nivel.upper()} ({len(textos)} textos):")
        print("-" * 70)
        
        for i, texto in enumerate(textos, 1):
            preview = texto[:40] + "..." if len(texto) > 40 else texto
            sys.stdout.write(f"  [{i:2d}/{len(textos)}] {preview:<45}")
            sys.stdout.flush()
            
            try:
                resultado = ejecutar_analisis(texto, 'linguistica')
                if resultado:
                    resumen_total[nivel]['exitosos'] += 1
                    score = resultado.get('score', 0)
                    nivel_resultado = resultado.get('nivel_riesgo', '?')
                    print(f" [{nivel_resultado}: {score:.2f}]")
                else:
                    resumen_total[nivel]['errores'] += 1
                    print(" [ERROR]")
            except Exception as e:
                resumen_total[nivel]['errores'] += 1
                print(" [ERROR]")
    
    print("\n" + "=" * 70)
    print("RESUMEN GENERAL")
    print("=" * 70)
    
    total_exitosos = 0
    total_errores = 0
    
    for nivel, stats in resumen_total.items():
        exitosos = stats['exitosos']
        errores = stats['errores']
        total = exitosos + errores
        porcentaje = (exitosos / total * 100) if total > 0 else 0
        print(f"{nivel.upper():10s}: {exitosos:2d}/{total} exitosos ({porcentaje:5.1f}%)")
        total_exitosos += exitosos
        total_errores += errores
    
    print("-" * 70)
    total = total_exitosos + total_errores
    porcentaje_total = (total_exitosos / total * 100) if total > 0 else 0
    print(f"{'TOTAL':10s}: {total_exitosos:2d}/{total} exitosos ({porcentaje_total:5.1f}%)")
    print("=" * 70)
    
    input("\nPresiona ENTER para volver al menú...")


def probar_texto_personalizado():
    """Permite al usuario ingresar un texto personalizado para analizar."""
    limpiar_pantalla()
    
    print("\nIngresa el texto que deseas analizar:")
    print("-" * 70)
    print("(Escribe 'SALIR' en una línea para terminar)\n")
    
    lineas = []
    while True:
        linea = input()
        if linea.upper() == 'SALIR':
            break
        lineas.append(linea)
    
    texto = '\n'.join(lineas).strip()
    
    if texto:
        print("\n¿Qué estrategia deseas usar?")
        print("1. Lingüística (análisis de palabras clave)")
        print("2. Machine Learning (Naive Bayes)")
        
        opcion = input("\nOpción (1-2): ").strip()
        
        estrategia = 'linguistica' if opcion == '1' else 'ml'
        
        print("\nAnalizando...")
        analizar_y_mostrar(texto, None, estrategia)
    else:
        print("Texto vacío.")
    
    input("\nPresiona ENTER para volver al menú...")


def analizar_y_mostrar(texto, nivel=None, estrategia='linguistica'):
    """
    Realiza el análisis de un texto y muestra los resultados.
    
    Args:
        texto (str): Texto a analizar
        nivel (str): Nivel de riesgo esperado (para comparación)
        estrategia (str): Estrategia a usar ('linguistica' o 'ml')
    """
    print("\n" + "=" * 70)
    print("RESULTADO DEL ANÁLISIS")
    print("=" * 70)
    
    print(f"\nTexto: {texto[:60]}..." if len(texto) > 60 else f"\nTexto: {texto}")
    print(f"Estrategia: {estrategia}")
    
    if nivel:
        print(f"Nivel esperado: {nivel.upper()}")
    
    print("-" * 70)
    
    try:
        resultado = ejecutar_analisis(texto, estrategia)
        
        if resultado:
            print(f"\nNivel de Riesgo: {resultado.get('nivel_riesgo', 'Desconocido')}")
            print(f"Score: {resultado.get('score', 0):.4f}")
            
            if 'recomendacion' in resultado:
                print(f"\nRecomendación:")
                print(f"  {resultado['recomendacion']}")
            
            if 'recursos' in resultado:
                print(f"\nRecursos:")
                for recurso in resultado['recursos']:
                    print(f"  - {recurso}")
        else:
            print("No se pudo obtener resultado del análisis.")
    
    except Exception as e:
        print(f"Error durante el análisis: {str(e)}")
    
    print("=" * 70)


def main():
    """Función principal del programa."""
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == '1':
            mostrar_textos_disponibles()
        elif opcion == '2':
            probar_texto_especifico()
        elif opcion == '3':
            probar_todos_textos_nivel()
        elif opcion == '4':
            prueba_comparativa()
        elif opcion == '5':
            probar_texto_personalizado()
        elif opcion == '6':
            print("\n¡Gracias por usar la herramienta de prueba!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        sys.exit(0)
