document.addEventListener('DOMContentLoaded', function() {
    const currentDateSpan = document.getElementById('currentDate');
    updateCurrentDate(); // Inicializa con "Global" al cargar

    const ctx = document.getElementById('consumptionChart').getContext('2d');
    let consumptionChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Enero", "Febrero", "Marzo", "Abril"], // Ejemplo de etiquetas
            datasets: [{
                label: 'Energía Producida',
                backgroundColor: 'rgba(76, 175, 80, 0.2)',
                borderColor: 'rgba(76, 175, 80, 1)',
                data: [20, 30, 45, 60], // Datos de ejemplo
            }, {
                label: 'Energía Consumida',
                backgroundColor: 'rgba(255, 165, 0, 0.2)',
                borderColor: 'rgba(255, 165, 0, 1)',
                data: [25, 35, 40, 55], // Datos de ejemplo
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    document.querySelectorAll('.time-range-selector button').forEach(button => {
        button.addEventListener('click', function() {
            document.querySelectorAll('.time-range-selector button').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const selection = this.id;
            updateCurrentDate(selection);
            
            // Aquí puedes añadir llamadas a funciones para actualizar el gráfico si es necesario.
            // Por ejemplo: updateChart(selection); 
        });
    });

    function updateCurrentDate(selection) {
        const now = new Date();
        let dateString = '';

        switch(selection) {
            case 'daily':
                dateString = `Día: ${now.toLocaleDateString()}`;
                break;
            case 'monthly':
                dateString = `Mes: ${now.toLocaleString('default', { month: 'long' })} ${now.getFullYear()}`;
                break;
            case 'yearly':
                dateString = `Año: ${now.getFullYear()}`;
                break;
            case 'global':
                dateString = "Global";
                break;
            default:
                dateString = `Día: ${now.toLocaleDateString()}`;
                break;
        }

        currentDateSpan.textContent = dateString;
    }

    // La implementación para updateChart(selection) debería ir aquí, adaptada a cómo planeas actualizar los datos del gráfico
});
