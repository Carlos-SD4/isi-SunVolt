from flask import Flask, render_template
from APIs import NREL, OpenWeatherMap, REData


app = Flask(__name__)

@app.route('/pagina-principal')
def pagina_principal():
    # Llama al método mostrar_datos_en_espanol del módulo NREL
    NREL.mostrar_datos_en_espanol()
    OpenWeatherMap.obtener_tiempo('Madrid')
    REData.get_real_time_market_prices()

    # Resto de tu código aquí...

if __name__ == '__main__':
    app.run(debug=True)
