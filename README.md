# Sistema de Análisis de Riesgo Emocional

Aplicación educativa que implementa 6 patrones de diseño del Gang of Four para analizar textos y determinar niveles de riesgo emocional.

---

## Descripción General

Este proyecto demuestra la implementación de patrones de diseño en un contexto real: un sistema de análisis de salud mental que:

- Analiza textos en español con múltiples estrategias
- Detecta niveles de riesgo emocional (BAJO, MODERADO, ALTO, CRÍTICO)
- Genera recomendaciones personalizadas basadas en el nivel de riesgo
- Proporciona interfaz web intuitiva e interactiva
- Soporta intercambio dinámico de estrategias de análisis

### Tecnologías Utilizadas

| Componente | Tecnología |
|-----------|-----------|
| Backend | Python 3.8+ |
| Framework Web | Flask |
| Análisis de Texto | Procesamiento de palabras clave + Naive Bayes |
| Interfaz | HTML5 + CSS3 |
| Gestión de Dependencias | pip (requirements.txt) |

---

## Arquitectura y Patrones de Diseño

### Seis Patrones de Diseño Integrados

#### PATRONES CREACIONALES (3)

| Patrón | Ubicación | Descripción |
|--------|-----------|-------------|
| **Singleton** | `core/singleton.py` | Garantiza una única instancia centralizada del administrador de análisis |
| **Abstract Factory** | `fabricas/` | Define familias relacionadas de procesadores y analizadores compatibles |
| **Factory Method** | `resource/GeneradorRecomendaciones.py` | Crea recomendaciones específicas basadas en el contexto (nivel de riesgo) |

#### PATRONES ESTRUCTURALES (1)

| Patrón | Ubicación | Descripción |
|--------|-----------|-------------|
| **Adapter** | `core/adapters/AdaptadorProcesador.py` | Unifica formatos heterogéneos de salida de diferentes procesadores |

#### PATRONES DE COMPORTAMIENTO (2)

| Patrón | Ubicación | Descripción |
|--------|-----------|-------------|
| **Strategy** | `productos/` | Permite intercambiar algoritmos de análisis sin cambiar el cliente |
| **Observer** | `core/observers/` | Notifica observadores de eventos importantes en tiempo real |

---

## Estructura del Proyecto

```
ProyectoAnalisis/
├── Codigo/
│   ├── __init__.py
│   ├── main.py (Interfaz CLI)
│   ├── webapp.py (Servidor Flask)
│   ├── test_texts.py (Base de datos de textos de prueba)
│   ├── pruebas_interactivas.py (Herramienta interactiva)
│   │
│   ├── core/
│   │   ├── singleton.py (Patrón Singleton + Adapter + Observer)
│   │   ├── adapters/
│   │   │   └── AdaptadorProcesador.py
│   │   ├── observers/
│   │   │   ├── ObservadorAnalisis.py (Interfaz base)
│   │   │   ├── GestorObservadores.py (Gestor de observadores)
│   │   │   ├── LoggerAnalisis.py (Logger de análisis)
│   │   │   └── AlertaRiesgoAlto.py (Alertas de riesgo alto)
│   │   └── interfaces/
│   │       ├── AnalizadorRiesgo.py
│   │       ├── ProcesadorTexto.py
│   │       └── Recomendacion.py
│   │
│   ├── fabricas/ (Abstract Factory + Factory Method)
│   │   ├── FabricaLinguistica.py
│   │   ├── FabricaMachineLearning.py
│   │   ├── RecomendacionRiesgoAltoFactory.py
│   │   ├── RecomendacionRiesgoBajoFactory.py
│   │   └── RecomendacionRiesgoModeradoFactory.py
│   │
│   ├── productos/ (Strategy Pattern)
│   │   ├── analizadores/
│   │   │   ├── AnalizadorPuntajePonderado.py
│   │   │   └── ClasificadorNaiveBayes.py
│   │   ├── procesadores/
│   │   │   ├── ProcesadorPalabrasClave.py
│   │   │   └── ProcesadorVectorial.py
│   │   └── recomendaciones/
│   │       ├── RecomendacionRiesgoAlto.py
│   │       ├── RecomendacionRiesgoBajo.py
│   │       └── RecomendacionRiesgoModerado.py
│   │
│   ├── resource/
│   │   └── GeneradorRecomendaciones.py
│   │
│   └── templates/
│       └── index.html
│
├── Diagramas\ UML/
│   ├── Singleton/
│   │   └── Singleton.mdj
│   ├── Abstract\ Factory/
│   │   └── Abstract\ Factory.mdj
│   ├── Factory\ Method/
│   │   └── Factory\ Method.mdj
│   ├── Adapter/
│   │   └── Adapter.puml (PlantUML - Patrón Adapter)
│   └── Observer/
│       └── Observer.puml (PlantUML - Patrón Observer)
│
├── GUIA_PRUEBAS.md (Guía completa de uso de herramientas de prueba)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)

### Pasos de Instalación

1. **Clona el repositorio o navega al proyecto:**
   ```bash
   cd /ruta/del/proyecto
   ```

2. **Crea un entorno virtual:**
   ```bash
   python3 -m venv venv
   ```

3. **Activa el entorno virtual:**
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución

### Opción 1: Interfaz Web (Recomendada)

```bash
cd Codigo
python3 webapp.py
```

Luego abre tu navegador en: `http://127.0.0.1:5001`

