import axios from "axios";

const api = axios.create({

  baseURL:
    "http://localhost:8000/api",

  timeout: 120000,

  headers: {

    "Content-Type":
      "application/json",
  },
});


// =========================================
// REQUEST INTERCEPTOR
// =========================================

api.interceptors.request.use(

  (config) => {

    console.log(
      "API REQUEST:",
      config.url
    );

    const token =
      localStorage.getItem(
        "token"
      );

    if (token) {

      config.headers.Authorization =
        `Bearer ${token}`;
    }

    return config;
  },

  (error) => {

    console.error(
      "REQUEST ERROR:",
      error
    );

    return Promise.reject(error);
  }
);


// =========================================
// RESPONSE INTERCEPTOR
// =========================================

api.interceptors.response.use(

  (response) => {

    console.log(
      "API RESPONSE:",
      response
    );

    return response;
  },

  (error) => {

    console.error(
      "API ERROR:",
      error
    );

    if (error.response?.status === 401) {

      localStorage.removeItem(
        "token"
      );

      window.location.href =
        "/login";
    }

    return Promise.reject(error);
  }
);

export default api;