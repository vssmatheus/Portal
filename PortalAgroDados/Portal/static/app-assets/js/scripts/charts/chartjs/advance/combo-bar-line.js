/*=========================================================================================
    File Name: combo-bar-line.js
    Description: Chartjs combo bar line chart
    ----------------------------------------------------------------------------------------
    Item Name: Stack - Responsive Admin Theme
    Version: 1.0
    Author: PIXINVENT
    Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/

// Combo bar line chart
// ------------------------------
$(window).on("load", function(){

    //Get the context of the Chart canvas element we want to select
    var ctx = $("#combo-bar-line");

    // Chart Options
    var chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                display: true,
                gridLines: {
                    color: "#f3f3f3",
                    drawTicks: false,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Placas'
                }
            }],
            yAxes: [{
                display: true,
                gridLines: {
                    color: "#f3f3f3",
                    drawTicks: false,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Valores'
                }
            }]
        },
        title: {
            display: false,
            text: 'Chart.js Combo Bar Line Chart'
        }
    };

    // Chart Data
    var chartData = {
        labels: LABEL_GRAFICO_RANKING,
        datasets: [
        //     {
        //     type: 'line',
        //     label: "My Second dataset",
        //     data: PERCENTUAL_GRAFICO_RANKING,
        //     backgroundColor: "rgba(250,142,117,.5)",
        //     borderColor: "transparent",
        //     borderWidth: 2,
        //     pointBorderColor: "#FA8E75",
        //     pointBackgroundColor: "#FFF",
        //     pointBorderWidth: 2,
        //     pointHoverBorderWidth: 2,
        //     pointRadius: 4,
        // }
        {
            type: 'bar',
            label: 'Valor Total',
            // data: [65, 59, 80, 81, 56, 55, 40.50,50,50],
            data: VALOR_GRAFICO_RANKING,
            backgroundColor: "#597d5e",
            borderColor: "transparent",
            borderWidth: 2
        }
        // ,{
        //     type: 'bar',
        //     label: "My Third dataset - No bezier",
        //     data: PERCENTUAL_GRAFICO_RANKING,
        //     backgroundColor: "#F25E75",
        //     borderColor: "transparent",
        //     borderWidth: 2
        // }
        ]
    };

    var config = {
        type: 'bar',

        // Chart Options
        options : chartOptions,

        data : chartData
    };

    // Create the chart
    var lineChart = new Chart(ctx, config);

});