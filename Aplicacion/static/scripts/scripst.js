document.addEventListener('DOMContentLoaded', function () {
    // Función para obtener los datos del tiempo
    function obtenerTiempo(provincia) {
        fetch(`/tiempo?provincia=${provincia}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('temperature').textContent = data.temperatura + '°C';
                document.getElementById('humidity').textContent = data.humedad + '%';
                document.getElementById('cloudiness').textContent = data.nubosidad + '%';
                document.getElementById('rain-probability').textContent = data.probabilidad_lluvia + '%';
                document.getElementById('solar-radiation').textContent = data.radiacion_solar + ' W/m^2';
            })
            .catch(error => console.error('Error al obtener los datos:', error));
    }

    /*obtenerTiempo('Ciudad Real');*/
});