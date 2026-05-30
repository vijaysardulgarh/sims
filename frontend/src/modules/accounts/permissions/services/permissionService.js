import api from "../../../../services/api/axios";


const PermissionService = {

    // =====================================
    // GET PERMISSIONS
    // =====================================

    getPermissions: async (
        params = {}
    ) => {

        try {

            const response = await api.get(

                "/accounts/permissions/",

                {
                    params,
                }
            );

            return response.data;

        } catch (error) {

            console.error(
                "GET PERMISSIONS ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // GET ACTIVE PERMISSIONS
    // =====================================

    getActivePermissions: async () => {

        try {

            const response = await api.get(

                "/accounts/permissions/",

                {
                    params: {
                        is_active: true,
                    }
                }
            );

            return response.data;

        } catch (error) {

            console.error(
                "GET ACTIVE PERMISSIONS ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // GET PERMISSIONS BY MODULE
    // =====================================

    getPermissionsByModule: async (
        moduleId
    ) => {

        try {

            const response = await api.get(

                "/accounts/permissions/",

                {
                    params: {
                        module: moduleId,
                    }
                }
            );

            return response.data;

        } catch (error) {

            console.error(
                "GET MODULE PERMISSIONS ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // GET SINGLE PERMISSION
    // =====================================

    getPermission: async (
        id
    ) => {

        try {

            const response = await api.get(

                `/accounts/permissions/${id}/`
            );

            return response.data;

        } catch (error) {

            console.error(
                "GET PERMISSION ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // CREATE PERMISSION
    // =====================================

    createPermission: async (
        data
    ) => {

        try {

            const response = await api.post(

                "/accounts/permissions/",

                data
            );

            return response.data;

        } catch (error) {

            console.error(
                "CREATE PERMISSION ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // UPDATE PERMISSION
    // =====================================

    updatePermission: async (

        id,

        data

    ) => {

        try {

            const response = await api.patch(

                `/accounts/permissions/${id}/`,

                data
            );

            return response.data;

        } catch (error) {

            console.error(
                "UPDATE PERMISSION ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // DELETE PERMISSION
    // =====================================

    deletePermission: async (
        id
    ) => {

        try {

            const response = await api.delete(

                `/accounts/permissions/${id}/`
            );

            return response.data;

        } catch (error) {

            console.error(
                "DELETE PERMISSION ERROR:",
                error
            );

            throw error;
        }
    },


    // =====================================
    // BULK CREATE PERMISSIONS
    // =====================================

    bulkCreatePermissions: async (
        permissions
    ) => {

        try {

            const response = await api.post(

                "/accounts/permissions/bulk-create/",

                {
                    permissions,
                }
            );

            return response.data;

        } catch (error) {

            console.error(
                "BULK CREATE PERMISSIONS ERROR:",
                error
            );

            throw error;
        }
    },
};


export default PermissionService;