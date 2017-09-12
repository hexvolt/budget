import React from 'react';
import {
  Route,
  Switch
} from 'react-router-dom';
import Home from 'components/home';
import Dashboard from 'components/dashboard';
import Login from 'components/auth/login';
import { EnsureLoggedInContainer } from 'components/auth/utils';
import Routes from "routes";


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
