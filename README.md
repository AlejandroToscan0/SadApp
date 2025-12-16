# 🧠 Sistema de Análisis de Riesgo Emocional  
### Patrón **Singleton** + **Abstract Factory** + **Factory Method**

Este proyecto implementa un sistema modular para analizar texto y determinar niveles de riesgo emocional utilizando dos enfoques diferentes:

- **Análisis Lingüístico** (basado en reglas y métricas)
- **Machine Learning** (clasificación probabilística)

El diseño sigue dos patrones de diseño fundamentales:

- **Singleton** → Para administrar un único gestor central de análisis que puede cambiar dinámicamente de estrategia.



## 📂 Estructura del Proyecto
```bash
├── 📁 Codigo
│   ├── 📁 core
│   │   ├── 📁 interfaces
│   │   │   ├── 🐍 AnalizadorRiesgo.py
│   │   │   ├── 🐍 ProcesadorTexto.py
│   │   │   ├── 🐍 Recomendacion.py
│   │   │   ├── 🐍 RecomendacionFactory.py
│   │   │   └── 🐍 SaludMentalFactory.py
│   │   └── 🐍 singleton.py
│   ├── 📁 fabricas
│   │   ├── 🐍 FabricaLinguistica.py
│   │   ├── 🐍 FabricaMachineLearning.py
│   │   ├── 🐍 RecomendacionRiesgoAltoFactory.py
│   │   ├── 🐍 RecomendacionRiesgoBajoFactory.py
│   │   └── 🐍 RecomendacionRiesgoModeradoFactory.py
│   ├── 📁 productos
│   │   ├── 📁 analizadores
│   │   │   ├── 🐍 AnalizadorPuntajePonderado.py
│   │   │   └── 🐍 ClasificadorNaiveBayes.py
│   │   ├── 📁 procesadores
│   │   │   ├── 🐍 ProcesadorPalabrasClave.py
│   │   │   └── 🐍 ProcesadorVectorial.py
│   │   └── 📁 recomendaciones
│   │       ├── 🐍 RecomendacionRiesgoAlto.py
│   │       ├── 🐍 RecomendacionRiesgoBajo.py
│   │       └── 🐍 RecomendacionRiesgoModerado.py
│   ├── 📁 resource
│   │   └── 🐍 GeneradorRecomendaciones.py
│   └── 🐍 main.py
├── 📁 Diagramas UML
│   ├── 📁 Abstract Factory
│   │   ├── 📄 Abstract Factory.mdj
│   │   └── 🖼️ Abstract Factory.png
│   ├── 📁 Factory Method
│   │   └── 🖼️ Factory Method.mdj
│   │   └── 🖼️ Factory Method.png
│   └── 📁 Singleton
│       ├── 📄 Singleton.mdj
│       └── 🖼️ Singleton.png
├── ⚙️ .gitignore
└── 📝 README.md
```


## 🧩 Componentes del Sistema

### **1. Singleton (core/singleton.py)**  
`AdministradorAnalisisTexto` gestiona el flujo de análisis y asegura una única instancia en todo el sistema.


## Instalación y ejecución
------------------------

Requisitos: Python 3.8+ y pip.

1) (Opcional) crear un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Instalar dependencias (para el front web)

```bash
pip install -r requirements.txt
```

3) Ejecutar la versión CLI (ya incluida)

```bash
python3 Codigo/main.py
```

4) Ejecutar el front web (abre http://127.0.0.1:5000)

```bash
python3 Codigo/webapp.py
```

Notas
-----

- El proyecto demuestra varios patrones: Singleton, Abstract Factory, Strategy y Factory Method.
- El front es un micro-servicio con Flask para facilitar la interacción y visualización de los patrones usados.



## ▶️ Ejecución

Ejecuta el archivo principal:

```bash
python main.py
```