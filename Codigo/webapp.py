from flask import Flask, request, render_template, redirect, url_for
import os
from fabricas.FabricaLinguistica import FabricaLinguistica
from fabricas.FabricaMachineLearning import FabricaMachineLearning
from core.singleton import AdministradorAnalisisTexto

app = Flask(__name__)


def _get_factory(choice: str):
    if choice == 'ml':
        return FabricaMachineLearning()
    return FabricaLinguistica()


@app.route('/', methods=['GET'])
def index():
    ejemplo = 'me siento triste y nada tiene sentido'
    return render_template('index.html', resultado=None, ejemplo=ejemplo)


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        texto = request.form.get('texto', '').strip()
        strategy = request.form.get('strategy', 'linguistica')

        # Validar que el texto no esté vacío
        if not texto:
            return render_template('index.html', resultado=None, ejemplo=texto, error="Por favor ingresa un texto"), 400

        print(f"[DEBUG] Texto recibido: {texto[:50]}...")
        print(f"[DEBUG] Estrategia: {strategy}")

        factory = _get_factory(strategy)
        print(f"[DEBUG] Factory creada: {type(factory).__name__}")

        # Inicializar/obtener singleton
        manager = AdministradorAnalisisTexto.get_instancia(factory)
        print(f"[DEBUG] Manager obtenido: {type(manager).__name__}")

        resultado = manager.analizar(texto)
        print(f"[DEBUG] Análisis completado: {resultado.keys()}")
        print(
            f"[DEBUG] Estructura de analisis: {resultado['analisis'].keys()}")

        # Pasar directamente el diccionario a Jinja2
        # Jinja2 puede acceder a dict keys como atributos
        return render_template('index.html', resultado=resultado, ejemplo=texto)

    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return render_template('index.html', resultado=None, ejemplo="", error=str(e)), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '5001'))
    host = os.environ.get('HOST', '127.0.0.1')
    print(f'Iniciando servidor web en http://{host}:{port}')
    app.run(host=host, port=port, debug=True)
