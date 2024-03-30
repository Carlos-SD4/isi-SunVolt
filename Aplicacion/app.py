from flask import Flask, render_template

app = Flask(__name__)

@app.route('/InicioSesion')
def pagina_principal():
    # Renderiza la plantilla InicioSesion.html
    return render_template('InicioSesion.html')

@app.route('/Registro')  # Agrega una nueva ruta para la página de registro
def registro():
    # Renderiza la plantilla Registro.html
    return render_template('Registro.html')

if __name__ == '__main__':
    app.run(debug=True)

