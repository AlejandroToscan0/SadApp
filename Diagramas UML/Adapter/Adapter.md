# 🔌 Patrón ADAPTER - Diagrama UML

## Descripción General

El patrón **Adapter** permite que interfaces incompatibles trabajen juntas mediante un adaptador que convierte la interfaz de una clase en otra que el cliente espera.

### 📍 Ubicación en el Proyecto
- **Archivo**: `Codigo/core/adapters/AdaptadorProcesador.py`
- **Propósito**: Unificar la salida heterogénea de procesadores

---

## 🎯 Problema Resuelto

Tenemos dos procesadores que retornan formatos DIFERENTES:

```
ProcesadorPalabrasClave  →  dict {"negatividad": 0.9, ...}
ProcesadorVectorial      →  list [0.1, 0.5, 0.9, 0.0]
```

El analizador espera siempre un formato consistente. **¡Solución: Adapter!**

---

## 📊 Diagrama UML Detallado

```
┌────────────────────────────────────────────────────────────────┐
│                    TARGET (Esperado)                           │
├────────────────────────────────────────────────────────────────┤
│              ProcesadorTexto (Interface)                        │
├────────────────────────────────────────────────────────────────┤
│ + procesar(texto: str) -> dict                                 │
└────────────┬─────────────────────────────────────────┬─────────┘
             │                                         │
             │ implementa                implementa     │
             │                                         │
   ┌─────────▼──────────────┐         ┌───────────────▼────────┐
   │ ProcesadorPalabrasClave │        │  ProcesadorVectorial   │
   ├────────────────────────┤         ├────────────────────────┤
   │ + procesar() -> dict   │         │ + procesar() -> list   │
   │   retorna:             │         │   retorna:             │
   │   {                    │         │   [0.1, 0.5, 0.9, 0.0]│
   │     "negatividad": 0.9 │         │                        │
   │     "peligro": ...     │         │ ❌ Formato incompatible │
   │   }                    │         └────────────────────────┘
   └────────────────────────┘

                            ADAPTER (Solución)
                            ✨ AdaptadorProcesador ✨
                        
    ┌──────────────────────────────────────────────────┐
    │         AdaptadorProcesador                      │
    ├──────────────────────────────────────────────────┤
    │ - procesador: ProcesadorTexto                    │
    ├──────────────────────────────────────────────────┤
    │ + __init__(procesador)                           │
    │ + procesar(texto: str) -> dict                   │
    │ - _adaptar_resultado(resultado)                  │
    │ - _normalizar_vector(vector: list) -> dict       │
    ├──────────────────────────────────────────────────┤
    │ Retorna SIEMPRE:                                 │
    │ {                                                │
    │   "tipo_procesador": str,                        │
    │   "datos_originales": any,                       │
    │   "features": dict,  ← FORMATO UNIFICADO        │
    │   "metadata": dict                               │
    │ }                                                │
    └───────────────────┬─────────────────────────────┘
                        │
            uses/adapts │
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
    ┌─────────────┐            ┌─────────────┐
    │   dict      │            │    list     │
    │  format     │            │  format     │
    └─────────────┘            └─────────────┘
         │                             │
         └──────────────┬──────────────┘
                        │
            ✅ Ambos adaptan a ✅
                        │
                        ▼
            ┌─────────────────────┐
            │   Formato UNI-      │
            │   FICADO: dict      │
            │  con "features"     │
            └─────────────────────┘
```

---

## 🔄 Flujo de Colaboración

```
                    Cliente
                       │
                       │ usa
                       ▼
              ┌─────────────────────┐
              │ AdministradorAnalisis │
              │ Texto (Singleton)     │
              └──────────┬────────────┘
                         │
                    obtiene │
                         │
                  ┌──────▼──────────┐
                  │ AdaptadorProcesa │
                  │ dor              │
                  └──────┬───────────┘
                         │
                  wrappea │
                         │
         ┌───────────────┴────────────────┐
         │                                │
         ▼                                ▼
  ┌────────────────┐         ┌──────────────────┐
  │ Procesador     │         │ Procesador       │
  │ PalabrasClave  │         │ Vectorial        │
  │ (dict output)  │         │ (list output)    │
  └────────────────┘         └──────────────────┘
         │                                │
         └───────────────┬────────────────┘
                         │
                    adapta a │
                         │
                         ▼
                  ┌────────────────────┐
                  │ Formato Estándar:  │
                  │  {                 │
                  │    "features": {   │
                  │      "negatividad" │
                  │      "peligro"     │
                  │    }               │
                  │  }                 │
                  └────────┬───────────┘
                           │
                      usa  │
                           ▼
                    ┌────────────────┐
                    │ Analizador     │
                    │ Riesgo (ABC)   │
                    └────────────────┘
```

---

## 💻 Ejemplo de Código

### **Uso Básico**