Características:
- Interfaz visual intuitiva
- Soporta ambas estrategias (Lingüística y ML)
- Muestra alertas en tiempo real
- Coloring dinámico del score según nivel de riesgo

### Opción 2: Interfaz CLI (Línea de Comandos)

```bash
cd Codigo
python3 main.py
```

Opciones disponibles:
```bash
# Análisis interactivo
python3 main.py

# Con texto directo
python3 main.py --text "me siento triste" --strategy linguistica

# Usar estrategia Machine Learning
python3 main.py --text "no quiero vivir" --strategy ml

# Ver ayuda
python3 main.py --help
```

### Opción 3: Herramienta Interactiva de Pruebas

```bash
cd Codigo
python3 pruebas_interactivas.py
```

Menú interactivo con opciones para:
- Ver textos disponibles
- Probar textos específicos
- Ejecutar pruebas por nivel
- Prueba comparativa completa
- Analizar textos personalizados

---

## Flujo de la Aplicación

```
ENTRADA DE TEXTO
        |
        v
   SINGLETON PATTERN
   (Administrador único)
        |
        v
   ABSTRACT FACTORY
   (Selecciona estrategia)
        |
        v
   ADAPTER PATTERN
   (Unifica formatos)
        |
        v
   STRATEGY PATTERN
   (Procesa y analiza)
        |
        v
   FACTORY METHOD
   (Genera recomendaciones)
        |
        v
   OBSERVER PATTERN
   (Notifica eventos)
        |
        v
   SALIDA: Resultado Análisis
   (Score, nivel, recomendación, recursos)
```

---

## Diferencias de Score por Estrategia

El sistema soporta dos estrategias de análisis:

### Estrategia Lingüística

- Análisis basado en palabras clave
- Puntaje ponderado por importancia
- Rápido de ejecutar
- Fácil de entender

### Estrategia Machine Learning

- Análisis usando Naive Bayes
- Clasificación probabilística
- Puede ser más preciso con datos
- Requiere mayor tiempo de procesamiento

---

## Textos de Prueba Disponibles

Se incluyen 97 textos de prueba disponibles en `test_texts.py`:

- BAJO (0.0 - 0.4): 20 textos
- MODERADO (0.4 - 0.6): 24 textos
- ALTO (0.6 - 0.85): 28 textos
- CRÍTICO (≥ 0.85): 25 textos

Para usar los textos de prueba:

```bash
# Ver todos los textos
python3 test_texts.py

# Ver textos de un nivel
python3 test_texts.py --nivel alto

# Ejecutar pruebas masivas
python3 test_texts.py --masivo
```

Consulta `GUIA_PRUEBAS.md` para más detalles.

---

## Patrones de Diseño - Análisis Profundo

### 1. SINGLETON

**Propósito:** Garantizar una única instancia del administrador

**Ubicación:** `core/singleton.py`

**Características:**
- Una única instancia en toda la aplicación
- Compartir estado global de forma segura
- Sincronización entre componentes

