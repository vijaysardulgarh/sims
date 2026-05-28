// ============================================
// IMPORTS
// ============================================

import api from '../../../../../services/api/axios';

// ============================================
// API ENDPOINT
// ============================================

const BASE_URL = '/associations/associations/';

// ============================================
// ASSOCIATION SERVICE
// ============================================

const associationService = {

    // ========================================
    // GET ALL
    // ========================================

    getAll: async () => {

        const response = await api.get(
            BASE_URL
        );

        return response.data;
    },

    // ========================================
    // GET DETAIL
    // ========================================

    getById: async (id) => {

        const response = await api.get(
            `${BASE_URL}committees/${id}/`
        );

        return response.data;
    },

    // ========================================
    // CREATE
    // ========================================

    create: async (data) => {

        const response = await api.post(
            BASE_URL,
            data
        );

        return response.data;
    },

    // ========================================
    // UPDATE
    // ========================================

    update: async (id, data) => {

        const response = await api.put(
            `${BASE_URL}${id}/`,
            data
        );

        return response.data;
    },

    // ========================================
    // DELETE
    // ========================================

    delete: async (id) => {

        const response = await api.delete(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },
};

export default associationService;