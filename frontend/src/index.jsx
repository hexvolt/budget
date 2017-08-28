import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import App from './components/app'
import rootReducer from './reducers'


ReactDOM.render((
  <Provider store={createStore(rootReducer)}>
    {/* makes `store` available in the context for all children */}
    <App />
  </Provider>
), document.getElementById('root'));
