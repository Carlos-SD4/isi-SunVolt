from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from colorama import Fore, Style
import requests

app = Flask(__name__)

def obtener_tiempo(provincia):
    API_KEY = "cfe4345974400a6d38f5b383b86adb87"
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

        fecha_actual = datetime.now()

        predicciones = []

        for prediccion in lista_predicciones:
            fecha_prediccion = datetime.strptime(prediccion['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if fecha_prediccion >= fecha_actual and fecha_prediccion <= fecha_actual + timedelta(days=7):
                temperatura = round(prediccion['main']['temp'], 1)
                humedad = prediccion['main']['humidity']
                nubosidad = prediccion['clouds']['all']
                probabilidad_lluvia = prediccion['pop'] * 100  # Convertir a porcentaje
                
                # Estimación de la radiación solar basada en la nubosidad (valor arbitrario)
                radiacion_estimada = round(estimar_radiacion_solar(nubosidad))
                
                # Seleccionar color según el valor de radiación
                if radiacion_estimada >= 800:
                    color_radiacion = Fore.GREEN
                elif radiacion_estimada < 420:
                    color_radiacion = Fore.RED
                else:
                    color_radiacion = ''
                
                # Crear diccionario con la información de la predicción
                prediccion_info = {
                    'fecha': fecha_prediccion,
                    'temperatura': temperatura,
                    'humedad': humedad,
                    'nubosidad': nubosidad,
                    'probabilidad_lluvia': probabilidad_lluvia,
                    'radiacion_solar': radiacion_estimada
                }

                predicciones.append(prediccion_info)

        return predicciones
    else:
        return []

def estimar_radiacion_solar(nubosidad):
    # Coeficiente de corrección arbitrario para la nubosidad (este valor puede ajustarse según sea necesario)
    coeficiente_nubosidad = 0.6
    
    # Supongamos que la radiación solar máxima posible en un día despejado es de 1000 W/m^2
    radiacion_maxima = 1000  # W/m^2
    
    # Estimación de la radiación solar basada en la nubosidad
    radiacion_estimada = radiacion_maxima * (1 - coeficiente_nubosidad * (nubosidad / 100))  # Convertimos nubosidad a fracción
    
    return radiacion_estimada

if __name__ == '__main__':
    app.run(debug=True)
