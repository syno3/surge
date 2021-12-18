import React, { Component } from 'react';
import MiddleCard2 from './middlecard2';
import LineChart from './linechartmiddle'

class MiddleCard extends Component {
    /* contain states for the middle card */
    render() { 
        return (
        <div className='dashboard-middle-card-one'>
            <div className='dashboard-middle-card-chart'>
                {/* we use chart js */}
                <LineChart />
            </div>
            <div className='dashboard-middle-card-r'>
                {/* we will update later */}
                <MiddleCard2 name='Resolved' number={442}/>
                <MiddleCard2 name='Received' number={449}/>
                <MiddleCard2 name='Average first response time' number={33}/>
                <MiddleCard2 name='Average response time' number={94}/>
            </div>
        </div>
        );
    }
}
export default MiddleCard;