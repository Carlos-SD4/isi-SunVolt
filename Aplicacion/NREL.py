import requests

def obtener_produccion():
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

    # Obtener la producción anual de energía eléctrica
    produccion_anual = data['outputs']['ac_annual']

    return produccion_anual

# Prueba de la función
produccion_anual = obtener_produccion()
