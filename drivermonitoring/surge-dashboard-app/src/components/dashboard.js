import React, { Component } from 'react';
import MainContent from './pages/dashboard/maincontent';
import SideBar from './pages/dashboard/sidebar';
import TopBar from './pages/dashboard/topbar';


class Dashboard extends React.Component {
    render() { 
        return (
            <div className='Dashboard'>
                <SideBar />
                <div className='maincontent'>
                    <TopBar />
                    <MainContent />
                </div>
            </div>
        );
    }
}
export default Dashboard;