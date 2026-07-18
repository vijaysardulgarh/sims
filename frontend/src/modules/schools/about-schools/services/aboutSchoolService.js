import api from "../../../../services/api/axios";

export const ENDPOINT =
    "/schools/about-schools/";

const aboutSchoolService = {

    getAboutSchools: (params = {}) =>
        api.get(
            ENDPOINT,
            {
                params,
            }
        ),

    getAboutSchool: (id) =>
        api.get(
            `${ENDPOINT}${id}/`
        ),

    createAboutSchool: (data) =>
        api.post(
            ENDPOINT,
            data
        ),

    updateAboutSchool: (
        id,
        data
    ) =>
        api.put(
            `${ENDPOINT}${id}/`,
            data
        ),

    deleteAboutSchool: (id) =>
        api.delete(
            `${ENDPOINT}${id}/`
        ),
};

export default aboutSchoolService;