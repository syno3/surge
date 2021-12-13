import React, { Component } from 'react';
import SideBar from './pages/dashboard/sidebar';
import TopBar from './pages/dashboard/topbar';
import StatisticsBody from './pages/dashboard/statisticsbody'

class Statistics extends Component {
    render() { 
        return (
        <div className='Dashboard'>
            <SideBar />
            <div className='maincontent'>
                <TopBar page='Statistics'/>
            </div>
        </div>
        );
    }
}

export default Statistics;