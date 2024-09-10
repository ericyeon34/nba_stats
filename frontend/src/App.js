import logo from './logo.svg';
import './App.css';

import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Navbar from './components/Navbar';

import PlayersList from './components/fetchPlayers';

const App = () => {
  return (
    <Router>
      <div className='App'>
        <Navbar />
        <Routes>
          {/* <Route exact path='/' component={Home} /> */}
          <Route exact path='/components/Navbar' component={Navbar} />
          {/* <Route exact path='/players' component={Players} /> */}
        </Routes>
        <main>
          {<PlayersList />}
        </main>
      </div>
    </Router>
  )
}

export default App;
