import api from "@/services/api";

const BASE_URL =
    "/transport/transport-routes/";


const transportRouteService = {

    getRoutes: async () => {

        const response = await api.get(
            BASE_URL
        );

        return response.data;
    },

    getRoute: async (id) => {

        const response = await api.get(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },

    createRoute: async (data) => {

        const response = await api.post(
            BASE_URL,
            data
        );

        return response.data;
    },

    updateRoute: async (id, data) => {

        const response = await api.put(
            `${BASE_URL}${id}/`,
            data
        );

        return response.data;
    },

    deleteRoute: async (id) => {

        const response = await api.delete(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },
};

export default transportRouteService;