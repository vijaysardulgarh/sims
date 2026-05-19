import axios from "axios";

const API =
    "http://127.0.0.1:8000/api/users";

const login = async (
    credentials
) => {

    const response =
        await axios.post(

            `${API}/login/`,

            credentials
        );

    return response.data;
};

const me = async (
    token
) => {

    const response =
        await axios.get(

            `${API}/me/`,

            {
                headers: {

                    Authorization:
                        `Bearer ${token}`
                }
            }
        );

    return response.data;
};

export default {
    login,
    me,
};