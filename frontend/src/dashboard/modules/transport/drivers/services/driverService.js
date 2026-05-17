import api from "@/services/api";

const BASE_URL = "/transport/drivers/";

const driverService = {

    getDrivers: async () => {

        const response = await api.get(
            BASE_URL
        );

        return response.data;
    },

    getDriver: async (id) => {

        const response = await api.get(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },

    createDriver: async (data) => {

        const response = await api.post(
            BASE_URL,
            data
        );

        return response.data;
    },

    updateDriver: async (id, data) => {

        const response = await api.put(
            `${BASE_URL}${id}/`,
            data
        );

        return response.data;
    },

    deleteDriver: async (id) => {

        const response = await api.delete(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },
};

export default driverService;