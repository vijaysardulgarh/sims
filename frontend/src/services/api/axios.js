import axios from "axios";

const api = axios.create({

    baseURL: "http://localhost:8000/api/",
});


api.interceptors.request.use(

    (config) => {

        const token =
            localStorage.getItem("access");

        console.log("TOKEN:", token);

        if (token) {

            config.headers.Authorization =
                `Bearer ${token}`;

            console.log(
                "HEADER SET:",
                config.headers.Authorization
            );
        }

        return config;
    },

    (error) => {

        return Promise.reject(error);
    }
);

export default api;