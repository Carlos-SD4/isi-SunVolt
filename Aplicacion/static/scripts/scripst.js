document.addEventListener('DOMContentLoaded', function () {
    // Función para obtener los datos del tiempo
    function obtenerTiempo() {
        var provincia = document.getElementById('provincia').value; // Obtener la provincia desde el elemento oculto
        fetch(`/Principal?provincia=${provincia}`)
            .then(response => response.json())
            .then(data => {
                // Manipular los datos recibidos y actualizar el DOM según sea necesario
                document.getElementById('temperature').textContent = data.temperatura + '°C';
                document.getElementById('humidity').textContent = data.humedad + '%';
                document.getElementById('cloudiness').textContent = data.nubosidad + '%';
                document.getElementById('rain-probability').textContent = data.probabilidad_lluvia + '%';
                document.getElementById('solar-radiation').textContent = data.radiacion_solar + ' W/m^2';
            })
            .catch(error => console.error('Error al obtener los datos:', error));
    }

    // Llamar a la función obtenerTiempo al cargar la página
    obtenerTiempo();
});
