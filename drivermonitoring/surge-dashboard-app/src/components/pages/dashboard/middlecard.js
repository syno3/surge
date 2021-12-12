import React, { Component } from 'react';

class MiddleCard extends React.Component {
    /* contain states for the middle card */
    state = {
        details: [
            {name: 'test', value: 449},
            {name: 'test', value: 426},
            {name: 'test', value: 33},
            {name: 'test', value: 203},
            {name: 'test', value: 94},
        ]
    }

    render() { 
        return (
        <div className='dashboard-middle-card-one'>
        </div>
        );
    }
}
export default MiddleCard;