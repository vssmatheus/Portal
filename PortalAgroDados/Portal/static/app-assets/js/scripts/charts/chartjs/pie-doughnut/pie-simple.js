/*=========================================================================================
    File Name: pie.js
    Description: Chartjs pie chart
    ----------------------------------------------------------------------------------------
    Item Name: Stack - Responsive Admin Theme
    Version: 1.0
    Author: PIXINVENT
    Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/

// Pie chart
// ------------------------------
$(window).on("load", function(){

    //Get the context of the Chart canvas element we want to select
    var ctx = $("#simple-pie-chart");

    // Chart Options
    var chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        responsiveAnimationDuration:500,
    };

    // Chart Data
    var chartData = {
        labels: LABEL_GRAFICO_EMPENHO,
        // labels: ["Valor", "Saldo", "Valor Faturado", "Valor Provisionado", "Valor Total Gasto"],
        datasets: [{
            // label: "My First dataset",
            data: GRAFICO_EMPENHO,
            // data: ['1510.09', 65, 34, 45, 35],
            backgroundColor: ['#f3f3d0', '#d38f00', '#686e9f','#3bbfad', '#76c96e'],
        }]
    };

    var config = {
        type: 'pie',

        // Chart Options
        options : chartOptions,

        data : chartData
    };

    // Create the chart
    var pieSimpleChart = new Chart(ctx, config);
});