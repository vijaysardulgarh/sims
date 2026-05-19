import api from "../../../services/api";


const permissionService = {

    // =====================================
    // GET ALL PERMISSIONS
    // =====================================

    getPermissions: async () => {

        const response = await api.get(

            "/permissions/"
        );

        return response.data;
    },


    // =====================================
    // ASSIGN ROLE PERMISSIONS
    // =====================================

    assignPermissionsToRole: async (

        roleId,

        permissions

    ) => {

        const response = await api.post(

            `/roles/${roleId}/permissions/`,

            {
                permissions,
            }
        );

        return response.data;
    },
};


export default permissionService;