import React, { Component } from 'react';

class TopBar extends React.Component {

    constructor(){
        super();
        this.state = {page: 'Overview'}
    }

    render() { 
        return (
        <div className='topbar'>
            <div className='topbar-text'>
                <h1>{this.state.page}</h1>
            </div>
            <div className='topbar-icons'>
                {/* we will fix later */}
                <h1>hello</h1>
            </div>
        </div>
        );
    }
}

export default TopBar;