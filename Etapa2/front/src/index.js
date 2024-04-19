import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App'; 
import HomePage from './HomePage'; 
import AppTexto from './AppTexto'; 

ReactDOM.render(
  <Router>
    <Switch>
      <Route exact path="/" component={HomePage} />
      <Route exact path="/app" component={App} />
      <Route exact path="/appTexto" component={AppTexto} />
    </Switch>
  </Router>,
  document.getElementById('root')
);
