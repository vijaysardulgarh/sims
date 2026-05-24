import api from "../../../../../services/api/axios";


const roleService = {

    // =====================================
    // GET ALL ROLES
    // =====================================

    getRoles: async (params = {}) => {

        const response = await api.get(

            "/users/roles/",

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

            `/users/roles/${id}/`
        );

        return response.data;
    },


    // =====================================
    // CREATE ROLE
    // =====================================

    createRole: async (data) => {

        const response = await api.post(

            "/users/roles/",

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

            `/users/roles/${id}/`,

            data
        );

        return response.data;
    },


    // =====================================
    // DELETE ROLE
    // =====================================

    deleteRole: async (id) => {

        const response = await api.delete(

            `/users/roles/${id}/`
        );

        return response.data;
    },
};


export default roleService;