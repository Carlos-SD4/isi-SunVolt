from flask import Flask, render_template, jsonify, request
from OpenWeatherMap import obtener_tiempo  # Importar la función obtener_tiempo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('InicioSesion.html')

@app.route('/tiempo')
def tiempo():
    provincia = request.args.get('provincia')  # Obtener la provincia desde la solicitud

    predicciones = obtener_tiempo(provincia)  # Usar la función obtener_tiempo

    return render_template('PaginaPrincipal.html', predicciones=predicciones)  # Renderizar Estadisticas.html con los datos de predicciones meteorológicas

if __name__ == '__main__':
    app.run(debug=True)
