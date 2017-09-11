const setLoggedIn = (token) => {
  return {'type': 'LOGGED_IN', 'token': token}
};

export {
  setLoggedIn,
}