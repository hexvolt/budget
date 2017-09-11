import React from 'react';

const ErrorList = ({errors}) => (
  <ul className="errors">
    { errors && errors.map((error, i) => (<li key={i}>{error}</li>)) }
  </ul>
);


export {
  ErrorList,
}