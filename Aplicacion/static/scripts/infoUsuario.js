document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const correoUsuario = params.get('correo'); // Asume que pasas el correo como parámetro

    fetch('usuarios.json')
        .then(response => response.json())
        .then(data => {
            const usuario = data.usuarios.find(u => u.correo === correoUsuario);
            if (usuario) {
                const contenedor = document.getElementById('infoUsuario');
                contenedor.innerHTML = `
                    <h2>${usuario.nombre} ${usuario.apellido}</h2>
                    <p>Correo: ${usuario.correo}</p>
                    <p>Provincia: ${usuario.provincia}</p>
                `;
            } else {
                document.getElementById('infoUsuario').textContent = 'Usuario no encontrado.';
            }
        });
});
