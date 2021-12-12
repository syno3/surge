import React from 'react';
import Header from './pages/home/header';
import About from './pages/home/about'
import Footer from './pages/home/footer'


class Home extends React.Component {
    render() { 
        return (
        <React.Fragment>
            <Header />
            <About />
            <Footer />
        </React.Fragment>
        );
    }
}
export default Home;