// ============================================
// IMPORTS
// ============================================

import api from '../../../../../services/api/axios';

// ============================================
// BASE URL
// ============================================

const BASE_URL =
    '/associations/association-roles/';

// ============================================
// SERVICE
// ============================================

const associationRoleService = {

    // ========================================
    // GET ALL
    // ========================================

    getAll: async () => {

        const response =
            await api.get(
                BASE_URL
            );

        return response;
    },

    // ========================================
    // GET BY ID
    // ========================================

    getById: async (id) => {

        const response =
            await api.get(
                `${BASE_URL}${id}/`
            );

        return response;
    },

    // ========================================
    // CREATE
    // ========================================

    create: async (data) => {

        const response =
            await api.post(
                BASE_URL,
                data
            );

        return response;
    },

    // ========================================
    // UPDATE
    // ========================================

    update: async (
        id,
        data
    ) => {

        const response =
            await api.put(
                `${BASE_URL}${id}/`,
                data
            );

        return response;
    },

    // ========================================
    // DELETE
    // ========================================

    delete: async (id) => {

        const response =
            await api.delete(
                `${BASE_URL}${id}/`
            );

        return response;
    },
};

export default associationRoleService;