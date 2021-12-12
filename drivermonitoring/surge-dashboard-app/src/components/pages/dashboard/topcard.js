import React, { Component } from 'react';

class Card extends React.Component {

    render() { 
        return (
        <div className='dashboard-card-one'>
            <h1 className='dashboard-card-title'>{this.props.name}</h1>
            <h1 className='dashboard-card-value'>{this.props.number}</h1>
        </div>
        );
    }
}

export default Card;