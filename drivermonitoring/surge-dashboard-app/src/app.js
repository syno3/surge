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
import AuthContextprovider from './context/auth'
class App extends React.Component {
    render() { 
        return (
        <AuthContextprovider>
            <BrowserRouter>
                <Switch>
                    <Route path='/' component={Home} exact/>
                    <Route path='/login' component={Login} />
                    <Route path='/dashboard' component={Dashboard} />
                    <Route component={NotFound} />
                </Switch>
            </BrowserRouter>
        </AuthContextprovider>
        );
    }
}
export default App;
