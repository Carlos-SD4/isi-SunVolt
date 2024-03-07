import requests

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
                print(f"Provincia: {provincia}, Fecha: {fecha}, Temperatura: {temperatura}°C, Nubosidad: {nubosidad}%")
                return
        print(f"No se encontraron datos meteorológicos para la fecha {fecha} en la provincia: {provincia}")
    else:
        print(f"Error al obtener datos meteorológicos para la provincia: {provincia}")

if __name__ == "__main__":
    provincia = input("Ingrese el nombre de la provincia: ")
    fecha = input("Ingrese la fecha en el formato YYYY-MM-DD HH:MM:SS: ")
    obtener_tiempo(provincia, fecha)

