import api from "../../../../../services/api/axios";


const roleService = {

    // =====================================
    // GET ALL ROLES
    // =====================================

    getRoles: async (
        params = {}
    ) => {

        const response = await api.get(

            "/accounts/roles/",

            {
                params,
            }
        );

        return response.data.data;
    },


    // =====================================
    // GET SINGLE ROLE
    // =====================================

    getRole: async (
        id
    ) => {

        const response = await api.get(

            `/accounts/roles/${id}/`
        );

        return response.data.data;
    },


    // =====================================
    // CREATE ROLE
    // =====================================

    createRole: async (
        data
    ) => {

        const response = await api.post(

            "/accounts/roles/",

            data
        );

        return response.data.data;
    },


    // =====================================
    // UPDATE ROLE
    // =====================================

    updateRole: async (

        id,

        data

    ) => {

        const response = await api.patch(

            `/accounts/roles/${id}/`,

            data
        );

        return response.data.data;
    },


    // =====================================
    // DELETE ROLE
    // =====================================

    deleteRole: async (
        id
    ) => {

        const response = await api.delete(

            `/accounts/roles/${id}/`
        );

        return response.data.data;
    },
};


export default roleService;