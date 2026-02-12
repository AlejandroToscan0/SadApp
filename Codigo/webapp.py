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
	texto = request.form.get('texto', '').strip()
	strategy = request.form.get('strategy', 'linguistica')

	factory = _get_factory(strategy)

	# Inicializar/obtener singleton
	manager = AdministradorAnalisisTexto.get_instancia(factory)
	# Si ya existía, cambiamos la factory
	manager.set_factory(factory)

	resultado = manager.analizar(texto)

	# Para permitir uso en template, convertir llaves a atributos simples usando un pequeño helper
	class Attr:
		def __init__(self, d):
			self.__dict__.update(d)

	# preparar objeto simple para Jinja
	analisis = resultado['analisis']
	out = type('R', (), {})()
	out.analisis = Attr(analisis)
	out.recomendacion = resultado['recomendacion']
	out.recursos = resultado['recursos']

	return render_template('index.html', resultado=out, ejemplo=texto)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', '5001'))
	host = os.environ.get('HOST', '127.0.0.1')
	print(f'Iniciando servidor web en http://{host}:{port}')
	app.run(host=host, port=port, debug=False)