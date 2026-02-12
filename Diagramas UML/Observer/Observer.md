# 👁️ Patrón OBSERVER - Diagrama UML

## Descripción General

El patrón **Observer** define una relación uno-a-muchos donde cuando un objeto (Subject) cambia de estado, todos sus dependientes (Observers) son notificados automáticamente.

### 📍 Ubicación en el Proyecto
- **Archivo Principal**: `Codigo/core/observers/ObservadorAnalisis.py`
- **Observadores Concretos**:
  - `core/observers/LoggerAnalisis.py`
  - `core/observers/AlertaRiesgoAlto.py`
- **Propósito**: Notificar eventos de análisis a múltiples observadores

---

## 🎯 Problema Resuelto

**Escenario sin Observer:**
```python
# ❌ Acoplamiento fuerte
def analizar(self, texto):
    resultado = self._procesar(texto)
    
    # El Singleton NECESITA saber de Logger
    logger.registrar(resultado)
    
    # El Singleton NECESITA saber de Alertas
    if "ALTO" in resultado:
        alerta.enviar(resultado)
    
    # ¿Qué si agreguemos notificaciones por email?
    # ¿Y si queremos desactivar logging temporalmente?
```

**Solución con Observer:**
```python
# ✅ Desacoplamiento
def analizar(self, texto):
    resultado = self._procesar(texto)
    self.notificar("analisis_completado", resultado)
    # ↑ El Singleton NO sabe quién escucha
    # Los observadores se suscriben dinámicamente
```

---

## 📊 Diagrama UML Detallado

```
┌─────────────────────────────────────────────────────────────────┐
│                        Subject                                  │
│          (AdministradorAnalisisTexto - Singleton)              │
├─────────────────────────────────────────────────────────────────┤
│ - gestor_observadores: GestorObservadores                       │
├─────────────────────────────────────────────────────────────────┤
│ + registrar_observador(observador)                              │
│ + desregistrar_observador(observador)                           │
│ + analizar(texto: str) -> dict                                  │
│   • Ejecuta análisis                                            │
│   • 🔔 Notifica observadores al terminar                        │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 │ usa/delega notificaciones a
                 │
    ┌────────────▼──────────────────────────────┐
    │       GestorObservadores                  │
    ├───────────────────────────────────────────┤
    │ - _observadores: List[ObservadorAnalisis] │
    ├───────────────────────────────────────────┤
    │ + registrar(observador)                   │
    │ + desregistrar(observador)                │
    │ + notificar(evento, resultado)            │
    │ + limpiar()                               │
    └────────────┬─────────────────────────────┘
                 │
                 │ notifica a lista de
                 │
         ┌───────▼────────────────────────────────────┐
         │   ObservadorAnalisis (Interface)           │
         ├───────────────────────────────────────────┤
         │ + actualizar(evento: str, resultado: dict) │
         └┬───────────────────────────────────────────┘
          │
          │ implementa
          │
     ┌────┴────────────────────┬──────────────────────────────┐
     │                         │                              │
     ▼                         ▼                              ▼
┌──────────────┐      ┌──────────────┐          ┌──────────────────┐
│ LoggerAnalisis  │     │AlertaRiesgoAlto│       │ MiObservador     │
├──────────────┤      ├──────────────┤          ├──────────────────┤
│ + actualizar │      │ + actualizar │          │ + actualizar()   │
│   registra   │      │   alerta si  │          │ (customizado)    │
│   con LOG    │      │   "ALTO"     │          │                  │
└──────────────┘      └──────────────┘          └──────────────────┘

            Cada observador reacciona
            de forma INDEPENDIENTE
            sin conocerse entre sí
```

---

## 🔄 Flujo de Notificación

```
1. Usuario ingresa texto
         │
         ▼
┌─────────────────┐
│ admin.analizar()│
└────────┬────────┘
         │
    [Procesa]
    [Analiza]
    [Genera recomendaciones]
         │
         ▼
┌──────────────────────────────────┐
│ gestor_observadores.notificar()  │
│ (evento="analisis_completado")   │
└──────────────┬───────────────────┘
               │
        ┌──────┴──────┐
        │             │
        ▼             ▼
┌─────────────┐  ┌──────────────┐
│ Logger      │  │ AlertaAlto   │
│             │  │              │
│ actualizar()│  │ actualizar() │
│             │  │              │
│ Registra:   │  │ Si ALTO:     │
│ "[LOG]      │  │ Emite:       │
│  Análisis   │  │ 🚨 ALERTA    │
│  completado"│  │              │
└─────────────┘  └──────────────┘
        │              │
        ▼              ▼
   Terminal      Terminal (rojo)
   (info)        (alerta visual)
```

---

## 💻 Ejemplo de Código

### **1. Interfaz Observer**

```python
from abc import ABC, abstractmethod

class ObservadorAnalisis(ABC):
    @abstractmethod
    def actualizar(self, evento: str, resultado: dict) -> None:
        """Llamado cuando ocurre un evento."""
        pass
```

