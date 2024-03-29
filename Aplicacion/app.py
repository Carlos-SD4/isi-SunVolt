from flask import Flask, render_template,request
from OpenWeatherMap import obtener_tiempo  # Importar la función obtener_tiempo
from REData import get_real_time_market_prices  # Importar la función get_real_time_market_prices

app = Flask(__name__)

@app.route('/Principal')
def index():
    provincia = request.args.get('provincia')  # Obtener la provincia desde la solicitud

    predicciones = obtener_tiempo(provincia)  # Usar la función obtener_tiempo

    return render_template('PaginaPrincipal.html', predicciones=predicciones)  # Renderizar Estadisticas.html con los datos de predicciones meteorológicas



@app.route('/mis_dispositivos')
def mis_dispositivos():
    return render_template('Dispositivos.html')

@app.route('/recomendaciones')
def recomendaciones():
    provincia = request.args.get('provincia', 'Madrid')  #Falta Ajustar tiempo y provincia con las apis
    predicciones_tiempo = obtener_tiempo(provincia)
    precioluz = get_real_time_market_prices()
    return render_template('Recomendaciones.html', predicciones_tiempo=predicciones_tiempo, precioluz=precioluz)


if __name__ == '__main__':
    app.run(debug=True)
