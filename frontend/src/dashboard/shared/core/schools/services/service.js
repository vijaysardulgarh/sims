import api from "@/services/api";

const BASE_URL = "/core/schools/";

const schoolService = {

    getSchools: async () => {

        const response = await api.get(
            BASE_URL
        );

        return response.data;
    },

    getSchool: async (id) => {

        const response = await api.get(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },

    createSchool: async (data) => {

        const response = await api.post(
            BASE_URL,
            data
        );

        return response.data;
    },

    updateSchool: async (id, data) => {

        const response = await api.put(
            `${BASE_URL}${id}/`,
            data
        );

        return response.data;
    },

    deleteSchool: async (id) => {

        const response = await api.delete(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },
};

export default schoolService;