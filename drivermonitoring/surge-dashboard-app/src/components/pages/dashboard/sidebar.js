import React, { Component } from 'react';
import logo from '../resources/sidebarlogo.svg'


class SideBar extends Component {
    render() { 
        return (
        <div className='Dashboard-sidebar'>
            <div className='Dashboard-logo'>
                <img src={logo} />
                <h1>DriverX</h1>
            </div>
            <div className='Dashboard-links'>
                <div className='Dashboard-li-links'><h1>Overview</h1></div>
                <div className='Dashboard-li-links'><h1>Statistics</h1></div>
                <div className='Dashboard-li-links'><h1>Tickets</h1></div>
                <div className='Dashboard-li-links'><h1>Maps</h1></div>
                <div className='Dashboard-li-links'><h1>Transactions</h1></div>
                <div className='Dashboard-li-links'><h1>Settings</h1></div>
            </div>
        </div>
        );
    }
}

export default SideBar;