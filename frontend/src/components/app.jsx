import React from 'react';
import {
  BrowserRouter,
  Route,
  Switch
} from 'react-router-dom';
import Home from './home';
import Dashboard from './dashboard';
import Login from './auth/login';
import { EnsureLoggedInContainer } from './auth/utils';


const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/login" component={Login} />

        <Route component={EnsureLoggedInContainer}>
          <Route path="/dash" component={Dashboard} />
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default App;
