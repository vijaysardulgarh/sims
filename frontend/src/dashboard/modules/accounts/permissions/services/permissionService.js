import api from "../../../../../services/api/axios";


const PermissionService = {

    // =====================================
    // GET ALL PERMISSIONS
    // =====================================

    getPermissions: async (
        params = {}
    ) => {

        const response = await api.get(

            "/users/permissions/",

            {
                params,
            }
        );

        return response.data;
    },


    // =====================================
    // GET SINGLE PERMISSION
    // =====================================

    getPermission: async (
        id
    ) => {

        const response = await api.get(

            `/users/permissions/${id}/`
        );

        return response.data;
    },


    // =====================================
    // CREATE PERMISSION
    // =====================================

    createPermission: async (
        data
    ) => {

        const response = await api.post(

            "/users/permissions/",

            data
        );

        return response.data;
    },


    // =====================================
    // UPDATE PERMISSION
    // =====================================

    updatePermission: async (

        id,

        data

    ) => {

        const response = await api.patch(

            `/users/permissions/${id}/`,

            data
        );

        return response.data;
    },


    // =====================================
    // DELETE PERMISSION
    // =====================================

    deletePermission: async (
        id
    ) => {

        const response = await api.delete(

            `/users/permissions/${id}/`
        );

        return response.data;
    },
};


export default PermissionService;