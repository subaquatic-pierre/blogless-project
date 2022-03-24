const parseResponse = (response) => {
  if (response.data.error && response.data.error.message)
    return response.data.error.message;
  else {
    return false;
  }
};

export default parseResponse;
