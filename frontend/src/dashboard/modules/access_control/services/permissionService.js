import api from "../../../../services/api/axios";


const permissionService = {

    // =====================================
    // GET ALL PERMISSIONS
    // =====================================

    getPermissions: async (
        params = {}
    ) => {

        try {

            const response = await api.get(

                "/users/permissions/",

                {
                    params,
                }
            );

            // =============================
            // DEBUG
            // =============================

            console.log(
                "PERMISSION RESPONSE:",
                response
            );

            console.log(
                "PERMISSION DATA:",
                response.data
            );

            return response.data;

        } catch (error) {

            // =============================
            // FULL DEBUG
            // =============================

            console.log(
                "FULL ERROR:",
                error
            );

            console.log(
                "ERROR RESPONSE:",
                error.response
            );

            console.log(
                "ERROR DATA:",
                error.response?.data
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

                `/users/permissions/${id}/`
            );

            console.log(
                "GET PERMISSION:",
                response.data
            );

            return response.data;

        } catch (error) {

            console.log(
                "GET PERMISSION ERROR:",
                error.response?.data
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

                "/users/permissions/",

                data
            );

            console.log(
                "CREATE RESPONSE:",
                response.data
            );

            return response.data;

        } catch (error) {

            console.log(
                "CREATE ERROR:",
                error.response?.data
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

                `/users/permissions/${id}/`,

                data
            );

            console.log(
                "UPDATE RESPONSE:",
                response.data
            );

            return response.data;

        } catch (error) {

            console.log(
                "UPDATE ERROR:",
                error.response?.data
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

                `/users/permissions/${id}/`
            );

            console.log(
                "DELETE RESPONSE:",
                response.data
            );

            return response.data;

        } catch (error) {

            console.log(
                "DELETE ERROR:",
                error.response?.data
            );

            throw error;
        }
    },


    // =====================================
    // ASSIGN ROLE PERMISSIONS
    // =====================================

    assignPermissionsToRole: async (

        roleId,

        permissions

    ) => {

        try {

            const response = await api.post(

                `/users/roles/${roleId}/permissions/`,

                {
                    permissions,
                }
            );

            console.log(
                "ASSIGN RESPONSE:",
                response.data
            );

            return response.data;

        } catch (error) {

            console.log(
                "ASSIGN ERROR:",
                error.response?.data
            );

            throw error;
        }
    },
};


export default permissionService;