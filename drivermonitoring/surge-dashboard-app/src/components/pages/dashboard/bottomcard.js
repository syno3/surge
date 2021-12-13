import React, { Component } from 'react';
import DriverFlags from './driverflags'

class BottomCard extends React.Component {
    render() { 
        return (
            <React.Fragment>
                <div className='dashboard-bottom-card-one'>
                    <div className='dashboard-bottom-heading-one'>
                        <h2 className='bottom-heading-title'>Driver Flags</h2>
                        <h2 className='bottom-heading-flags'>More Details</h2>
                    </div>
                    <div className='bottom-driver'>
                        <DriverFlags driver='James Macharia' flags='4870'/>
                        <DriverFlags driver='Jalango Otieno' flags='3768'/>
                        <DriverFlags driver='Vincent Kemboi' flags='2655'/>
                        <DriverFlags driver='Festus Kirimi' flags='1457'/>   
                    </div>
                </div>
                <div className='dashboard-bottom-card-two'>
                    <div className='dashboard-bottom-heading-one'>
                        <h2 className='bottom-heading-title'>Driver Flags</h2>
                        <h2 className='bottom-heading-flags'>More Details</h2>
                    </div>
                    <div className='bottom-driver'>
                        <DriverFlags driver='James Macharia'/>
                        <DriverFlags driver='Jalango Otieno'/>
                        <DriverFlags driver='Vincent Kemboi'/>
                        <DriverFlags driver='Festus Kirimi'/>   
                    </div>
                </div>
            </React.Fragment>
            );
    }
}

export default BottomCard;