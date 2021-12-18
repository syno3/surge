
import React, { Component } from 'react';
import ReactApexCharts from 'react-apexcharts'



class Pie extends Component {
    
    constructor(props) {
        super(props);
            this.state = {
                series: [44, 55, 13, 43, 22],
                options: {
                chart: {
                    width: 380,
                    type: 'pie',
                },
                labels: ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                responsive: [{
                    breakpoint: 480,
                    options: {
                    chart: {
                        width: 300
                    },
                    legend: {
                        position: 'bottom'
                    }
                    }
                }]
            },
        };
    }

    render() {
        return (
            <div id="chart">
                <ReactApexCharts options={this.state.options} series={this.state.series} type="pie" width={300} />
            </div>
        );
    }
}


export default Pie;