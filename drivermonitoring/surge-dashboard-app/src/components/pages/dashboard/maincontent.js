import React, { Component } from 'react';
import Card from './topcard';
import MiddleCard from './middlecard';
import BottomCard from './bottomcard';


class MainContent extends React.Component {
    /* state sections */
    /* main render section */
    render() { 
        return (
        <div className='dashboard-main'>
            <div className='dashboard-main-top-card'>
                {/* link to firebase */}

                <Card name='Driver' number={60}/>
                <Card name='Flags' number= {890}/>
                <Card name='Cars' number={43}/>
                <Card name='Fuel' number={7000}/>
            </div>
            <div className='dashboard-middle-card'>
                {/* link to firebase */}

                <MiddleCard />
            </div>
            <div className='dasboard-bottom-cards'>
                {/* link to firebase */}

                <BottomCard />
            </div>
        </div>
        );
    }
}

export default MainContent;