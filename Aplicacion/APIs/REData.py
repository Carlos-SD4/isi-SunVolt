import requests
from datetime import datetime, timedelta

def get_real_time_market_prices():
    # Obtén la fecha actual
    now = datetime.now()
    # Formatea la fecha en el formato requerido por la API
    start_date = now.strftime("%Y-%m-%dT00:00")
    end_date = now.strftime("%Y-%m-%dT23:59")

    url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real"
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "time_trunc": "hour"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Extrae los precios del kWh de los datos de la respuesta
        prices = data["included"][0]["attributes"]["values"]
        for price_info in prices:
            datetime_str = price_info["datetime"]
            # Convierte la cadena de fecha y hora en un objeto datetime
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            # Formatea la fecha y hora en el formato solicitado
            formatted_datetime = datetime_obj.strftime("%Y-%m-%d a las %H:%M")
            price_mwh = price_info["value"]
            # Convierte el precio a €/kWh
            price_kwh = price_mwh / 1000
            print(f"El precio del kWh en {formatted_datetime} es {price_kwh} €.")
    else:
        print("Error al obtener los datos.")

# Uso de la función
get_real_time_market_prices()
