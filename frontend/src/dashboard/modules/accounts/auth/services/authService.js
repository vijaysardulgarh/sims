import api from
"../../../../../services/api/axios";


const API = "/accounts";


// =====================================
// LOGIN
// =====================================

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


// =====================================
// CURRENT USER
// =====================================

const getCurrentUser =
    async () => {

    const response =
        await api.get(

            `${API}/current-user/`
        );

    return response.data;
};


// =====================================
// LOGOUT
// =====================================

const logout = async () => {

    try {

        const refresh =
            localStorage.getItem(
                "refresh"
            );

        if (refresh) {

            await api.post(

                `${API}/logout/`,

                {
                    refresh,
                }
            );
        }

    } catch (error) {

        console.error(error);

    } finally {

        localStorage.removeItem(
            "access"
        );

        localStorage.removeItem(
            "refresh"
        );
    }
};


export default {

    login,

    getCurrentUser,

    logout,
};