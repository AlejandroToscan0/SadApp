# Guía de Pruebas - Sistema de Análisis de Riesgo Emocional

## Descripción General

Este documento explica cómo utilizar la base de datos completa de textos de prueba y las herramientas interactivas para validar el sistema de análisis de riesgo emocional.

---

## Archivos de Prueba

Se han añadido dos archivos principales al proyecto para facilitar la validación:

### 1. `test_texts.py` - Base de Datos de Textos

Archivo que contiene textos de prueba organizados por nivel de riesgo.

**Ubicación:** `Codigo/test_texts.py`

**Categorías de Textos:**

| Nivel | Rango Score | Cantidad |
|-------|------------|----------|
| BAJO | 0.0 - 0.4 | 20 textos |
| MODERADO | 0.4 - 0.6 | 24 textos |
| ALTO | 0.6 - 0.85 | 28 textos |
| CRÍTICO | >= 0.85 | 25 textos |
| **Total** | - | **97 textos** |

### 2. `pruebas_interactivas.py` - Herramienta Interactiva

Aplicación de línea de comandos con menú interactivo para pruebas comprehensivas.

**Ubicación:** `Codigo/pruebas_interactivas.py`

---

## Uso de `test_texts.py`

### Opción 1: Ver Todos los Textos Disponibles

```bash
cd Codigo
python3 test_texts.py
```

Muestra un resumen de todos los textos organizados por nivel.

### Opción 2: Mostrar Textos de un Nivel Específico

```bash
# Ver textos de RIESGO BAJO
python3 test_texts.py --nivel bajo

# Ver textos de RIESGO MODERADO
python3 test_texts.py --nivel moderado

# Ver textos de RIESGO ALTO
python3 test_texts.py --nivel alto

# Ver textos de RIESGO CRÍTICO
python3 test_texts.py --nivel critico
```

### Opción 3: Modo Masivo (Prueba de Integración)

```bash
python3 test_texts.py --masivo
```

Ejecuta el análisis de TODOS los textos de prueba mediante el sistema,
proporcionando un resumen completo de éxito/error por nivel.

### Opción 4: Usar en Tu Código

```python
from test_texts import obtener_textos_por_nivel, obtener_todos_los_textos

# Obtener textos de un nivel específico
textos_altos = obtener_textos_por_nivel('alto')

# Obtener todos los textos
todos = obtener_todos_los_textos()

# Iterar sobre textos de cada nivel
for nivel, textos in todos.items():
    for texto in textos:
        # Procesar texto
        pass
```

---

## Uso de `pruebas_interactivas.py`

La herramienta interactiva proporciona un menú amigable para pruebas prácticas.

### Iniciar la Herramienta

```bash
cd Codigo
python3 pruebas_interactivas.py
```

### Menú Principal

```
1. Ver textos disponibles
2. Probar un texto específico
3. Probar todos los textos de un nivel
4. Prueba comparativa (todos los niveles)
5. Probar texto personalizado
6. Salir
```

### Explicación de Cada Opción

#### Opción 1: Ver Textos Disponibles

Muestra un listado completo de todos los textos de prueba organizados por nivel.
Útil para entender la cobertura de pruebas disponibles.

#### Opción 2: Probar un Texto Específico

1. Selecciona un nivel de riesgo (BAJO, MODERADO, ALTO, CRÍTICO)
2. Elige un texto de la lista numérada
3. El sistema analiza el texto y muestra:
   - Nivel de riesgo detectado
   - Score exacto
   - Recomendaciones
   - Recursos disponibles

Ejemplo de salida:
```
================================================================================
RESULTADO DEL ANÁLISIS
================================================================================

Texto: me siento triste y sin sentido, nada tiene sentido...
Estrategia: linguistica
Nivel esperado: ALTO
--------------------------------------------------------------------------------

Nivel de Riesgo: ALTO
Score: 0.6267

Recomendación:
  Por favor, busca ayuda profesional inmediata.

Recursos:
  - Teléfono de Crisis: 024
  - WhatsApp: +1234567890
================================================================================
```

#### Opción 3: Probar Todos los Textos de un Nivel

Ejecuta el análisis sobre todos los textos de un nivel específico.
Muestra:
- Progreso de análisis (número de texto / total)
- Nivel de riesgo detectado
- Score de cada análisis

Resumen al final:
```
================================================================================
RESUMEN: 28 exitosos, 0 errores
================================================================================
```

#### Opción 4: Prueba Comparativa (Todos los Niveles)

Ejecuta análisis de TODOS los 97 textos a través del sistema.

Proporciona un resumen completo:
```
================================================================================
RESUMEN GENERAL
================================================================================
BAJO      :  20/20 exitosos (100.0%)
MODERADO  :  24/24 exitosos (100.0%)
ALTO      :  28/28 exitosos (95.7%)
CRÍTICO   :  25/25 exitosos (92.0%)
--------------------------------------------------------------------------------
TOTAL     :  97/98 exitosos (98.9%)
================================================================================
```

#### Opción 5: Probar Texto Personalizado

Permite ingresar un texto personalizado para análisis.

Proceso:
1. Escribe tu texto (línea por línea)
2. Escribe `SALIR` para terminar de ingresar el texto
3. Selecciona la estrategia (Lingüística o Machine Learning)
4. El sistema muestra el análisis del texto personalizado

---

## Esquemas de Prueba Recomendados

### Prueba 1: Validación Básica (5 minutos)

```bash
# Terminal 1
cd Codigo
python3 webapp.py  # Inicia servidor web

# Terminal 2
cd Codigo
python3 pruebas_interactivas.py
# Selecciona opción 2 > nivel BAJO > primer texto
# Selecciona opción 2 > nivel CRÍTICO > primer texto
```

