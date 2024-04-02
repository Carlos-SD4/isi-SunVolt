document.addEventListener('DOMContentLoaded', function() {
    const currentDateSpan = document.getElementById('currentDate');
    const ctx = document.getElementById('consumptionChart').getContext('2d');
    
    let dailyData = {
        labels: ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "24:00"],
        datasets: [{
            label: 'Energía Producida (kWh)',
            backgroundColor: 'rgba(76, 175, 80, 0.2)',
            borderColor: 'rgba(76, 175, 80, 1)',
            data: [0.08, 0.08, 0.2, 0.3, 0.2, 0.1, 0.08]
        }, {
            label: 'Energía Consumida (kWh)',
            backgroundColor: 'rgba(255, 165, 0, 0.2)',
            borderColor: 'rgba(255, 165, 0, 1)',
            data: [0.4, 0.4, 1.0, 1.5, 1.0, 0.5, 0.4]
        }]
    };

    // Datos mensuales (291.67 kWh de consumo medio mensual)
    let monthlyData = {
        labels: ["1", "5", "10", "15", "20", "25", "30"],
        datasets: [{
            label: 'Energía Producida (kWh)',
            backgroundColor: 'rgba(76, 175, 80, 0.2)',
            borderColor: 'rgba(76, 175, 80, 1)',
            data: [10, 11, 12, 11, 10, 11, 10] // Ejemplo de variación diaria con producción de ~20%
        }, {
            label: 'Energía Consumida (kWh)',
            backgroundColor: 'rgba(255, 165, 0, 0.2)',
            borderColor: 'rgba(255, 165, 0, 1)',
            data: [50, 55, 60, 55, 50, 55, 50] // Aproximadamente 291.67 kWh mensuales en total
        }]
    };

    // Datos anuales (3.500 kWh de consumo medio anual)
    let yearlyData = {
        labels: ["Enero", "Febrero", "Marzo", "Abril"],
        datasets: [{
            label: 'Energía Producida (kWh)',
            backgroundColor: 'rgba(76, 175, 80, 0.2)',
            borderColor: 'rgba(76, 175, 80, 1)',
            data: [58, 60, 62, 60] // 20% de la energía consumida
        }, {
            label: 'Energía Consumida (kWh)',
            backgroundColor: 'rgba(255, 165, 0, 0.2)',
            borderColor: 'rgba(255, 165, 0, 1)',
            data: [290, 300, 310, 300] // Aproximadamente 3.500 kWh anuales divididos en 12 meses
        }]
    };

    // Datos globales (últimos 5 años)
    let globalData = {
        labels: ["2020", "2021", "2022", "2023", "2024"],
        datasets: [{
            label: 'Energía Producida (kWh)',
            backgroundColor: 'rgba(76, 175, 80, 0.2)',
            borderColor: 'rgba(76, 175, 80, 1)',
            data: [700, 720, 740, 760, 280] // 20% de la energía consumida
        }, {
            label: 'Energía Consumida (kWh)',
            backgroundColor: 'rgba(255, 165, 0, 0.2)',
            borderColor: 'rgba(255, 165, 0, 1)',
            data: [3500, 3600, 3700, 3800, 1400] // Aumento anual del consumo + parcial para 2024
        }]
    };

    let consumptionChart = new Chart(ctx, {
        type: 'line',
        data: dailyData, // Inicializa con datos diarios
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    function updateChartAndDate(selection) {
        let data;
        let dateString = "";
        const now = new Date();

        switch(selection) {
            case 'daily':
                data = dailyData;
                dateString = `Día - ${now.toLocaleDateString()}`;
                break;
            case 'monthly':
                data = monthlyData;
                dateString = `Mes - ${now.toLocaleString('default', { month: 'long' })}`;
                break;
            case 'yearly':
                data = yearlyData;
                dateString = `Año - ${now.getFullYear()}`;
                break;
            case 'global':
                data = globalData;
                dateString = "Global";
                break;
            default:
                data = dailyData; // Por defecto a dailyData
                dateString = `Día - ${now.toLocaleDateString()}`;
                break;
        }

        consumptionChart.data = data;
        consumptionChart.update();
        currentDateSpan.textContent = dateString; // Actualiza el texto de la fecha
    }

    document.querySelectorAll('.time-range-selector button').forEach(button => {
        button.addEventListener('click', function() {
            document.querySelectorAll('.time-range-selector button').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const selection = this.id;
            updateChartAndDate(selection);
        });
    });

    // Inicialización por defecto con la gráfica diaria
    updateChartAndDate('daily');
});