**Uso:**
```python
manager = AdministradorAnalisisTexto.get_instancia()
resultado = manager.analizar("texto")
```

---

### 2. ABSTRACT FACTORY

**Propósito:** Crear familias de objetos relacionados

**Ubicación:** `fabricas/`

**Componentes:**
- FabricaLinguistica (crea procesador y analizador lingüístico)
- FabricaMachineLearning (crea procesador y analizador ML)

**Características:**
- Intercambio de estrategias completas
- Desacoplamiento de creación
- Garantiza familias compatibles

---

### 3. FACTORY METHOD

**Propósito:** Crear objetos basados en contexto

**Ubicación:** `resource/GeneradorRecomendaciones.py`

**Decisiones basadas en:**
- Nivel de riesgo detectado
- Contexto del análisis

**Genera:**
- RecomendacionRiesgoAlto
- RecomendacionRiesgoModerado
- RecomendacionRiesgoBajo

---

### 4. ADAPTER (ESTRUCTURAL)

**Propósito:** Unificar interfaces heterogéneas

**Ubicación:** `core/adapters/AdaptadorProcesador.py`

**Problema que resuelve:**

El sistema utiliza dos procesadores que retornan formatos incompatibles:
- `ProcesadorPalabrasClave` → retorna `dict` {"negatividad": 0.9, ...}
- `ProcesadorVectorial` → retorna `list` [0.1, 0.5, 0.9, 0.0]

El analizador de riesgo espera siempre un formato consistente, creando acoplamiento.

**Solución Implementada:**

El **AdaptadorProcesador** envuelve cualquier procesador y:
1. Normaliza la salida a formato estándar dict
2. Mantiene metadatos del procesador original
3. Proporciona interfaz uniforme: `procesar(texto: str) -> dict`

```python
# Retorna formato unificado:
{
    "tipo_procesador": "Vectorial",
    "datos_originales": [0.1, 0.5, 0.9, 0.0],
    "features": {  # ← FORMATO CONSISTENTE
        "negatividad": 0.1,
        "primera_persona": 0.5,
        "desesperanza": 0.9,
        "peligro": 0.0
    },
    "metadata": {...}
}
```

**Beneficios alcanzados:**
- Reutilización sin cambios de procesadores existentes
- Desacoplamiento entre procesadores y analizador
- Fácil agregar nuevos procesadores
- Cambios en procesadores no afectan el analizador

**Diagrama:** [Diagramas UML/Adapter/](Diagramas%20UML/Adapter/) (Adapter.puml)

---

### 5. STRATEGY

**Propósito:** Intercambiar algoritmos en tiempo de ejecución

**Ubicación:** `productos/`

**Estrategias disponibles:**
- Lingüística (palabras clave)
- Machine Learning (Naive Bayes)

**Ventaja:**
- No requiere cambios en el cliente
- Fácil agregar nuevas estrategias

---

### 6. OBSERVER (COMPORTAMIENTO)

**Propósito:** Notificar múltiples objetos de cambios sin acoplamiento

**Ubicación:** `core/observers/`

**Problema que resuelve:**

Sin Observer, el Singleton tendría que conocer y llamar explícitamente a cada componente:
```python
# ❌ Acoplamiento fuerte
def analizar(texto):
    resultado = self._procesar(texto)
    logger.registrar(resultado)      # Conoce logger
    if "ALTO" in resultado:          # Conoce alertas
        alerta.enviar(resultado)
    # ¿Y si queremos agregar más observadores?
```

**Solución Implementada:**

El **GestorObservadores** desacopla completamente la comunicación:

```python
# ✅ Desacoplamiento completo
def analizar(texto):
    resultado = self._procesar(texto)
    self.gestor_observadores.notificar("analisis_completado", resultado)
    # El Singleton NO sabe quién escucha
```

**Observadores implementados:**

1. **LoggerAnalisis**: Registra todos los análisis completados
   - Timestamp automático
   - Información de score y nivel de riesgo

2. **AlertaRiesgoAlto**: Emite alertas visuales cuando detecta riesgo alto
   - Alerta inmediata al detectar nivel ALTO
   - Proporciona recomendaciones urgentes

3. **ObservadorPersonalizado**: Interfaz base para crear observadores propios

