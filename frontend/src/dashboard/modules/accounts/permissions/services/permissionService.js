import api from "../../../../../services/api/axios";


const PermissionService = {

    getPermissions: async (
        params = {}
    ) => {

        const response = await api.get(

            "/accounts/permissions/",

            {
                params,
            }
        );

        console.log(
            "RAW API RESPONSE:",
            response.data
        );

        return response.data;
    },


    getPermission: async (
        id
    ) => {

        const response = await api.get(

            `/accounts/permissions/${id}/`
        );

        return response.data;
    },


    createPermission: async (
        data
    ) => {

        const response = await api.post(

            "/accounts/permissions/",

            data
        );

        return response.data;
    },


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