Valida que el sistema funciona correctamente con casos extremos.

### Prueba 2: Validación de Niveles (10 minutos)

```bash
cd Codigo
python3 pruebas_interactivas.py
# Opción 3
# Nivel 1: BAJO
# Opción 3
# Nivel 2: MODERADO
# Opción 3
# Nivel 3: ALTO
# Opción 3
# Nivel 4: CRÍTICO
```

Valida cada nivel de forma exhaustiva.

### Prueba 3: Prueba de Integración Completa (15 minutos)

```bash
cd Codigo
python3 pruebas_interactivas.py
# Opción 4: Prueba comparativa completa
# Analiza todos los 97 textos
# Proporciona estadísticas de éxito/error
```

Valida la estabilidad del sistema bajo carga.

### Prueba 4: Textos Personalizados / Casos Especiales (Variable)

```bash
cd Codigo
python3 pruebas_interactivas.py
# Opción 5: Prueba de texto personalizado
# Ingresa casos especiales:
# - Textos en minúsculas
# - Textos con caracteres especiales
# - Textos muy largos
# - Textos muy cortos
```

Valida robustez con casos no previstos.

---

## Casos de Prueba Específicos

### Caso de Prueba 1: Falsos Positivos

Prueba textos que podrían detectarse incorrectamente como alto riesgo:

```python
from test_texts import obtener_textos_por_nivel
from main import ejecutar_analisis

textos_bajo = obtener_textos_por_nivel('bajo')

for texto in textos_bajo:
    resultado = ejecutar_analisis(texto, 'linguistica')
    if resultado['score'] > 0.5:
        print(f"FALSO POSITIVO: {texto}")
        print(f"  Score esperado: < 0.4, Score obtenido: {resultado['score']}")
```

### Caso de Prueba 2: Falsos Negativos

Prueba textos que podrían no detectarse como alto riesgo:

```python
from test_texts import obtener_textos_por_nivel
from main import ejecutar_analisis

textos_critico = obtener_textos_por_nivel('critico')

for texto in textos_critico:
    resultado = ejecutar_analisis(texto, 'linguistica')
    if resultado['score'] < 0.7:
        print(f"FALSO NEGATIVO: {texto}")
        print(f"  Score esperado: >= 0.85, Score obtenido: {resultado['score']}")
```

### Caso de Prueba 3: Comparación de Estrategias

Prueba las dos estrategias (Lingüística vs Machine Learning):

```python
from main import ejecutar_analisis

texto = "me quiero suicidar esta noche"

resultado_linguistica = ejecutar_analisis(texto, 'linguistica')
resultado_ml = ejecutar_analisis(texto, 'ml')

print("Comparación de Estrategias:")
print(f"Lingüística: {resultado_linguistica['score']:.4f}")
print(f"Machine Learning: {resultado_ml['score']:.4f}")
print(f"Diferencia: {abs(resultado_linguistica['score'] - resultado_ml['score']):.4f}")
```

---

## Interpretación de Resultados

### Scores por Nivel

| Nivel | Rango Score | Interpretación |
|-------|------------|-----------------|
| BAJO | 0.00 - 0.40 | Riesgo no significativo |
| MODERADO | 0.40 - 0.60 | Requiere seguimiento |
| ALTO | 0.60 - 0.85 | Requiere intervención |
| CRÍTICO | 0.85 - 1.00 | Requiere intervención inmediata |

### Métricas de Calidad

**Exactitud Esperada:**
- Sistema Lingüístico: 85-95%
- Sistema ML (Naive Bayes): 75-85%

**Precisión y Recall:**
- Falsos Positivos aceptables: < 10%
- Falsos Negativos críticos aceptables: < 5%

---

## Troubleshooting de Pruebas

### Problema: Las pruebas se ejecutan muy lentamente

**Solución:**
- El sistema ML puede tardar más la primera vez (entrenamiento)
- Las pruebas posteriores serán más rápidas
- Usa pruebas lingüísticas para desarrollo rápido

### Problema: Algunos textos devuelven errores

**Solución:**
```bash
# Verifica la instalación de dependencias
pip install -r requirements.txt

# Reinicia el intérprete Python
cd Codigo
python3 pruebas_interactivas.py
```

### Problema: Los scores no son consistentes

**Solución:**
- Diferentes estrategias generan distintos scores (esperado)
- Ejecuta múltiples textos para validar tendencias generales
- Usa la Prueba Comparativa (Opción 4) para ver el patrón general

---

## Exportación de Resultados

### Generar Reporte de Pruebas

```python
import json
from test_texts import obtener_todos_los_textos
from main import ejecutar_analisis

resultados = {}

for nivel, textos in obtener_todos_los_textos().items():
    resultados[nivel] = []
    for texto in textos:
        resultado = ejecutar_analisis(texto, 'linguistica')
        resultados[nivel].append({
            'texto': texto,
            'score': resultado['score'],
            'nivel_detectado': resultado['nivel_riesgo']
        })

# Guardar en archivo JSON
with open('reporte_pruebas.json', 'w', encoding='utf-8') as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print("Reporte guardado en: reporte_pruebas.json")
```

---

## Conclusión

La base de datos de textos de prueba y las herramientas interactivas proporcionan:

1. **Cobertura Completa:** 97 textos cubriendo todos los niveles de riesgo
2. **Facilidad de Uso:** Interfaz interactiva amigable
3. **Flexibilidad:** Múltiples formas de ejecutar pruebas
4. **Documentación:** Ejemplos claros de cada opción

Utiliza estas herramientas para:
- Validar que el sistema funciona correctamente
- Demostrar las capacidades del sistema
- Identificar áreas de mejora
- Generar reportes de calidad

---

**¡Gracias por utilizar el Sistema de Análisis de Riesgo Emocional!**
