import React, { Component } from 'react';
import avatar from '../resources/avatar.png';
import {useAuth} from '../../../context/auth'


const TopBar = ({page}) => {
    const {currentUser} = useAuth();

    return (
        <div className='topbar'>

            <div className='topbar-text'>
                <h1>{page}</h1>
            </div>

            <div className='topbar-icons'>

                <div className='topbar-name-avatar'>
                    <h1 className='topbar-name'>{currentUser}</h1>
                    <img src={avatar}/>
                </div>

            </div>
        </div>
        );
}
export default TopBar;

