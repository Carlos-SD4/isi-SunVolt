# SunVolt

Este proyecto ha sido desarrollado por los siguientes miembros del grupo:
- nombre_del_miembro1
- nombre_del_miembro2
- nombre_del_miembro3

## Manual de Uso

En esta sección, vamos a proporcionar un manual de uso para los tres archivos: **NREL.py**, **REData.py** y **OpenWeatherMap.py**. Este manual te guiará sobre cómo ejecutar estos archivos y cómo configurar cualquier token necesario.

Antes de ejecutar estos archivos, es importante instalar todas las bibliotecas o paquetes necesarios. Para hacer esto, deberás ejecutar el archivo **requirements.txt**. Aquí tienes un ejemplo de cómo podrías hacerlo:

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu entorno Python:

$ pip install -r requirements.txt

Una vez que hayas instalado todas las dependencias necesarias, puedes proceder a ejecutar los archivos:

### NREL.py y REData.py
Estos dos archivos no requieren ningún token para su ejecución. Simplemente puedes ejecutarlos en tu entorno Python. Asegúrate de tener todas las dependencias necesarias instaladas. Aquí tienes un ejemplo de cómo podrías ejecutar estos archivos:

$ python NREL.py
$ python REData.py

### OpenWeatherMap.py
Para este archivo, necesitarás registrarte y obtener un token. Sigue estos pasos:
1. Ve a la página web de OpenWeatherMap y regístrate para obtener una cuenta.
2. Una vez que hayas creado tu cuenta, podrás generar un token. Este token es necesario para hacer solicitudes a la API de OpenWeatherMap.
3. Una vez que hayas obtenido tu token, debes sustituirlo en el archivo `OpenWeatherMap.py` donde pone `API_KEY`. Aquí tienes un ejemplo de cómo podría verse:

API_KEY = "tu_api_key"

Después de reemplazar el token, puedes ejecutar el archivo `OpenWeatherMap.py` de la misma manera que los otros archivos:

$ python OpenWeatherMap.py

Este es un ejemplo básico. Puedes personalizarlo según tus necesidades. ¡Espero que esto te ayude! 😊
