// src/modules/schools/services/schoolService.js

import api from "../../../../services/api/axios";

const BASE_URL = "/schools";

export const getSchools = async () => {
    const response = await api.get(`${BASE_URL}/`);
    return response.data;
};

export const getSchool = async (id) => {
    const response = await api.get(`${BASE_URL}/${id}/`);
    return response.data;
};

export const createSchool = async (data) => {
    const response = await api.post(
        `${BASE_URL}/`,
        data,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};

export const updateSchool = async (
    id,
    data
) => {

    const response = await api.put(
        `${BASE_URL}/${id}/`,
        data,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};

export const deleteSchool = async (id) => {
    const response = await api.delete(
        `${BASE_URL}/${id}/`
    );

    return response.data;
};