**Flujo de notificación:**

```
usuario ingresa texto
         ↓
   admin.analizar()
    [procesamiento]
    [análisis]
         ↓
  gestor_observadores.notificar()
         ↓
    ┌────┴────┐
    ↓         ↓
 Logger   AlertaAlto
    ↓         ↓
[Registra] [Alerta visual]
```

**Interfaz Observer:**

```python
class ObservadorAnalisis(ABC):
    @abstractmethod
    def actualizar(self, evento: str, resultado: dict) -> None:
        """Se llama cuando ocurre un evento."""
        pass
```

**Uso: Agregar Nuevo Observador**

```python
class MiObservador(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        if evento == "analisis_completado":
            # Tu lógica personalizada
            print(f"Riesgo: {resultado['nivel']}")

# Registrar
observador = MiObservador()
manager = AdministradorAnalisisTexto.get_instancia()
manager.registrar_observador(observador)
```

**Beneficios alcanzados:**
- Desacoplamiento total
- Fácil agregar/remover observadores en tiempo de ejecución
- Comunicación push automática
- Aislamiento de responsabilidades

**Diagrama:** [Diagramas UML/Observer/](Diagramas%20UML/Observer/) (Observer.puml)

---

## Desarrollo y Extensiones

### Agregar Nueva Estrategia

1. Crear procesador en `productos/procesadores/`
2. Crear analizador en `productos/analizadores/`
3. Crear fábrica en `fabricas/`
4. Registrar en factory registry

### Agregar Nuevo Observador

1. Heredar de `ObservadorAnalisis`
2. Implementar `actualizar(evento, resultado)`
3. Registrar en main.py:

```python
observador = MiObservador()
manager = AdministradorAnalisisTexto.get_instancia()
manager.registrar_observador(observador)
```

---

## Diagramas UML

Los diagramas están disponibles en la carpeta `Diagramas UML/`:

### Patrones Existentes
- `Diagramas UML/Singleton/` - Singleton.mdj
- `Diagramas UML/Abstract Factory/` - Abstract Factory.mdj
- `Diagramas UML/Factory Method/` - Factory Method.mdj

### Patrones Nuevos
- `Diagramas UML/Adapter/Adapter.puml` - Diagrama PlantUML del Adapter
- `Diagramas UML/Observer/Observer.puml` - Diagrama PlantUML del Observer

**Para ver los diagramas PlantUML:**
- Usar VS Code con extensión PlantUML
- Herramientas online como plantuml.com
- Generar PNG con: `plantuml -Tpng Adapter.puml`

---

## Solución de Problemas

### El puerto 5001 está en uso

Si el puerto 5001 también está ocupado, puedes cambiar el puerto configurando la variable de entorno:

macOS/Linux:
```bash
PORT=8000 python3 webapp.py
```

O si necesitas liberar el puerto 5001:
```bash
lsof -i :5001
kill -9 <PID>
```

### Módulo no encontrado

```bash
# Asegúrate de estar en el directorio Codigo/
cd Codigo

# Verifica que el entorno está activado
source ../venv/bin/activate  # macOS/Linux
```

### Dependencias desactualizadas

```bash
pip install --upgrade -r requirements.txt
```

---

## Información Importante

AVISO: Este proyecto es EDUCATIVO. No debe usarse para:
- Diagnósticos clínicos reales
- Reemplazo de atención profesional
- Decisiones de salud mental críticas

Para emergencias de salud mental, contacta:
- Ambulancia: 911
- Línea de Crisis: 024 (España)
- Crisis Text Line (USA)

---

## Licencia

Este proyecto se proporciona con fines educativos.

---

## Autor

Equipo de Desarrollo: 
- Andrea Raura 
- Brayan Jácome 
- Jossue Toscano
Proyecto: 
- Sistema de Análisis de Riesgo Emocional
Asignatura: 
- Análisis (Patrones de Diseño)
Semestre: 
- Sep25 - Mar26

---

## Enlaces Útiles

- [Design Patterns Gang of Four](https://en.wikipedia.org/wiki/Design_Patterns)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python 3 Documentation](https://docs.python.org/3/)
- [PlantUML Documentation](https://plantuml.com/)

---

Gracias por su atención
