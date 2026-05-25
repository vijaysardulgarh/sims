import api from "../../../../../services/api/axios";


const rolePermissionService = {

    // =====================================
    // GET ROLE PERMISSIONS
    // =====================================

    getRolePermissions: async (
        roleId
    ) => {

        try {

            const response = await api.get(

                `/accounts/role-permissions/roles/${roleId}/permissions/`
            );

            return response.data;

        } catch (error) {

            console.error(error);

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

                `/accounts/role-permissions/roles/${roleId}/permissions/`,

                {
                    permissions,
                }
            );

            return response.data;

        } catch (error) {

            console.error(error);

            throw error;
        }
    },
};


export default rolePermissionService;