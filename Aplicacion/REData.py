import requests
from datetime import datetime, timedelta
import pytz

def get_real_time_market_prices():
    # Obtén la fecha y hora actual en la zona horaria de España (CET)
    tz = pytz.timezone(f'Europe/Madrid')
    now = datetime.now(tz)

    # Redondea la hora actual al intervalo de una hora hacia abajo
    rounded_hour = now.replace(minute=0, second=0, microsecond=0)

    # Formatea la fecha en el formato requerido por la API
    start_date = rounded_hour.strftime("%Y-%m-%dT%H:%M:%S")
    end_date = (rounded_hour + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S")

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
        if prices:
            for price_info in prices:
                datetime_str = price_info["datetime"]
                # Convierte la cadena de fecha y hora en un objeto datetime
                datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")
                # Formatea la fecha y hora en el formato solicitado
                formatted_datetime = datetime_obj.astimezone(tz).strftime("%Y-%m-%d a las %H:%M %Z")
                price_mwh = price_info["value"]
                # Convierte el precio a €/kWh
                price_kwh = price_mwh / 1000
                return price_kwh
        else:
            return get_real_time_market_prices()  # Intenta obtener datos para Madrid si no hay para la provincia
    else:
        print("Error al obtener los datos.")
        return None  # Devuelve None en caso de error


