import React, { Component } from 'react';
import logo from '../resources/sidebarlogo.svg'
import app from '../../../utils/firebase'

import SettingsIcon from '@mui/icons-material/Settings';
import AccountBalanceWalletIcon from '@mui/icons-material/AccountBalanceWallet';
import MapIcon from '@mui/icons-material/Map';
import InsightsIcon from '@mui/icons-material/Insights';
import HomeIcon from '@mui/icons-material/Home';
import FlagIcon from '@mui/icons-material/Flag';
import LogoutIcon from '@mui/icons-material/Logout';

import {useAuth} from '../../../context/auth'




const SideBar = () => {

    const {Logout} = useAuth();

    return (
        <div className='Dashboard-sidebar'>
            <div className='Dashboard-logo'>
                <img src={logo} />
                <h1>DriverX</h1>
            </div>
            <div className='Dashboard-links'>
                <div className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <HomeIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Overview</h1>
                </div>
                <div className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <InsightsIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Statistics</h1>
                </div>
                <div className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <FlagIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Tickets</h1>
                </div>
                <div className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <MapIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Maps</h1>
                </div>
                <div className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <AccountBalanceWalletIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Transactions</h1>
                </div>
                <div className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <SettingsIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Settings</h1>
                </div>
                <div onClick={async e =>{
                    e.preventDefault()
                    Logout()
                }} className='Dashboard-li-links'>
                    <div className='Dashboard-link-icon'>
                        <LogoutIcon style={{fill: "#DDE2FF"}}/>
                    </div>
                    <h1>Sign Out</h1>
                </div>
            </div>
        </div>
        );
}

export default SideBar;



