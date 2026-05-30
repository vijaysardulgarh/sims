import api from "../../../../services/api/axios";

const BASE_URL =
    "/associations/smc-members/";

const smcMemberService = {

    // ============================================
    // GET ALL MEMBERS
    // ============================================

    getSMCMembers: async () => {

        const response =
            await api.get(
                BASE_URL
            );

        return (
            response.data?.results ||
            response.data?.data ||
            response.data ||
            []
        );

    },

    // ============================================
    // GET SINGLE MEMBER
    // ============================================

    getSMCMember: async (
        id
    ) => {

        const response =
            await api.get(
                `${BASE_URL}${id}/`
            );

        return (
            response.data?.data ||
            response.data
        );

    },

    // ============================================
    // CREATE MEMBER
    // ============================================

    createSMCMember: async (
        data
    ) => {

        const formData =
            new FormData();

        Object.keys(data).forEach(
            (key) => {

                const value =
                    data[key];

                if (
                    value === null ||
                    value === undefined ||
                    value === ""
                ) {

                    return;

                }

                if (
                    key === "photo" &&
                    typeof value === "string"
                ) {

                    return;

                }

                formData.append(
                    key,
                    value
                );

            }
        );

        const response =
            await api.post(
                BASE_URL,
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data",
                    },
                }
            );

        return response.data;

    },

    // ============================================
    // UPDATE MEMBER
    // ============================================

    updateSMCMember: async (
        id,
        data
    ) => {

        const formData =
            new FormData();

        Object.keys(data).forEach(
            (key) => {

                const value =
                    data[key];

                if (
                    value === null ||
                    value === undefined ||
                    value === ""
                ) {

                    return;

                }

                if (
                    key === "photo" &&
                    typeof value === "string"
                ) {

                    return;

                }

                formData.append(
                    key,
                    value
                );

            }
        );

        const response =
            await api.put(
                `${BASE_URL}${id}/`,
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data",
                    },
                }
            );

        return response.data;

    },

    // ============================================
    // DELETE MEMBER
    // ============================================

    deleteSMCMember: async (
        id
    ) => {

        const response =
            await api.delete(
                `${BASE_URL}${id}/`
            );

        return response.data;

    },

};

export default smcMemberService;