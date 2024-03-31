document.addEventListener('DOMContentLoaded', function() {
    // Actualiza la fecha actual en la página
    const currentDateSpan = document.getElementById('currentDate');
    updateCurrentDate();

    // Manejador para los botones de selección de rango de tiempo
    document.querySelectorAll('.time-range-selector button').forEach(button => {
        button.addEventListener('click', function() {
            // Remueve la clase 'active' de todos los botones y la asigna al clickeado
            document.querySelectorAll('.time-range-selector button').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Actualizar el gráfico basado en la selección
            const selection = this.id;
            updateChart(selection);
            
            // Opcionalmente, actualiza la fecha actual
            updateCurrentDate(selection);
        });
    });

    function updateChart(selection) {
        // Aquí va la lógica para actualizar el gráfico basada en la selección
        // Puede ser una solicitud AJAX al servidor para obtener nuevos datos y luego actualizar el gráfico
        console.log("Actualizar gráfico para: ", selection);
        // Ejemplo: updateChartData(selection); // Función ficticia que deberás implementar
    }

    function updateCurrentDate(selection = 'total') {
        const date = new Date();
        let dateString = '';
        switch(selection) {
            case 'daily':
                dateString = date.toLocaleDateString();
                break;
            case 'monthly':
                dateString = `${date.getMonth() + 1}/${date.getFullYear()}`;
                break;
            case 'yearly':
                dateString = date.getFullYear().toString();
                break;
            case 'total':
            default:
                dateString = 'Todo el tiempo';
                break;
        }
        currentDateSpan.textContent = dateString;
    }
});
