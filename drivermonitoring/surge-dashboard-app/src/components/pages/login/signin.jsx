import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import image from '../resources/login-image.svg'
import googleicon from '../resources/google.svg'


class SignIn extends React.Component {

    /* we create state the updates */
    state = {
        status: false,
    };

    /* the main render function */
    render() { 
        return (
        <div className='login'>
            <div className='login-content'>
                <div className='login-left-text'>
                    <h1>#1 Driver monitoring system in the country</h1>
                    <img src={image}/>
                </div>
                <div className='login-card-right'>
                    {this.state.status ? this.cardbuttonsignin() : this.cardbuttonsignup()}
                </div>
            </div>
        </div>
        );
    }

    cardbuttonsignup(){
        return ( 
        <React.Fragment>              
            <div className='card-button'>
                <button className='signin-button'>Sign In</button>
                <button className='signup-button'>Sign Up</button>
            </div>
            <div className='card-forms'>
                <form>
                    <ul>
                        <li>
                            <input type='text' id="fname" name="fname" className='field-split align-left' placeholder="First Name"/>
                            <input type='text' id="lname" name="lname" className='field-split align-right' placeholder="Last Name"/>
                        </li>
                        <li>
                            <input type='text' id="email" name="email" className='field-full' placeholder="Email"/>
                        </li>
                        <li>
                            <input type='password' id="password" name="password" className='field-full' placeholder="Password"/>
                        </li>
                        <li>
                            <input type="submit" value="Lets Go!" />
                        </li>
                    </ul>
                </form>
            </div>
            <div className='card-google-auth'>
                <img src={googleicon}/>
                <h1>Sign up with google</h1>
            </div>
            <div className='card-footer-text'>
                <h2>By clicking the button you agree our <Link to=''>Terms of use</Link> and <Link to=''>Privacy policy</Link></h2>
            </div>
        </React.Fragment>
        );
    }


    cardbuttonsignin(){
        return ( 
        <React.Fragment>              
            <div className='card-button card-button-update'>
                <button className='signup-button signup-button-update'>Sign In</button>
                <button className='signin-button signin-button-update'>Sign Up</button>
            </div>
            <div className='card-forms card-forms-padding'>
                <form>
                    <ul>
                        <li>
                            <input type='text' id="email" name="email" className='field-full' placeholder="Use Email or Password"/>
                        </li>
                        <li>
                            <input type='password' id="password" name="password" className='field-full signin-padding' placeholder="Password"/>
                        </li>
                        <li>
                            <input type="submit" value="Lets Continue!" />
                        </li>
                    </ul>
                </form>
            </div>
            <div className='card-google-auth'>
                <img src={googleicon}/>
                <h1>Sign In with google</h1>
            </div>
            <div className='card-footer-text'>
                <h2>By clicking the button you agree our <Link to=''>Terms of use</Link> and <Link to=''>Privacy policy</Link></h2>
            </div>
        </React.Fragment>
        );
    }

    /* we will this function to update state when button clicked  */
    constructor(){
        super();
        this.statesignin = this.statesignin.bind(this);
        this.statesignup = this.statesignup.bind(this);
    }

    statesignin(){
        this.setState({status: true});
    }

    statesignup(){
        this.setState({status: false})
    }
}

export default SignIn;