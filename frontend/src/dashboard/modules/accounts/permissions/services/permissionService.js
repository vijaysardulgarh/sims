import api from "../../../../../services/api/axios";


const accessControlService = {

    // =====================================
    // GET ALL ACCESS CONTROLS
    // =====================================

    getAccessControls: async (
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
    // GET SINGLE ACCESS CONTROL
    // =====================================

    getAccessControl: async (
        id
    ) => {

        const response = await api.get(

            `/users/permissions/${id}/`
        );

        return response.data;
    },


    // =====================================
    // CREATE ACCESS CONTROL
    // =====================================

    createAccessControl: async (
        data
    ) => {

        const response = await api.post(

            "/users/permissions/",

            data
        );

        return response.data;
    },


    // =====================================
    // UPDATE ACCESS CONTROL
    // =====================================

    updateAccessControl: async (

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
    // DELETE ACCESS CONTROL
    // =====================================

    deleteAccessControl: async (
        id
    ) => {

        const response = await api.delete(

            `/users/permissions/${id}/`
        );

        return response.data;
    },
};


export default accessControlService;