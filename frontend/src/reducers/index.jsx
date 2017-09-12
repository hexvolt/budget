import { combineReducers } from 'redux';
import auth from "./auth";


const rootReducer = combineReducers({
  auth,
  //<state-key>: <reducer-to-manage-it>
});

export default rootReducer;