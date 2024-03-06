from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def obtener_tiempo(provincia, fecha):
    API_KEY = "tu_api_key"
    URL = "http://api.openweathermap.org/data/2.5/forecast"

    parametros = {
        'q': provincia + ', Spain',
        'appid': API_KEY,
        'units': 'metric',  # Para obtener la temperatura en Celsius
        'cnt': 40  # Número máximo de resultados (máximo permitido por OpenWeatherMap)
    }

    response = requests.get(URL, params=parametros)

    if response.status_code == 200:
        data = response.json()
        lista_predicciones = data['list']
        
        for prediccion in lista_predicciones:
            if prediccion['dt_txt'] == fecha:
                temperatura = prediccion['main']['temp']
                nubosidad = prediccion['clouds']['all']
                return {"provincia": provincia, "fecha": fecha, "temperatura": temperatura, "nubosidad": nubosidad}
        
        return {"error": f"No se encontraron datos meteorológicos para la fecha {fecha} en la provincia: {provincia}"}
    else:
        return {"error": f"Error al obtener datos meteorológicos para la provincia: {provincia}"}

@app.route('/tiempo', methods=['GET'])
def consultar_tiempo():
    provincia = request.args.get('provincia')
    fecha = request.args.get('fecha')
    if provincia and fecha:
        informacion_meteorologica = obtener_tiempo(provincia, fecha)
        return jsonify(informacion_meteorologica)
    else:
        return jsonify({"error": "Por favor, proporciona el nombre de la provincia en el parámetro 'provincia' y la fecha en el parámetro 'fecha' en el formato YYYY-MM-DD HH:MM:SS"}), 400

if __name__ == "__main__":
    app.run(debug=True)
