import React, { Component } from 'react';
import Card from './topcard';
import SbottomCards from './statisticsbottomcards';

class StatisticsBody extends React.Component {
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
            

            <div className='statistics-middle'>
                <div className='statistics-middle-piechart'>
                    {/* we will a pie chart D3.js */}
                </div>
                <div className='Statistics-middle-linechart'>
                    {/* we will a line chart D3.js */}
                </div>
            </div>
            
            <div className='statistics-bottom-cards'>
                <div className='statistics-bottom-row'>
                    {/* props: number, name, icon */}
                    <SbottomCards number={8286}/>
                    <SbottomCards number={8520}/>
                    <SbottomCards number={4872}/>
                    <SbottomCards number={167}/>
                </div>
                <div className='statistics-bottom-row'>
                    <SbottomCards number={1478286}/>
                    <SbottomCards number={478520}/>
                    <SbottomCards number={154872}/>
                    <SbottomCards number={167}/>
                </div>
            </div>

        </div>
        );
    }
}

export default StatisticsBody;