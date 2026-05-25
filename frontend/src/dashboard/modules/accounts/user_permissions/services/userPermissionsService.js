// =========================================
// FILE:
// frontend/src/modules/accounts/user_permissions/services/userPermissionsService.js
// =========================================

import api from "../../../../../services/api/axios";


const userPermissionsService = {

    // =====================================
    // GET USER PERMISSIONS
    // =====================================

    getUserPermissions: async () => {

        try {

            const response = await api.get(

                "/accounts/user-permissions/"
            );

            return response.data;

        } catch (error) {

            console.error(
                "GET USER PERMISSIONS ERROR:",
                error
            );

            throw error;
        }
    },
};


export default userPermissionsService;