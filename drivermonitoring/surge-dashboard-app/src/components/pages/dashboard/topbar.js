import React, { Component } from 'react';
import avatar from '../resources/avatar.png';
class TopBar extends Component {

    state= {
        name: 'Festus Murimi',
        image: avatar
    }

    render() { 
        return (
        <div className='topbar'>

            <div className='topbar-text'>
                <h1>{this.props.page}</h1>
            </div>

            <div className='topbar-icons'>

                <div className='topbar-name-avatar'>
                    <h1 className='topbar-name'>{this.state.name}</h1>
                    <img src={this.state.image}/>
                </div>

            </div>
        </div>
        );
    }
}

export default TopBar;