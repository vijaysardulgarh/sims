import api from "./axios";


export const setupInterceptors = (
    logout
) => {

    api.interceptors.request.use(

        (config) => {

            const token =
                localStorage.getItem(
                    "access"
                );

            if (token) {

                config.headers.Authorization =
                    `Bearer ${token}`;
            }

            return config;
        },

        (error) => {

            return Promise.reject(
                error
            );
        }
    );

    api.interceptors.response.use(

        (response) => response,

        (error) => {

            if (
                error.response?.status === 401
            ) {

                logout();
            }

            return Promise.reject(
                error
            );
        }
    );
};