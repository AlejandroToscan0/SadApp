# 🧠 Sistema de Análisis de Riesgo Emocional  
### Patrón **Singleton** + **Abstract Factory**

Este proyecto implementa un sistema modular para analizar texto y determinar niveles de riesgo emocional utilizando dos enfoques diferentes:

- **Análisis Lingüístico** (basado en reglas y métricas)
- **Machine Learning** (clasificación probabilística)

El diseño sigue dos patrones de diseño fundamentales:

- **Abstract Factory** → Para crear familias completas de procesadores y analizadores.  
- **Singleton** → Para administrar un único gestor central de análisis que puede cambiar dinámicamente de estrategia.



## 📂 Estructura del Proyecto

proyecto_analisis/
│
├── main.py
│
├── core/
│ ├── interfaces.py
│ └── singleton.py
│
├── productos/
│ ├── procesadores.py
│ └── analizadores.py
│
└── fabricas/
└── fabricas.py



## 🧩 Componentes del Sistema

### **1. Interfaces (core/interfaces.py)**
Define las abstracciones:
- ProcesadorTexto
- AnalizadorRiesgo
- SaludMentalFactory (Abstract Factory)

### **2. Productos Concretos (productos/)**
Cada familia tiene su propio procesador y analizador.

**Familia Lingüística**  
- ProcesadorPalabrasClave  
- AnalizadorPuntajePonderado  

**Familia Machine Learning**  
- ProcesadorVectorial  
- ClasificadorNaiveBayes  

### **3. Fábricas Concretas (fabricas/fabricas.py)**
- FabricaLinguistica
- FabricaMachineLearning

Estas generan objetos compatibles entre sí.

### **4. Singleton (core/singleton.py)**  
`AdministradorAnalisisTexto` gestiona el flujo de análisis y asegura una única instancia en todo el sistema.



## ▶️ Ejecución

Ejecuta el archivo principal:

```bash
python main.py
```