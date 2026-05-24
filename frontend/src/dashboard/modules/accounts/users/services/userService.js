import api from "../../../../../services/api/axios";


const userService = {

    // =====================================
    // GET ALL USERS
    // =====================================

    getUsers: async (
        params = {}
    ) => {

        const response = await api.get(

            "/users/",

            {
                params,
            }
        );

        return response.data;
    },


    // =====================================
    // GET SINGLE USER
    // =====================================

    getUser: async (
        id
    ) => {

        const response = await api.get(

            `/users/${id}/`
        );

        return response.data;
    },


    // =====================================
    // CREATE USER
    // =====================================

    createUser: async (
        data
    ) => {

        const response = await api.post(

            "/users/",

            data,

            {
                headers: {

                    "Content-Type":
                        "multipart/form-data",
                },
            }
        );

        return response.data;
    },


    // =====================================
    // UPDATE USER
    // =====================================

    updateUser: async (

        id,

        data

    ) => {

        const response = await api.patch(

            `/users/${id}/`,

            data,

            {
                headers: {

                    "Content-Type":
                        "multipart/form-data",
                },
            }
        );

        return response.data;
    },


    // =====================================
    // DELETE USER
    // =====================================

    deleteUser: async (
        id
    ) => {

        const response = await api.delete(

            `/users/${id}/`
        );

        return response.data;
    },


    // =====================================
    // ASSIGN ROLES TO USER
    // =====================================

    assignRoles: async (

        userId,

        roles

    ) => {

        const response = await api.post(

            `/users/${userId}/roles/`,

            {
                roles,
            }
        );

        return response.data;
    },
};


export default userService;