```python
# Sin Adapter (problemático)
procesador = ProcesadorPalabrasClave()
resultado = procesador.procesar("texto")  # retorna dict
# ↑ Cliente necesita saber qué tipo retorna

# Con Adapter (solución)
procesador_base = ProcesadorVectorial()
adaptador = AdaptadorProcesador(procesador_base)
resultado_adaptado = adaptador.procesar("texto")
# ↑ Siempre retorna formato consistente
features = resultado_adaptado["features"]  # ✅ seguro
```

### **Integración en Singleton**

```python
class AdministradorAnalisisTexto:
    def __init__(self, factory):
        self.procesador_base = factory.crear_procesador()
        # ✨ Wrappear con Adapter
        self.procesador = AdaptadorProcesador(self.procesador_base)
    
    def analizar(self, texto):
        # Siempre obtiene formato unificado
        datos_adaptados = self.procesador.procesar(texto)
        features = datos_adaptados["features"]  # dict garantizado
        return self.analizador.evaluar_riesgo(features)
```

---

## 🎯 Beneficios Alcanzados

| Beneficio | Descripción |
|-----------|-------------|
| ✅ **Reutilización** | Ambos procesadores reutilizados sin cambios |
| ✅ **Desacoplamiento** | Analizador no conoce formato original |
| ✅ **Flexibilidad** | Agregar nuevo procesador solo requiere adaptarlo |
| ✅ **Mantenibilidad** | Cambios en procesadores no afectan analizador |
| ✅ **Consistencia** | Garantiza formato uniforme siempre |

---

## 🔌 Variantes en el Proyecto

### **Adaptando dict → Formato Unificado**

```python
# ProcesadorPalabrasClave retorna:
{
    "negatividad": 0.9,
    "primera_persona": 0.5,
    "desesperanza": 0.8,
    "danger": False
}

# Adapter convierte a:
{
    "tipo_procesador": "PalabrasClave",
    "datos_originales": {...},
    "features": {...},  # ← uso del analizador
    "metadata": {...}
}
```

### **Adaptando list → Formato Unificado**

```python
# ProcesadorVectorial retorna:
[0.1, 0.5, 0.9, 0.0]

# Adapter convierte a:
{
    "tipo_procesador": "Vectorial",
    "datos_originales": [0.1, 0.5, 0.9, 0.0],
    "features": {  # ← normalizado
        "negatividad": 0.1,
        "primera_persona": 0.5,
        "desesperanza": 0.9,
        "peligro": 0.0
    },
    "metadata": {...}
}
```

---

## 📝 Implementación Paso a Paso

```python
class AdaptadorProcesador:
    # 1️⃣ Constructor: Recibe objeto a adaptar
    def __init__(self, procesador):
        self.procesador = procesador
    
    # 2️⃣ Interfaz pública: misma que esperan clientes
    def procesar(self, texto: str) -> dict:
        resultado_original = self.procesador.procesar(texto)
        return self._adaptar_resultado(resultado_original)
    
    # 3️⃣ Lógica de conversión
    def _adaptar_resultado(self, resultado_original):
        if isinstance(resultado_original, dict):
            # Caso 1: dict → unificado
            return self._adaptar_dict(resultado_original)
        elif isinstance(resultado_original, list):
            # Caso 2: list → unificado
            return self._adaptar_list(resultado_original)
    
    # 4️⃣ Normalización de vectores
    def _normalizar_vector(self, vector: list) -> dict:
        # [0.1, 0.5, 0.9, 0.0] → {"negatividad": 0.1, ...}
        return {
            "negatividad": vector[0],
            "primera_persona": vector[1],
            "desesperanza": vector[2],
            "peligro": vector[3]
        }
```

---

## 🧪 Caso de Uso Real

### **Escenario: Agregar Nuevo Procesador**

**Antes (sin Adapter):**
```python
# ❌ Problema: Analizador necesita conocer todos los tipos
if isinstance(datos, dict):
    features = datos
elif isinstance(datos, ndarray):
    features = ndarray_to_dict(datos)
elif isinstance(datos, list):
    features = list_to_dict(datos)
# ❌ Alto acoplamiento
```

**Ahora (con Adapter):**
```python
# ✅ Solución: Siempre formato consistente
nuevo_procesador = NuevoProcesador()
adaptador = AdaptadorProcesador(nuevo_procesador)
datos_adaptados = adaptador.procesar(texto)
features = datos_adaptados["features"]  # ✅ siempre funciona
```

---

## 📚 Referencias

- **Patrón**: Adapter (Structural Design Pattern)
- **GoF Book**: "Design Patterns: Elements of Reusable Object-Oriented Software"
- **Propósito**: Convertir interfaz de una clase en otra esperada
- **Sinónimos**: Wrapper

---

## ✅ Checklist de Implementación

- [x] Interfaz consistente (`procesar(texto) -> dict`)
- [x] Wrappea procesadores heterogéneos
- [x] Normaliza formatos
- [x] No modifica clases originales
- [x] Permite agregar nuevos procesadores fácilmente
- [x] Integrado en Singleton
- [x] Documentado y comentado

---

**Diagrama creado**: 12 de febrero de 2026
**Proyecto**: Sistema de Análisis de Riesgo Emocional
**Patrón**: Adapter (Structural)
