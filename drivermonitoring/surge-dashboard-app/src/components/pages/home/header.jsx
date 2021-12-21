import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import stars from '../resources/stars.svg';



class Header extends Component {
    render() { 
        return (
        <div className='header'>
            <div className='navcontent'>
                <div className='logo'>
                    <h1>SURGE</h1>
                </div>
                <div className="nav-right-content">
                    <h1 className='nav-about-text'>About us</h1>
                    <div className='nav-right-button'>
                        <h1 className='buttontext'><Link to='/login'>Try DiverX</Link></h1>
                    </div>
                </div>
            </div>
            <div className='headercontent'>
                <div className='textcontent'> 
                    <h1 className='line-height'>Making Driving safer</h1>
                    <p>We are redefining the standards of saftey in the transportation industry.</p>
                    <div className='searchbox'>
                        <div className='seacrhboxbtn'>
                            <h1>Get Started</h1>
                        </div>
                    </div>
                </div>
                <div className='image mobile-image'>
                    <img src={stars} alt='image' />
                </div>
            </div>
        </div>
        );
    }
}


export default Header;
