import api from "../../../../../services/api/axios";


const userRoleService = {

    getUserRoles: async () => {

        const response = await api.get(
            "/accounts/user-roles/"
        );

        return response.data;
    },


    getUserRole: async (id) => {

        const response = await api.get(
            `/accounts/user-roles/${id}/`
        );

        return response.data;
    },


    createUserRole: async (data) => {

        const response = await api.post(

            "/accounts/user-roles/",

            data
        );

        return response.data;
    },


    updateUserRole: async (
        id,
        data
    ) => {

        const response = await api.patch(

            `/accounts/user-roles/${id}/`,

            data
        );

        return response.data;
    },


    deleteUserRole: async (id) => {

        const response = await api.delete(

            `/accounts/user-roles/${id}/`
        );

        return response.data;
    },
};

export default userRoleService;