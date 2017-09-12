import React from 'react';
import { Link } from 'react-router-dom';
import Routes from "routes";


const Header = () => (
  <header>
    <nav>
      <li><Link to={Routes.HOME}>Home</Link></li>
      <li><Link to={Routes.LOGIN}>Login</Link></li>
    </nav>
  </header>
);

export default Header;