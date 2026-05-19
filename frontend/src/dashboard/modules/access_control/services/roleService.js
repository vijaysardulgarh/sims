import api from "../../../services/api";


const roleService = {

    // =====================================
    // GET ALL ROLES
    // =====================================

    getRoles: async (params = {}) => {

        const response = await api.get(

            "/roles/",

            {
                params,
            }
        );

        return response.data;
    },


    // =====================================
    // GET SINGLE ROLE
    // =====================================

    getRole: async (id) => {

        const response = await api.get(

            `/roles/${id}/`
        );

        return response.data;
    },


    // =====================================
    // CREATE ROLE
    // =====================================

    createRole: async (data) => {

        const response = await api.post(

            "/roles/",

            data
        );

        return response.data;
    },


    // =====================================
    // UPDATE ROLE
    // =====================================

    updateRole: async (

        id,

        data

    ) => {

        const response = await api.patch(

            `/roles/${id}/`,

            data
        );

        return response.data;
    },


    // =====================================
    // DELETE ROLE
    // =====================================

    deleteRole: async (id) => {

        const response = await api.delete(

            `/roles/${id}/`
        );

        return response.data;
    },
};


export default roleService;