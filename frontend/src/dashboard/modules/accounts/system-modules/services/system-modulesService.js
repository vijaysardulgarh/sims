import api from "../../../../services/api/axios";


// ======================================
// GET ALL MODULES
// ======================================

export const getModules = async () => {

    const response = await api.get(
        "/accounts/modules/"
    );

    return response.data;
};


// ======================================
// GET SINGLE MODULE
// ======================================

export const getModule = async (id) => {

    const response = await api.get(
        `/accounts/system-modules/${id}/`
    );

    return response.data;
};


// ======================================
// CREATE MODULE
// ======================================

export const createModule = async (data) => {

    const response = await api.post(
        "/accounts/system-modules/",
        data
    );

    return response.data;
};


// ======================================
// UPDATE MODULE
// ======================================

export const updateModule = async (id, data) => {

    const response = await api.put(
        `/accounts/system-modules/${id}/`,
        data
    );

    return response.data;
};


// ======================================
// DELETE MODULE
// ======================================

export const deleteModule = async (id) => {

    const response = await api.delete(
        `/accounts/system-modules/${id}/`
    );

    return response.data;
};