import api from "../../../../../services/api/axios";


const PermissionService = {

    // =====================================
    // GET PERMISSIONS
    // =====================================

    getPermissions: async (
        params = {}
    ) => {

        const response = await api.get(

            "/accounts/permissions/",

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

            `/accounts/permissions/${id}/`
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

            "/accounts/permissions/",

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

            `/accounts/permissions/${id}/`,

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

            `/accounts/permissions/${id}/`
        );

        return response.data;
    },
};


export default PermissionService;