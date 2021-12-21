import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import image from '../resources/about-image.svg';

class About extends Component {
    render() { 
        return (
        <div className= 'about'>
            <div className='about-content'>
                <div className='about-image'>
                    <img src={image} alt='about-image' />
                </div>
                <div className='about-block'>
                    <div className='about-text'>
                        <h1>we the leader in automotive safety in the country</h1>
                        <p>Using our innovative driver monitoring technology we are redifing standards of safety in the transport industry. We provide high quality analytics to fleet managers on their drivers and their fleet to help them make better decisions</p>
                    </div>
                    <div className='about-button'>
                        <h1><Link to='/login'>Try DiverX</Link></h1>
                    </div>
                </div>
            </div>
        </div>
        );
    }
}

export default About;