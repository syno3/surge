import React, { Component } from 'react';

class DriverFlags extends Component {
    render() { 
        return (
            <div className='bottom-driver-name-flags'>
                <h1 className='bottom-driver-name'>{this.props.driver}</h1>
                <h1 className='bottom-driver-number-flags'>{this.props.flags}</h1>
            </div>
        );
    }
}

export default DriverFlags;