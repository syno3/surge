import React, { Component } from 'react';
import SideBar from './pages/dashboard/sidebar';
import TopBar from './pages/dashboard/topbar';
import MainContent from './pages/dashboard/maincontent';
import StatisticsBody from './pages/dashboard/statisticsbody'


class Dashboard extends Component {
    state ={
        page: 'overview'
    }
    /* conditional rendering function */
    changePage(){
        if(this.state.page === 'overview'){
            return <MainContent />
        }else if (this.state.page === 'statistics'){
            return <StatisticsBody />
        }
    }

    render() { 
        return (
            <div className='Dashboard'>
                <SideBar />
                <div className='maincontent'>
                    <TopBar page={this.state.page}/>
                    {this.changePage()}
                </div>
            </div>
        );
    }
}
export default Dashboard;