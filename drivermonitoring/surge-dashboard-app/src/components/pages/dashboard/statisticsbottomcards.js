import React, { Component } from 'react';

class SbottomCards extends Component {
    render() { 
        return (
        <div className='statistics-bottom-row-card'>
            <div className='bottom-cards-flex'>
                <div className='bottom-cards-block'>
                    <h1 className='bottom-cards-num'>{this.props.number}</h1>
                </div>
            </div>
        </div>
        );
    }
}

export default SbottomCards;