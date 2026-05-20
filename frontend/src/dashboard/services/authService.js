import api from "../../../services/api/axios";

const authService = {

    login: async (data) => {

        const response = await api.post(
            "/auth/login/",
            data
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
    },

    logout: () => {

        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
    },

    getProfile: async () => {

        const response = await api.get(
            "/auth/profile/"
        );

        return response.data;
    },
};

export default authService;