import React from 'react';
import {
  BrowserRouter,
  Route,
  Switch
} from 'react-router-dom';
import About from './about';
import Dashboard from './dashboard';
import Login from './auth/login';
import { EnsureLoggedInContainer } from './auth/utils';


const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/about" component={About} />

        <Route component={EnsureLoggedInContainer}>
          <Route exact path="/dashboard" component={Dashboard} />
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default App;
