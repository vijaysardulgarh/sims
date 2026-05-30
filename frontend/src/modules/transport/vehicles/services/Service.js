import api from "@/services/api";

const BASE_URL = "/transport/vehicles/";

const vehicleService = {

    getVehicles: async () => {

        const response = await api.get(
            BASE_URL
        );

        return response.data;
    },

    getVehicle: async (id) => {

        const response = await api.get(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },

    createVehicle: async (data) => {

        const response = await api.post(
            BASE_URL,
            data
        );

        return response.data;
    },

    updateVehicle: async (id, data) => {

        const response = await api.put(
            `${BASE_URL}${id}/`,
            data
        );

        return response.data;
    },

    deleteVehicle: async (id) => {

        const response = await api.delete(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },
};

export default vehicleService;