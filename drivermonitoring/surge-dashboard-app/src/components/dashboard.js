import React, { Component } from 'react';
import SideBar from './pages/dashboard/sidebar';
import TopBar from './pages/dashboard/topbar';
import MainContent from './pages/dashboard/maincontent';


class Dashboard extends Component {
    render() { 
        return (
            <div className='Dashboard'>
                <SideBar />
                <div className='maincontent'>
                    <TopBar page='Overview'/>
                    <MainContent />
                </div>
            </div>
        );
    }
}
export default Dashboard;