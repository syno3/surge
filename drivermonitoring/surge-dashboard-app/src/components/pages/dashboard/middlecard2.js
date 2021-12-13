import React, { Component } from 'react';

class MiddleCard2 extends Component {
    render() { 
        return (
            <div className='dashboard-middle-card-2'>
                <h2 className='dashboard-card-name'>{this.props.name}</h2>
                <h2 className='dashboard-card-number'>{this.props.number}</h2>
            </div>
        );
    }
}

export default MiddleCard2;