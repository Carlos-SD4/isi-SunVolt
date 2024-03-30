import json, os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/InicioSesion')
def pagina_principal():
    # Renderiza la plantilla InicioSesion.html
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
        contraseña = request.form['contraseña']

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
                    'contraseña': contraseña
                }

                # Agregar el nuevo usuario a la lista de usuarios existente
                data['usuarios'].append(nuevo_usuario)

                # Volver al principio del archivo y escribir los datos actualizados
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

                # Redireccionar a la página de inicio de sesión
                return redirect(url_for('pagina_principal'))

    # Si el método de solicitud es GET o si hay un error, renderizar el formulario de registro con el mensaje de error
    return render_template('Registro.html', error_message=error_message)




if __name__ == '__main__':
    app.run(debug=True)



