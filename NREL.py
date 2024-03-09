import requests
import json

# Función para mostrar los datos en español
def mostrar_datos_en_espanol(datos):
    inputs = datos['inputs']
    outputs = datos['outputs']
    station_info = datos['station_info']

    print("Datos de producción de energía solar:")
    print("-------------------------------------")
    print("Ubicación: {}, {}, {}".format(station_info['city'], station_info['state'], station_info['country']))
    print("Latitud: {:.2f}°".format(station_info['lat']))
    print("Longitud: {:.2f}°".format(station_info['lon']))
    print("Altitud: {:.2f} metros".format(station_info['elev']))
    print("Orientación de los paneles solares: {} grados".format(inputs['azimuth']))
    print("Inclinación de los paneles solares: {} grados".format(inputs['tilt']))
    print("-------------------------------------")
    print("Producción mensual de energía eléctrica (kWh):")
    for mes, produccion in enumerate(outputs['ac_monthly'], start=1):
        print("Mes {}: {:.2f}".format(mes, produccion))
    print("-------------------------------------")
    print("Producción anual de energía eléctrica (kWh): {:.2f}".format(outputs['ac_annual']))
    print("Radiación solar anual promedio (kWh/m²/día): {:.2f}".format(outputs['solrad_annual']))
    print("Factor de capacidad: {:.2f}%".format(outputs['capacity_factor']))

# Parámetros de la solicitud
params = {
    'api_key': 'DEMO_KEY',
    'azimuth': '180',
    'system_capacity': '4',
    'losses': '14',
    'array_type': '1',
    'module_type': '0',
    'gcr': '0.4',
    'dc_ac_ratio': '1.2',
    'inv_eff': '96.0',
    'radius': '0',
    'dataset': 'nsrdb',
    'tilt': '10',
    'address': 'boulder, co',
    'soiling': '12|4|45|23|9|99|67|12.54|54|9|0|7.6',
    'albedo': '0.3',
    'bifaciality': '0.7'
}

# Realizar la solicitud
url = 'https://developer.nrel.gov/api/pvwatts/v8.json'
response = requests.get(url, params=params)
data = response.json()

# Guardar en un archivo JSON (opcional)
with open('respuesta_api.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

# Mostrar los datos en español
mostrar_datos_en_espanol(data)
