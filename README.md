# SunVolt

Este proyecto ha sido desarrollado por los siguientes miembros del grupo:
- Javier Pardo González
- Carlos Sánchez Díaz
- Pablo Díaz Calderón

## Manual de Uso para sprint 1 y 2

En esta sección, vamos a proporcionar un manual de uso para los tres archivos: **NREL.py**, **REData.py** y **OpenWeatherMap.py**. Este manual te guiará sobre cómo ejecutar estos archivos y cómo configurar cualquier token necesario.

Antes de ejecutar estos archivos, es importante instalar todas las bibliotecas o paquetes necesarios. Para hacer esto, deberás ejecutar el archivo **requirements.txt**. Aquí tienes un ejemplo de cómo podrías hacerlo:

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu entorno Python:

$ pip install -r requirements.txt

Una vez que hayas instalado todas las dependencias necesarias, puedes proceder a ejecutar los archivos:

### NREL.py y REData.py
Estos dos archivos no requieren ningún token para su ejecución. Simplemente puedes ejecutarlos en tu entorno Python. Asegúrate de tener todas las dependencias necesarias instaladas. Aquí tienes un ejemplo de cómo podrías ejecutar estos archivos:

$ python NREL.py
$ python REData.py

Para la api NREL cabe recordar que hay un numero limitado de peticiones por lo que habra un momento en el que la aplicacion no vaya

### OpenWeatherMap.py
Para este archivo, necesitarás registrarte y obtener un token. Sigue estos pasos:
1. Ve a la página web de OpenWeatherMap y regístrate para obtener una cuenta.
2. Una vez que hayas creado tu cuenta, podrás generar un token. Este token es necesario para hacer solicitudes a la API de OpenWeatherMap.
3. Una vez que hayas obtenido tu token, debes sustituirlo en el archivo `OpenWeatherMap.py` donde pone `API_KEY`. Aquí tienes un ejemplo de cómo podría verse:

API_KEY = "tu_api_key"

Después de reemplazar el token, puedes ejecutar el archivo `OpenWeatherMap.py` de la misma manera que los otros archivos:

$ python OpenWeatherMap.py


## Manual de Uso para sprint 3 y 4

### EJECUCION DE LA IMAGEN DOCKER

Para ejecutar la aplicación utilizando Docker, sigue los siguientes pasos:

1. Abre una terminal.

2. Navega hasta el directorio raíz del proyecto.

3. Asegúrate de tener Docker instalado en tu sistema. Si no lo tienes instalado, consulta la documentación oficial de Docker para obtener instrucciones de instalación.

4. Ejecuta el siguiente comando para construir la imagen Docker utilizando el archivo Dockerfile proporcionado:

    ```bash
    sudo docker build -f Dockerfile -t sunvolt:latest .
    ```

   Este comando construirá la imagen Docker utilizando las instrucciones definidas en el archivo Dockerfile y le asignará el nombre `sunvolt` con la etiqueta `latest`.

5. Una vez que la construcción de la imagen haya finalizado con éxito, ejecuta el siguiente comando para iniciar un contenedor Docker a partir de la imagen recién creada:

    ```bash
    sudo docker run -p 2001:5000 -i sunvolt
    ```

   Este comando ejecutará un contenedor Docker a partir de la imagen `sunvolt` y lo pondrá en funcionamiento. La opción `-p 2001:5000` mapea el puerto 5000 del contenedor al puerto 2001 del host, lo que permite acceder a la aplicación desde el navegador utilizando el puerto 2001.

6. Una vez que el contenedor esté en funcionamiento, puedes acceder a la aplicación desde tu navegador web ingresando la dirección `http://localhost:2001`.
