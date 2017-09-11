import { combineReducers } from 'redux';

const loggedIn = (state = false, action) => {
  return action.type === 'LOGGED_IN' ? true: state;
};

const token = (state = '', action) => {
  return action.type === 'LOGGED_IN' ? action.token: state;
};

export default combineReducers({
  loggedIn,
  token,
});
