import React, { Component } from 'react';
import { Link } from 'react-router-dom';


class Footer extends React.Component {
    render() { 
        return (
        <div className='footer'>
            <div className='footer-text'>
                <h1>Join our newsletter</h1>
                <p>If you are interested in helping us build the future, join our email list and receivce important details on our progress</p>
                <div className='searchbox'>
                    <div className='seacrhboxbtn'>
                        <h1 className='footer-button-text'>Submit</h1>
                    </div>
                </div>
            </div>
            <div className='footer-links'>
                <h1 className='footer-logo'><Link to='/'>Surge</Link></h1>
                <h1 className='footer-twitter'>Twitter</h1>
            </div>
        </div>
        );
    }
}
export default Footer;