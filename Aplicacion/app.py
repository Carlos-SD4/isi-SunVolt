import json
import os
import random
import plotly.graph_objs as go
from OpenWeatherMap import obtener_tiempo  # Importar la función obtener_tiempo
from REData import get_real_time_market_prices  # Importar la función get_real_time_market_prices
from NREL import obtener_produccion  # Importar la función mostrar_datos_en_espanol
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def redirigir_a_inicio_sesion():
    return redirect(url_for('inicio_sesion'))

@app.route('/InicioSesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        # Obtener los datos del formulario HTML
        correo = request.form['correo']
        contraseña = request.form['contrasena']

        # Abrir el archivo JSON y cargar los datos existentes
        with open('usuarios.json', 'r') as f:
            data = json.load(f)
            usuario = next((u for u in data['usuarios'] if u['correo'] == correo and u['contrasena'] == contraseña), None)
            if usuario:
                session['correo'] = correo
                return redirect(url_for('pagina_principal', provincia=usuario['provincia']))
            else:
                return render_template('InicioSesion.html', error_message="Correo o contraseña incorrectos")
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

    bateria = 32
    precio = round(get_real_time_market_prices(provincia), 2)

    return render_template('PaginaPrincipal.html', predicciones=predicciones, produccion=produccion, consumo_electrico=consumo_electrico, bateria=bateria, precio=precio)

@app.route('/mis_dispositivos')
def mis_dispositivos():
    provincia = request.args.get('provincia')
    print(provincia)
    bateria=32
    return render_template('Dispositivos.html', provincia=provincia, bateria=bateria)

@app.route('/recomendaciones')
def recomendaciones():
    provincia = request.args.get('provincia')
    predicciones_tiempo = obtener_tiempo(provincia)
    precioluz = round(get_real_time_market_prices(provincia),2)
    hora_actual = datetime.now().hour  # Obtener la hora actual

    bateria = 32

    produccion_total = obtener_produccion()  # Usar la función mostrar_datos_en_espanol
    placa_solar = round((produccion_total/12)/31, 2)
    consumo_total= placa_solar+(placa_solar/2)

    # Filtrar las predicciones para obtener solo la del día de hoy
    prediccion_hoy = predicciones_tiempo[0] if predicciones_tiempo else None
    fecha_actual = datetime.now().date()
    
    recomendacion = generador_recomendaciones(prediccion_hoy, bateria, placa_solar, consumo_total)
    

    return render_template('Recomendaciones.html', provincia=provincia, predicciones_tiempo=predicciones_tiempo, placa_solar=placa_solar, precioluz=precioluz, consumo_total=consumo_total, fecha_actual=fecha_actual, hora_actual=hora_actual, bateria=bateria, recomendacion=recomendacion) 

def generador_recomendaciones(prediccion_hoy, bateria, placa_solar, consumo_total):
    recomendacion = None
    print(prediccion_hoy)
    # Verificar si se recibió una predicción para el día de hoy
    if prediccion_hoy:
        nubosidad = prediccion_hoy['nubosidad']
        radiacion_solar = prediccion_hoy['radiacion_solar']
        
        # Si la nubosidad es baja y la radiación solar es alta, utilizar la energía de las placas solares.
        if nubosidad < 30 and radiacion_solar > 700:
            recomendacion = "Recomendación: Utilizar la energía generada por las placas solares.\n"
            recomendacion += "Explicación: Las condiciones meteorológicas indican que hay poca nubosidad y una alta radiación solar, lo que sugiere que las placas solares pueden generar una cantidad significativa de energía. Aprovechar esta energía solar puede ayudar a reducir la dependencia de otras fuentes de energía y, potencialmente, ahorrar costos.\n"

        # Si la capacidad de la batería es alta y la generación de energía solar supera el consumo total, vender energía.
        elif bateria > 0.7 and placa_solar > consumo_total:
            recomendacion = "Recomendación: Vender la energía almacenada en la batería.\n"
            recomendacion += "Explicación: Dado que la capacidad de la batería es alta y la generación de energía solar es suficiente para cubrir el consumo total, vender el excedente de energía almacenada en la batería puede generar ingresos adicionales. Esto puede ser especialmente beneficioso durante períodos de alta demanda o cuando el precio de la electricidad es favorable en el mercado.\n"

        # Si la capacidad de la batería es baja y la radiación solar es alta, cargar la batería.
        elif bateria < 0.3 and radiacion_solar > 600:
            recomendacion = "Recomendación: Cargar la batería con la energía solar disponible.\n"
            recomendacion += "Explicación: En situaciones donde la capacidad de la batería es baja y la radiación solar es alta, aprovechar la energía solar disponible para cargar la batería puede garantizar un suministro continuo de energía cuando las condiciones meteorológicas no son óptimas para la generación solar directa. Esto puede ayudar a evitar interrupciones en el suministro eléctrico y mantener un nivel adecuado de reserva de energía.\n"

        # En otros casos, minimizar el consumo de energía.
        else:
            recomendacion = "Recomendación: Minimizar el consumo de energía eléctrica.\n"
            recomendacion += "Explicación: Cuando ninguna de las otras condiciones es aplicable, se recomienda minimizar el consumo de energía eléctrica para optimizar el uso de recursos y reducir costos. Esto puede lograrse apagando dispositivos no esenciales, ajustando la configuración de temperatura y utilizando tecnologías de eficiencia energética para optimizar el rendimiento de los equipos.\n"
    else:
        recomendacion = "No se pudo obtener la predicción del tiempo para el día de hoy."

    return recomendacion

@app.route('/estadisticas')
def estadisticas():
    return render_template('Estadisticas.html')

@app.route('/perfil')
def perfil():
    correo_usuario = session.get('correo')
    if not correo_usuario:
        return redirect(url_for('inicio_sesion'))
    with open('usuarios.json', 'r') as f:
        usuarios = json.load(f)['usuarios']
        usuario = next((u for u in usuarios if u['correo'] == correo_usuario), None)
    if usuario:
        return render_template('PerfilUsuario.html', nombre=usuario['nombre'], correo=correo_usuario)
    else:
        session.pop('correo', None)
        return redirect(url_for('inicio_sesion'))

@app.route('/info_usuario')
def info_usuario():
    correo_usuario = session.get('correo')
    if not correo_usuario:
        # Si no hay un correo en la sesión, redirigir al inicio de sesión
        return redirect(url_for('inicio_sesion'))
    
    with open('usuarios.json', 'r') as f:
        usuarios = json.load(f)['usuarios']
        usuario = next((u for u in usuarios if u['correo'] == correo_usuario), None)
    
    if usuario:
        # No incluyas la contraseña en la información que envías a la plantilla
        info = {
            'nombre': usuario['nombre'],
            'apellido': usuario['apellido'],
            'provincia': usuario['provincia'],
            'correo': usuario['correo']
        }
        return render_template('InfoUsuario.html', usuario=info)
    else:
        session.pop('correo', None)
        return redirect(url_for('inicio_sesion'))


if __name__ == '__main__':
    app.run(debug=True)




