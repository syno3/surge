import React from 'react';
import SideBar from './pages/dashboard/sidebar';
import TopBar from './pages/dashboard/topbar';
import MainContent from './pages/dashboard/maincontent';
import StatisticsBody from './pages/dashboard/statisticsbody'
import { dashboardselector } from '../store/globalstate'
import { useRecoilValue } from 'recoil';



const Dashboard = () => {
    const page = useRecoilValue(dashboardselector);

    function changePage(){
        if(page === 'overview'){
            return <MainContent />
        }else if (page === 'statistics'){
            return <StatisticsBody />
        }
    }

    return (
        <div className='Dashboard'>
            <SideBar />
            <div className='maincontent'>
                <TopBar page={page}/>
                {changePage()}
            </div>
        </div>
    );
}
export default Dashboard;




