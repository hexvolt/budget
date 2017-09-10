const checkApiResponseStatus = (response) => {
  if (response.ok)
    return Promise.resolve(response);

  return response.json().then(data => {
    const error = new Error(data);
    return Promise.reject(Object.assign(error, {data}))
  });
};

export {
  checkApiResponseStatus,
};