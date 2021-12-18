import React, { Component } from 'react';
import ReactApexCharts from 'react-apexcharts'

class LineChartStats extends Component {

    constructor(props) {
        super(props);
        this.state = {
            series: [{
            name: "STOCK ABC",
            data: [500, 410, 350, 510, 490, 620]
            }],
            options: {
            chart: {
                type: 'area',
                height: 350,
                zoom: {
                enabled: false
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'straight'
            },
            
            title: {
                text: 'Fundamental Analysis of Stocks',
                align: 'left'
            },
            subtitle: {
                text: 'Price Movements',
                align: 'left'
            },
            labels: [11/1/2021, 11/2/2021, 11/3/2021, 11/4/2021, 11/5/2021, 11/6/2021],
            xaxis: {
                type: 'datetime',
            },
            yaxis: {
                opposite: true
            },
            legend: {
                horizontalAlign: 'left'
            }
        },
        };
    }

    render() {
        return (
            <div id="chart">
                <ReactApexCharts options={this.state.options} series={this.state.series} type="area" height={350} />
            </div>
        );
    }
}


export default LineChartStats;