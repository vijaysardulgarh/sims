import api
from "../../services/api/axios";


const login = async (
  credentials
) => {

  const response =
    await api.post(

      "/users/login/",

      credentials
    );

  return response.data;
};


const getCurrentUser =
  async () => {

  const response =
    await api.get(
      "/users/me/"
    );

  return response.data;
};


export default {

  login,

  getCurrentUser,
};