### **2. Gestor de Observadores**

```python
class GestorObservadores:
    def __init__(self):
        self._observadores = []
    
    def registrar(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"✓ {observador.__class__.__name__} registrado")
    
    def notificar(self, evento, resultado):
        for observador in self._observadores:
            try:
                observador.actualizar(evento, resultado)
            except Exception as e:
                print(f"⚠️ Error en {observador}: {e}")
```

### **3. Observador Concreto: Logger**

```python
class LoggerAnalisis(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if evento == "analisis_completado":
            print(f"[LOG {timestamp}] Análisis: {resultado['nivel']}")
            print(f"             Score: {resultado['score']}")
```

### **4. Observador Concreto: Alerta**

```python
class AlertaRiesgoAlto(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        if evento == "analisis_completado":
            if "ALTO" in resultado['analisis']['nivel']:
                print("\n🚨 ALERTA DE RIESGO ALTO\n")
                print(resultado['recomendacion'])
```

### **5. Uso en Subject (Singleton)**

```python
class AdministradorAnalisisTexto:
    def __init__(self, factory):
        self.gestor_observadores = GestorObservadores()
    
    def registrar_observador(self, observador):
        self.gestor_observadores.registrar(observador)
    
    def analizar(self, texto):
        # ... análisis ...
        resultado_completo = {...}
        
        # Notificar a todos los observadores registrados
        self.gestor_observadores.notificar(
            "analisis_completado", 
            resultado_completo
        )
        
        return resultado_completo
```

### **6. Uso en Cliente (main.py)**

```python
# Crear instancia única
manager = AdministradorAnalisisTexto.get_instancia(factory)

# Crear observadores
logger = LoggerAnalisis()
alerta = AlertaRiesgoAlto()

# Registrar (suscribir)
manager.registrar_observador(logger)
manager.registrar_observador(alerta)

# Ejecutar análisis
# → Notificará automáticamente a logger y alerta
resultado = manager.analizar("texto a analizar")
```

---

## 🔌 Eventos Soportados

### **Evento: "analisis_completado"**

Se dispara cuando termina un análisis exitoso.

**Datos incluidos:**
```python
{
    "analisis": {
        "nivel": "Riesgo ALTO",
        "score": 0.67,
        "metodo": "Análisis Lingüístico"
    },
    "recomendacion": "Busca ayuda profesional...",
    "recursos": ["Teléfono: 024", ...]
}
```

### **Posibles Extensiones:**

```python
# "procesamiento_iniciado"
# → Se dispara antes de procesar

# "riesgo_detectado"
# → Se dispara cuando detecta riesgo ALTO

# "error_en_analisis"
# → Se dispara si hay excepción
```

---

## 🎯 Ventajas Alcanzadas

| Ventaja | Descripción |
|---------|-------------|
| ✅ **Desacoplamiento** | Singleton no conoce observadores concretos |
| ✅ **Extensibilidad** | Agregar observador sin tocar Singleton |
| ✅ **Dinamismo** | Registrar/desregistrar en tiempo de ejecución |
| ✅ **Reusabilidad** | Observadores reutilizables en otros contextos |
| ✅ **Separación de responsabilidades** | Cada observador tiene una única tarea |

---

## 🧩 Patrones Complementarios

Observer funciona bien combinado con:

| Patrón | Descripción |
|--------|-------------|
| **Mediator** | Observer + Mediator para comunicación compleja |
| **Singleton** | Subject como singleton (nuestro caso) |
| **Command** | Encapsular acciones en observadores |
| **Strategy** | Diferentes estrategias de reacción |

---

## 📈 Diagrama de Estados en Ejecución

```
┌─────────────────────────────────────────────────────────────┐
│ EJECUCIÓN PASO A PASO                                       │
└─────────────────────────────────────────────────────────────┘

1. REGISTRO/SUSCRIPCIÓN
───────────────────────
manager.registrar_observador(logger)
    ↓
GestorObservadores._observadores = [logger]
    ↓
✓ Logger suscrito


2. ANÁLISIS EN PROGRESO
──────────────────────
manager.analizar("texto")
    ├─ [1] Procesa
    ├─ [2] Analiza
    ├─ [3] Genera recomendaciones
    └─ [4] Notifica observadores


3. NOTIFICACIÓN A LOGGER
────────────────────────
gestor_observadores.notificar("analisis_completado", resultado)
    ├─ Para cada observador en _observadores:
    │   └─ observador.actualizar("analisis_completado", resultado)
    │       └─ logger.actualizar(...)
    │           └─ Imprime en terminal
    │               "[LOG 12/02/2026 00:07:02] ✓ Análisis completado..."
    └─ ✓ Notificación completada


4. NOTIFICACIÓN A ALERTA
────────────────────────
gestor_observadores.notificar("analisis_completado", resultado)
    ├─ Para cada observador en _observadores:
    │   └─ observador.actualizar("analisis_completado", resultado)
    │       └─ alerta.actualizar(...)
    │           ├─ Verifica si "ALTO" está en nivel
    │           └─ Si es verdad:
    │               └─ Imprime alerta prominente
    │                   "🚨 ALERTA DE RIESGO ALTO 🚨"
    └─ ✓ Notificación completada


5. RETORNO AL CLIENTE
──────────────────────
return resultado_completo
    ↓
Cliente recibe resultado
(Observadores ya fueron notificados silenciosamente)
```

