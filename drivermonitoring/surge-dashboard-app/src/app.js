import React from 'react';

import './index.css';
import './about.css';
import './footer.css';
import './login.css'
import './dashboard.css'

import Home from './components/home'
import Login from './components/login'
import Dashboard from './components/dashboard';
import NotFound from './components/404';

import {Route, BrowserRouter, Switch} from "react-router-dom"

class App extends React.Component {
    render() { 
        return (
        <BrowserRouter>
            <React.Fragment>
                <Switch>
                    <Route path='/' component={Home} exact/>
                    <Route path='/login' component={Login} />
                    <Route path='/dashboard' component={Dashboard} />
                    <Route component={NotFound} />
                </Switch>
            </React.Fragment>  
        </BrowserRouter>
        );
    }
}
export default App;
