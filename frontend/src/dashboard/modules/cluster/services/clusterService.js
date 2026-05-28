// src/modules/clusters/services/clusterService.js

import api from "../../../../services/api/axios";

const BASE_URL = "/clusters";

export const getClusters = async () => {

    const response =
        await api.get(`${BASE_URL}/`);

    return response.data;
};

export const getCluster = async (id) => {

    const response =
        await api.get(
            `${BASE_URL}/${id}/`
        );

    return response.data;
};

export const createCluster = async (
    data
) => {

    const response =
        await api.post(

            `${BASE_URL}/`,

            data,

            {
                headers: {
                    "Content-Type":
                        "multipart/form-data",
                },
            }
        );

    return response.data;
};

export const updateCluster = async (
    id,
    data
) => {

    const response =
        await api.put(

            `${BASE_URL}/${id}/`,

            data,

            {
                headers: {
                    "Content-Type":
                        "multipart/form-data",
                },
            }
        );

    return response.data;
};

export const deleteCluster = async (
    id
) => {

    const response =
        await api.delete(
            `${BASE_URL}/${id}/`
        );

    return response.data;
};