---

## 🧪 Casos de Uso Avanzados

### **Caso 1: Agregar Observador en Ejecución**

```python
# Crear sistema
manager = AdministradorAnalisisTexto.get_instancia(factory)
manager.registrar_observador(LoggerAnalisis())

# Hacer análisis
resultado1 = manager.analizar("texto 1")  # Solo Logger reacciona

# Agregar observador dinámicamente
manager.registrar_observador(AlertaRiesgoAlto())

# Hacer otro análisis
resultado2 = manager.analizar("texto 2")  # Logger + Alerta reaccionan
```

### **Caso 2: Observador Personalizado**

```python
class ObservadorEmail(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        if evento == "analisis_completado":
            if "ALTO" in resultado['nivel']:
                self.enviar_email_para_psiquiatra(resultado)

# Registrar
manager.registrar_observador(ObservadorEmail())
```

### **Caso 3: Desregistrar Observadores**

```python
logger = LoggerAnalisis()
manager.registrar_observador(logger)

# ... hacer análisis ...

# Ya no queremos logs
manager.desregistrar_observador(logger)

# Análisis sin logs
manager.analizar("nuevo texto")
```

---

## 📝 Implementación Paso a Paso

```python
# Paso 1: Definir interfaz abstracta
class ObservadorAnalisis(ABC):
    @abstractmethod
    def actualizar(self, evento, resultado):
        pass

# Paso 2: Crear gestor que maneja observadores
class GestorObservadores:
    def __init__(self):
        self._observadores = []
    
    def registrar(self, observador):
        self._observadores.append(observador)
    
    def notificar(self, evento, resultado):
        for obs in self._observadores:
            obs.actualizar(evento, resultado)

# Paso 3: Implementar observadores concretos
class MiObservador(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        # Lógica específica
        pass

# Paso 4: Usar en Subject (Singleton)
class Subject:
    def __init__(self):
        self.gestor = GestorObservadores()
    
    def registrar_observador(self, obs):
        self.gestor.registrar(obs)
    
    def notificar_observadores(self, evento, datos):
        self.gestor.notificar(evento, datos)
```

---

## 🔍 Diagrama de Secuencia

```
Cliente          Subject           Gestor          Logger      Alerta
  │                │                 │              │            │
  ├─register───────>│                 │              │            │
  │                 ├─register───────>│              │            │
  │                 │                 │              │            │
  ├─analizar───────>│                 │              │            │
  │                 │                 │              │            │
  │                 [Procesa]         │              │            │
  │                 [Analiza]         │              │            │
  │                 │                 │              │            │
  │                 ├─notificar──────>│              │            │
  │                 │                 ├─actualizar──>│            │
  │                 │                 │ (evento)     ├─LOG───────>│
  │                 │                 │              │ [Terminal] │
  │                 │                 │              │            │
  │                 │                 ├─actualizar──────────────>│
  │                 │                 │              │         ├─Print
  │                 │                 │              │         │ Alerta
  │                 │                 │              │         │ (si ALTO)
  │                 │                 │              │         >
  │                 │<─return────────────────────────────────────│
  │<─resultado──────│
  │                 │
  └─────────────────┘
```

---

## ✅ Checklist de Implementación

- [x] Interfaz `ObservadorAnalisis` definida
- [x] `GestorObservadores` coordinador
- [x] Observadores concretos (`Logger`, `Alerta`)
- [x] Integración en Singleton
- [x] Métodos de registro/desregistro
- [x] Notificación automática al completar análisis
- [x] Manejo de errores en observadores
- [x] Documentación y ejemplos

---

## 🚀 Extensiones Futuras

```python
# Idea 1: Observador para estadísticas
class ObservadorEstadisticas(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        # Contar análisis por nivel de riesgo
        # Guardar en base de datos

# Idea 2: Observador para notificaciones en tiempo real
class ObservadorWebSocket(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        # Enviar a clientes conectados vía WebSocket

# Idea 3: Observador para auditoría
class ObservadorAuditoria(ObservadorAnalisis):
    def actualizar(self, evento, resultado):
        # Registrar cambios para cumplimiento normativo
```

---

## 📚 Referencias

- **Patrón**: Observer (Behavioral Design Pattern)
- **GoF Book**: "Design Patterns: Elements of Reusable Object-Oriented Software"
- **Sinónimos**: Publish-Subscribe, Event-Subscriber, Listener
- **Propósito**: Notificar múltiples objetos de cambios de estado

---

**Diagrama creado**: 12 de febrero de 2026
**Proyecto**: Sistema de Análisis de Riesgo Emocional
**Patrón**: Observer (Behavioral)
