import api from "../../../services/api/axios";

const API =
    "/users";

const login = async (
    credentials
) => {

    const response =
        await api.post(

            `${API}/login/`,

            credentials
        );

    // SAVE TOKENS

    localStorage.setItem(
        "access",
        response.data.access
    );

    localStorage.setItem(
        "refresh",
        response.data.refresh
    );

    return response.data;
};

const me = async () => {

    const response =
        await api.get(

            `${API}/me/`
        );

    return response.data;
};

export default {
    login,
    me,
};