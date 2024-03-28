from flask import Flask, render_template
from APIs import NREL, OpenWeatherMap, REData

app = Flask(__name__)

@app.route('/InicioSesion')
def pagina_principal():
    OpenWeatherMap.obtener_tiempo('Madrid')
    REData.get_real_time_market_prices()

    # Renderiza la plantilla InicioSesion.html
    return render_template('InicioSesion.html')

if __name__ == '__main__':
    app.run(debug=True)
