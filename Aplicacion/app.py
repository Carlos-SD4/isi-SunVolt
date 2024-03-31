import json, os
import plotly.graph_objs as go
from OpenWeatherMap import obtener_tiempo  # Importar la función obtener_tiempo
from REData import get_real_time_market_prices  # Importar la función get_real_time_market_prices
from NREL import obtener_produccion  # Importar la función mostrar_datos_en_espanol
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/InicioSesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        # Obtener los datos del formulario HTML
        correo = request.form['correo']
        contraseña = request.form['contrasena']

        # Abrir el archivo JSON y cargar los datos existentes
        with open('usuarios.json', 'r') as f:
            data = json.load(f)

            # Verificar si las credenciales son válidas
            if any(usuario['correo'] == correo and usuario['contrasena'] == contraseña for usuario in data['usuarios']):
                # Obtener la provincia del usuario autenticado
                provincia_usuario = next((usuario['provincia'] for usuario in data['usuarios'] if usuario['correo'] == correo), None)
                # Redirigir a la página principal incluyendo la provincia como argumento en la URL
                return redirect(url_for('pagina_principal', provincia=provincia_usuario))
            else:
                return render_template('InicioSesion.html', error_message="Correo o contraseña incorrectos")

    # Renderizar la plantilla InicioSesion.html
    return render_template('InicioSesion.html')

@app.route('/Registro', methods=['GET', 'POST'])
def registro():
    error_message = None  # Inicializa el mensaje de error como None
    if request.method == 'POST':
        # Obtener los datos del formulario HTML
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        provincia = request.form['provincia']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        # Abrir el archivo JSON y cargar los datos existentes
        with open('usuarios.json', 'r+') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = {'usuarios': []}

            # Verificar si el correo del nuevo usuario ya está en uso
            if any(usuario['correo'] == correo for usuario in data['usuarios']):
                error_message = "El correo electrónico ya está registrado. Por favor, use otro correo electrónico."
            else:
                # Crear un diccionario con los datos del nuevo usuario
                nuevo_usuario = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'provincia': provincia,
                    'correo': correo,
                    'contrasena': contrasena
                }

                # Agregar el nuevo usuario a la lista de usuarios existente
                data['usuarios'].append(nuevo_usuario)

                # Volver al principio del archivo y escribir los datos actualizados
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

                # Redireccionar a la página de inicio de sesión
                return redirect(url_for('inicio_sesion'))

    # Si el método de solicitud es GET o si hay un error, renderizar el formulario de registro con el mensaje de error
    return render_template('Registro.html', error_message=error_message)


@app.route('/Principal')
def pagina_principal():
    provincia = request.args.get('provincia')  # Obtener la provincia desde la solicitud
    predicciones = obtener_tiempo(provincia)  # Usar la función obtener_tiempo

    produccion_total = obtener_produccion()  # Usar la función mostrar_datos_en_espanol
    produccion = round((produccion_total/12)/31, 2)
    consumo_electrico = produccion/2

    return render_template('PaginaPrincipal.html', predicciones=predicciones, produccion=produccion, consumo_electrico=consumo_electrico)


@app.route('/mis_dispositivos')
def mis_dispositivos():
    return render_template('Dispositivos.html')

@app.route('/recomendaciones')
def recomendaciones():
    provincia = request.args.get('provincia')
    predicciones_tiempo = obtener_tiempo(provincia)
    precioluz = get_real_time_market_prices()
    current_hour = datetime.now().hour  # Obtener la hora actual
    return render_template('Recomendaciones.html', predicciones_tiempo=predicciones_tiempo, precioluz=precioluz, current_hour=current_hour)




if __name__ == '__main__':
    app.run(debug=True)



