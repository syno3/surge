import React, { useState, useCallback, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';
import image from '../resources/login-image.svg'
import googleicon from '../resources/google.svg'
import {getAuth} from 'firebase/auth'
import {createUserWithEmailAndPassword, signInWithEmailAndPassword} from 'firebase/auth'
import {useAuth} from '../../../context/auth'
import useMounted from '../../../hooks/mounted'


const SignIn = () => {
    const [signin] = useState(true)
    return (
        <div className='login'>
            <div className='login-content'>
                <div className='login-left-text'>
                    <h1>#1 Driver monitoring system in the country</h1>
                    <img src={image}/>
                </div>
                <div className='login-card-right'>
                    {signin ? Cardbuttonsignin() : Cardbuttonsignup()}
                </div>
            </div>
        </div>
        );
}

const Cardbuttonsignup = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [isSubmitting, setIsSubmitting] = useState(false)

    return ( 
        <React.Fragment>              
            <div className='card-button'>
                <button className='signin-button'>Sign In</button>
                <button className='signup-button'>Sign Up</button>
            </div>
            <div className='card-forms'>

                <form onSubmit={HandleSignUp(email, password, setIsSubmitting)}>
                    <ul>
                        <li>
                            <input value={email} onChange={e => setEmail(e.target.value)} type='text' id="email" name="email" className='field-full' placeholder="Email" required/>
                        </li>
                        <li>
                            <input value={password} onChange={e => setPassword(e.target.value)} type='password' id="password" name="password" className='field-full' placeholder="Password"/>
                        </li>
                        <li>
                            <input isLoading={isSubmitting} type="submit" value="Lets Go!" />
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

const Cardbuttonsignin = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [isSubmitting, setIsSubmitting] = useState(false)

    const {signInWithGoogle} = useAuth();


    return ( 
        <React.Fragment>              
            <div className='card-button card-button-update'>
                <button className='signup-button signup-button-update'>Sign In</button>
                <button className='signin-button signin-button-update'>Sign Up</button>
            </div>
            <div className='card-forms card-forms-padding'>
                <form onSubmit={HandleSignIn(email, password, setIsSubmitting)}>
                    <ul>
                        <li>
                            <input value={email} onChange={e => setEmail(e.target.value)} type='text' id="email" name="email" className='field-full' placeholder="Use Email" required/>
                        </li>
                        <li>
                            <input value={password} onChange={e => setPassword(e.target.value)} type='password' id="password" name="password" className='field-full signin-padding' placeholder="Password" required/>
                        </li>
                        <li>
                            <input isLoading={isSubmitting} type="submit" value="Lets Continue!" />
                        </li>
                    </ul>
                </form>
            </div>
            <div onClick={() => signInWithGoogle()} className='card-google-auth'>
                <img src={googleicon}/>
                <h1>Sign In with google</h1>
            </div>
            <div className='card-footer-text'>
                <h2>By clicking the button you agree our <Link to=''>Terms of use</Link> and <Link to=''>Privacy policy</Link></h2>
            </div>
        </React.Fragment>
        );
}

/* adds user to the database */
const HandleSignUp = (email, password, setIsSubmitting) =>{
    const history = useHistory('')
    const mounted = useMounted()

    return (
        useCallback(async event => {
        event.preventDefault();
        setIsSubmitting(true)
        const auth = getAuth();

        try {
            await
                createUserWithEmailAndPassword(auth, email, password);
        } catch (error) {
            alert(error.message);
            }
        (mounted.current && setIsSubmitting(false))
        console.log('successful signup')
        history.push('/dashboard')
        }))
}


/* logins in back the user to website */
const HandleSignIn = (email, password, setIsSubmitting) => {
    const history = useHistory('')
    const mounted = useMounted()

    return (
        useCallback(async event => {
        event.preventDefault();
        setIsSubmitting(true)
        const auth = getAuth();

        try {
            await
                signInWithEmailAndPassword(auth, email, password);
        } catch (error) {
            alert(error.message);
            }
        (mounted.current && setIsSubmitting(false))
        console.log('successful login')
        history.push('./dashboard')
        }))
}






export default SignIn;

/* we write functions to for form submit to handle signin and signup */