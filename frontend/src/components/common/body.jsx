import React from 'react';
import {
  Route,
  Switch
} from 'react-router-dom';
import Home from '../home';
import Dashboard from '../dashboard';
import Login from '../auth/login';
import { EnsureLoggedInContainer } from '../auth/utils';
import Routes from "../routes";


const Body = () => {
  return (
    <Switch>
      <Route exact path={Routes.HOME} component={Home} />
      <Route exact path={Routes.LOGIN} component={Login} />

      <EnsureLoggedInContainer>
        <Route path={Routes.DASHBOARD} component={Dashboard} />
      </EnsureLoggedInContainer>
    </Switch>
  )
};

export default Body;
