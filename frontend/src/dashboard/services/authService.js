import api from "./api";

const authService = {

  login: async (data) => {
    const response = await api.post(
      "/auth/login/",
      data
    );

    return response.data;
  },

  logout: () => {
    localStorage.removeItem("token");
  },

  getProfile: async () => {
    const response = await api.get(
      "/auth/profile/"
    );

    return response.data;
  },

};

export default authService;